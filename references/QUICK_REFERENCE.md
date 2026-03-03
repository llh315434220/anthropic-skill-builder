# Anthropic Skill Design Quick Reference

## Metadata Format
```yaml
---
name: skill-name  # lowercase, hyphens only
description: What it does + COMPREHENSIVE when-to-use triggers (ALL triggering logic HERE)
---
```

## File Structure
```
skill-name/
├── SKILL.md                    # Required: <500 lines
├── scripts/                    # Optional: executable code
│   └── example.py
├── references/                 # Optional: docs for Claude to read
│   ├── ADVANCED.md
│   └── API_DOCS.md
└── assets/                     # Optional: templates/images for output
    └── template.html
```

## Writing Rules
- **Imperative voice**: "Read X.md" not "You can read X.md"
- **No meta-docs**: No README, CHANGELOG, INSTALLATION_GUIDE
- **Concise**: <500 lines in SKILL.md
- **Split when large**: Move details to references/
- **Table of contents**: For references >100 lines

## When to Use Each Resource Type

### scripts/
✅ Repetitive code being rewritten
✅ Fragile operations needing deterministic execution
✅ Complex algorithms
❌ Simple one-liners Claude can write

### references/
✅ API documentation
✅ Database schemas
✅ Domain-specific knowledge
✅ Framework-specific patterns
❌ General knowledge Claude already has

### assets/
✅ Templates to copy/modify
✅ Images, fonts, icons
✅ Boilerplate code
❌ Documentation (use references/)

## Progressive Disclosure Pattern
```markdown
# Skill Title

## Quick Start
[1-2 essential examples for 80% of use cases]

## Advanced Features
- **Feature A**: See [FEATURE_A.md](references/FEATURE_A.md)
- **Multiple frameworks**: See [FRAMEWORKS.md](references/FRAMEWORKS.md)

## Scripts
- `scripts/tool.py` — Description
```

## Common Mistakes

| ❌ Don't | ✅ Do |
|----------|-------|
| Put triggering logic in body | Put ALL triggers in description |
| Create README.md | Put everything in SKILL.md |
| Explain general concepts | Only non-obvious procedural knowledge |
| Write >500 line SKILL.md | Split into references/ files |
| Use nested references | Keep references one level deep |

## Validation Checklist
- [ ] description includes ALL triggering scenarios
- [ ] SKILL.md <500 lines
- [ ] No README/CHANGELOG/meta-docs
- [ ] References have table of contents if >100 lines
- [ ] All scripts tested
- [ ] Imperative voice throughout
