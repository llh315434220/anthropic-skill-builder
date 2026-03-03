#!/usr/bin/env python3
"""
Validate a skill against Anthropic design principles
"""
import sys
import re
from pathlib import Path
import yaml

class SkillValidator:
    def __init__(self, skill_dir: Path):
        self.skill_dir = Path(skill_dir)
        self.errors = []
        self.warnings = []
        self.info = []
    
    def validate(self):
        """Run all validation checks"""
        self.check_directory_structure()
        self.check_skill_md()
        self.check_no_meta_docs()
        self.check_references()
        return len(self.errors) == 0
    
    def check_directory_structure(self):
        """Check basic directory structure"""
        if not self.skill_dir.exists():
            self.errors.append(f"Skill directory does not exist: {self.skill_dir}")
            return
        
        skill_md = self.skill_dir / "SKILL.md"
        if not skill_md.exists():
            self.errors.append("SKILL.md is required but not found")
        
        self.info.append(f"✅ Skill directory exists: {self.skill_dir.name}")
    
    def check_skill_md(self):
        """Validate SKILL.md format and content"""
        skill_md = self.skill_dir / "SKILL.md"
        if not skill_md.exists():
            return
        
        content = skill_md.read_text()
        
        # Check frontmatter
        if not content.startswith('---\n'):
            self.errors.append("SKILL.md must start with YAML frontmatter (---)")
            return
        
        # Extract frontmatter
        parts = content.split('---\n', 2)
        if len(parts) < 3:
            self.errors.append("Invalid YAML frontmatter format")
            return
        
        try:
            frontmatter = yaml.safe_load(parts[1])
        except yaml.YAMLError as e:
            self.errors.append(f"Invalid YAML frontmatter: {e}")
            return
        
        # Check required fields
        if 'name' not in frontmatter:
            self.errors.append("Frontmatter must include 'name' field")
        else:
            # Validate name format
            name = frontmatter['name']
            if not re.match(r'^[a-z0-9-]+$', name):
                self.errors.append(f"Name must be lowercase with hyphens only: {name}")
            
            # Check directory name matches
            if name != self.skill_dir.name:
                self.warnings.append(f"Directory name ({self.skill_dir.name}) doesn't match skill name ({name})")
            
            self.info.append(f"✅ Skill name: {name}")
        
        if 'description' not in frontmatter:
            self.errors.append("Frontmatter must include 'description' field")
        else:
            desc = frontmatter['description']
            if len(desc) < 50:
                self.warnings.append("Description is very short (<50 chars). Should include comprehensive triggering logic.")
            if 'use when' not in desc.lower() and 'trigger' not in desc.lower():
                self.warnings.append("Description should include 'use when' or triggering scenarios")
            self.info.append(f"✅ Description length: {len(desc)} chars")
        
        # Check for extra frontmatter fields
        extra_fields = set(frontmatter.keys()) - {'name', 'description'}
        if extra_fields:
            self.warnings.append(f"Extra frontmatter fields (not needed): {extra_fields}")
        
        # Check body length
        body = parts[2]
        lines = body.split('\n')
        if len(lines) > 500:
            self.warnings.append(f"SKILL.md body is long ({len(lines)} lines). Consider splitting into references/")
        
        self.info.append(f"✅ SKILL.md body: {len(lines)} lines")
    
    def check_no_meta_docs(self):
        """Check for prohibited meta-documentation files"""
        prohibited = ['README.md', 'INSTALLATION.md', 'CHANGELOG.md', 'GUIDE.md', 
                     'SETUP.md', 'QUICKSTART.md', 'CONTRIBUTING.md']
        
        for file in prohibited:
            if (self.skill_dir / file).exists():
                self.errors.append(f"Remove meta-documentation file: {file}")
    
    def check_references(self):
        """Check references directory organization"""
        refs_dir = self.skill_dir / "references"
        if not refs_dir.exists():
            return
        
        for ref_file in refs_dir.glob('*.md'):
            content = ref_file.read_text()
            lines = content.split('\n')
            
            if len(lines) > 100:
                # Check for table of contents
                has_toc = any('table of contents' in line.lower() for line in lines[:20])
                if not has_toc:
                    self.warnings.append(f"{ref_file.name}: Long file (>{len(lines)} lines) should have Table of Contents")
            
            self.info.append(f"✅ Reference: {ref_file.name} ({len(lines)} lines)")
    
    def print_report(self):
        """Print validation report"""
        print("\n" + "="*60)
        print(f"SKILL VALIDATION: {self.skill_dir.name}")
        print("="*60)
        
        if self.errors:
            print("\n❌ ERRORS:")
            for error in self.errors:
                print(f"  - {error}")
        
        if self.warnings:
            print("\n⚠️  WARNINGS:")
            for warning in self.warnings:
                print(f"  - {warning}")
        
        if self.info:
            print("\nℹ️  INFO:")
            for info in self.info:
                print(f"  {info}")
        
        print("\n" + "="*60)
        if self.errors:
            print("❌ VALIDATION FAILED")
        else:
            print("✅ VALIDATION PASSED")
        print("="*60 + "\n")

def main():
    if len(sys.argv) < 2:
        print("Usage: validate_skill.py <skill-directory>")
        sys.exit(1)
    
    skill_dir = Path(sys.argv[1])
    validator = SkillValidator(skill_dir)
    success = validator.validate()
    validator.print_report()
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
