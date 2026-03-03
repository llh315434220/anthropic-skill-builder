#!/usr/bin/env python3
"""
Anthropic Skill Builder - Interactive skill creation following official design patterns
"""
import os
import sys
import argparse
from pathlib import Path

SKILL_MD_TEMPLATE = """---
name: {name}
description: {description}
---

# {title}

Brief introduction to the skill.

## Quick Start

[1-2 essential examples that cover 80% of use cases]

## Advanced Features

- **Feature A**: See [FEATURE_A.md](references/FEATURE_A.md)
- **Feature B**: See [FEATURE_B.md](references/FEATURE_B.md)

## Scripts

- `scripts/example.py` — Description and usage
"""

REFERENCE_TEMPLATE = """# {title}

## Table of Contents
- Section 1
- Section 2

## Section 1

Content...

## Section 2

More content...
"""

def normalize_name(name: str) -> str:
    """Convert name to hyphen-case lowercase"""
    return name.lower().replace(' ', '-').replace('_', '-')

def create_skill(name: str, description: str, resources: list, output_dir: Path):
    """Create a new skill with specified structure"""
    skill_name = normalize_name(name)
    skill_dir = output_dir / skill_name
    
    if skill_dir.exists():
        print(f"❌ Error: Skill directory already exists: {skill_dir}")
        return False
    
    # Create main directory
    skill_dir.mkdir(parents=True)
    print(f"✅ Created skill directory: {skill_dir}")
    
    # Create resource directories
    for resource in resources:
        (skill_dir / resource).mkdir()
        print(f"✅ Created {resource}/ directory")
    
    # Create SKILL.md
    skill_md = skill_dir / "SKILL.md"
    title = name.replace('-', ' ').title()
    content = SKILL_MD_TEMPLATE.format(
        name=skill_name,
        description=description,
        title=title
    )
    skill_md.write_text(content)
    print(f"✅ Created SKILL.md")
    
    # Create example reference if references directory was requested
    if 'references' in resources:
        ref_file = skill_dir / "references" / "EXAMPLE.md"
        ref_content = REFERENCE_TEMPLATE.format(title="Example Reference")
        ref_file.write_text(ref_content)
        print(f"✅ Created references/EXAMPLE.md")
    
    # Create example script if scripts directory was requested
    if 'scripts' in resources:
        script_file = skill_dir / "scripts" / "example.py"
        script_content = """#!/usr/bin/env python3
\"\"\"
Example script for {skill_name} skill
\"\"\"
import sys

def main():
    print("Example script executed")
    # Add your logic here

if __name__ == "__main__":
    main()
""".format(skill_name=skill_name)
        script_file.write_text(script_content)
        script_file.chmod(0o755)
        print(f"✅ Created scripts/example.py")
    
    print(f"\n🎉 Skill created successfully!")
    print(f"\nNext steps:")
    print(f"1. Edit {skill_dir}/SKILL.md")
    print(f"2. Add scripts, references, or assets as needed")
    print(f"3. Test the skill")
    print(f"4. Package: cd ~/.openclaw/skills && zip -r {skill_name}.skill {skill_name}/")
    
    return True

def main():
    parser = argparse.ArgumentParser(
        description="Create a new Anthropic-style skill for OpenClaw"
    )
    parser.add_argument("name", help="Skill name (will be normalized to hyphen-case)")
    parser.add_argument("--description", "-d", required=True, 
                       help="Skill description (including when-to-use triggers)")
    parser.add_argument("--resources", "-r", default="scripts,references",
                       help="Comma-separated list: scripts,references,assets")
    parser.add_argument("--output", "-o", default=str(Path.home() / ".openclaw/skills"),
                       help="Output directory (default: ~/.openclaw/skills)")
    
    args = parser.parse_args()
    
    resources = [r.strip() for r in args.resources.split(',') if r.strip()]
    output_dir = Path(args.output)
    
    if not output_dir.exists():
        output_dir.mkdir(parents=True)
    
    success = create_skill(args.name, args.description, resources, output_dir)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
