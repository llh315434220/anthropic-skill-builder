# How to Use Anthropic Skill Builder

## Table of Contents
- Quick Creation
- Workflow Example
- Best Practices Checklist
- Common Scenarios
- Troubleshooting
- Reference Patterns

## Quick Creation

### Interactive
Just ask me:
```
"Create a skill for PDF processing"
"Build a skill to query our BigQuery database"
"I need a skill for rotating images"
```

I'll guide you through:
1. Understanding use cases
2. Planning resources (scripts/references/assets)
3. Creating the structure
4. Writing SKILL.md following Anthropic patterns

### Command Line
```bash
# Create new skill
~/.openclaw/skills/anthropic-skill-builder/scripts/create_skill.py \
  my-skill \
  --description "What it does + when to use it" \
  --resources scripts,references

# Validate existing skill
~/.openclaw/skills/anthropic-skill-builder/scripts/validate_skill.py \
  ~/.openclaw/skills/my-skill
```

## Workflow Example

### 1. Start with Concrete Examples
**User**: "I want a skill for analyzing travel expenses"

**Me**: "Can you give 3-5 examples of how you'd use this?"

**User**:
- "Show me total travel expenses this month"
- "Who spent the most on hotels last quarter?"
- "Are there any expenses above $1000?"

### 2. Plan Resources
**Me**: "Here's what I'll create:
- `references/database_schema.md` — Travel expense table definitions
- `references/common_queries.md` — Template queries for frequent analyses
- `scripts/generate_report.py` — Monthly expense report generator"

### 3. Create Structure
```bash
~/.openclaw/skills/travel-analyst/
├── SKILL.md
├── scripts/
│   └── generate_report.py
└── references/
    ├── database_schema.md
    └── common_queries.md
```

### 4. Write SKILL.md
```yaml
---
name: travel-analyst
description: Analyze corporate travel expenses from database. Use when: user asks about travel spending, hotel costs, trip analysis, expense reports, or queries travel-related tables.
---

# Travel Expense Analyst

## Quick Start
Common queries:

**Total expenses this month**:
```sql
SELECT SUM(amount) FROM travel_expenses
WHERE date >= DATE_TRUNC('month', CURRENT_DATE)
```

## Advanced Analysis
- **Database Schema**: See [database_schema.md](references/database_schema.md)
- **Query Templates**: See [common_queries.md](references/common_queries.md)

## Scripts
- `scripts/generate_report.py` — Monthly expense summary report
```

### 5. Validate & Package
```bash
# Validate
~/.openclaw/skills/anthropic-skill-builder/scripts/validate_skill.py \
  ~/.openclaw/skills/travel-analyst

# Package
cd ~/.openclaw/skills
zip -r travel-analyst.skill travel-analyst/
```

## Best Practices Checklist

### Before You Start
- [ ] Have 3-5 concrete use case examples
- [ ] Know what data/resources skill needs
- [ ] Understand triggering scenarios

### Writing SKILL.md
- [ ] Description includes ALL "when to use" triggers
- [ ] Body <500 lines
- [ ] Use imperative voice ("Read X", not "You can read X")
- [ ] Split large sections into references/

### Resources
- [ ] Test all scripts before packaging
- [ ] Reference files >100 lines have table of contents
- [ ] No meta-docs (README, CHANGELOG, etc.)
- [ ] Assets/ only contains output templates, not documentation

### After Creation
- [ ] Run validate_skill.py
- [ ] Test skill on real examples
- [ ] Iterate based on usage
- [ ] Package and distribute

## Common Scenarios

### Scenario 1: Database Query Skill
**Resources needed**:
- `references/schema.md` — Table definitions
- `references/common_queries.md` — Query templates

**SKILL.md focus**: Query patterns, how to read schemas

### Scenario 2: Document Processing
**Resources needed**:
- `scripts/process.py` — Fragile conversion logic
- `assets/template.docx` — Output template

**SKILL.md focus**: When to use script vs. manual code

### Scenario 3: Multi-Framework Tool
**Resources needed**:
- `references/aws.md` — AWS-specific patterns
- `references/gcp.md` — GCP-specific patterns

**SKILL.md focus**: Framework selection, common workflow

## Troubleshooting

### "Skill doesn't trigger correctly"
→ Fix the description field. ALL triggering logic must be there.

### "SKILL.md is too long"
→ Split into references/. Keep only navigation and core workflow.

### "Claude recreates code instead of using scripts"
→ Make script usage clearer in SKILL.md. Show exact command with examples.

### "References aren't being loaded"
→ Make sure SKILL.md explicitly mentions when to read each reference.

## Reference Patterns

See full guide: [PATTERNS.md](PATTERNS.md)

Quick summary:
- **Multi-framework**: Split by framework (aws.md, gcp.md)
- **Basic + Advanced**: Link advanced features to separate files
- **Database**: Split schema by domain (finance.md, sales.md)
- **Template-based**: Store templates in assets/, brief usage in SKILL.md
- **Script-heavy**: List scripts with usage examples
