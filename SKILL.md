---
name: anthropic-skill-builder
description: "Create production-quality Claude/OpenClaw skills following Anthropic's official design patterns. Use when: designing new skills, improving existing skills, refactoring skill structure, or applying progressive disclosure patterns. Based on Anthropic's Complete Guide to Building Skills for Claude."
---

# Anthropic Skill Builder

Create and refactor skills following Anthropic's official design principles and patterns.

## Core Philosophy

**The context window is a public good.** Every token counts. Challenge each piece of information: "Does Claude really need this explanation?" Skills should provide **only non-obvious procedural knowledge**, not general capabilities Claude already has.

### Three-Level Progressive Disclosure

1. **Metadata (name + description)** — Always in context (~100 words)
   - Comprehensive triggering logic goes here
   - Include "when to use" information
   
2. **SKILL.md body** — Loaded when skill triggers (<500 lines)
   - Core workflow and navigation only
   - Link to references for details
   
3. **Bundled resources** — Loaded as needed
   - `scripts/` — Executable code
   - `references/` — Documentation to inform Claude's thinking
   - `assets/` — Files used in output (templates, icons, etc.)

## Skill Creation Workflow

### 1. Understand with Concrete Examples

Ask the user:
- What functionality should this skill support?
- Can you give 3-5 examples of how this would be used?
- What would trigger this skill?

**Output**: Clear list of use cases

### 2. Plan Reusable Contents

For each use case, identify:
- **Scripts**: Repetitive/fragile code that shouldn't be rewritten
- **References**: Schemas, API docs, domain knowledge
- **Assets**: Templates, boilerplate, fonts, images

**Output**: Resource list (scripts/references/assets)

### 3. Create Skill Structure

```bash
mkdir -p ~/.openclaw/skills/<skill-name>/{scripts,references,assets}
```

### 4. Write SKILL.md

#### Frontmatter (YAML)

```yaml
---
name: skill-name
description: What the skill does + comprehensive when-to-use triggers. Include ALL triggering logic here (not in body). Example: "PDF processing with rotation, merging, splitting. Use when: user mentions PDF files, asks to rotate/merge/split documents, needs to extract text from PDFs, or works with scanned documents."
---
```

#### Body (Markdown)

**Golden Rules:**
- **Concise is key** — Under 500 lines
- **Imperative form** — "Read X.md", not "You can read X.md"
- **No meta-documentation** — No README, INSTALLATION_GUIDE, CHANGELOG
- **Split when large** — Move details to references/ files

**Structure:**

```markdown
# Skill Name

## Quick Start

[1-2 essential examples that cover 80% of use cases]

## Advanced Features

- **Feature A**: See [FEATURE_A.md](references/FEATURE_A.md)
- **Feature B**: See [FEATURE_B.md](references/FEATURE_B.md)

## Scripts Available

- `scripts/example.py` — Description and usage
```

### 5. Create Reference Files

**When to split into references/**:
- Multiple domains/frameworks (e.g., AWS vs GCP vs Azure)
- Advanced features not needed for basic usage
- Long API documentation or schemas

**Structure large references** (>100 lines):
```markdown
# Reference Title

## Table of Contents
- Section 1
- Section 2

[Content...]
```

### 6. Write Scripts

```bash
# Test scripts before committing
python3 scripts/example.py --test
```

### 7. Package Skill

```bash
# OpenClaw doesn't have package_skill.py yet, so just:
cd ~/.openclaw/skills
zip -r skill-name.skill skill-name/
```

## Design Patterns

### Pattern 1: High-Level Guide with References

```markdown
# Multi-Framework Skill

## Quick Start
Basic example here.

## Framework-Specific Guides
- **AWS**: See [AWS.md](references/AWS.md)
- **GCP**: See [GCP.md](references/GCP.md)
```

### Pattern 2: Domain-Specific Organization

```
bigquery-skill/
├── SKILL.md          # Overview + navigation
└── references/
    ├── finance.md    # Finance queries
    ├── sales.md      # Sales queries
    └── product.md    # Product queries
```

### Pattern 3: Conditional Details

```markdown
# Core Workflow

Basic approach works for most cases.

**For advanced scenarios**: See [ADVANCED.md](references/ADVANCED.md)
**For specific edge cases**: See [EDGE_CASES.md](references/EDGE_CASES.md)
```

## Degrees of Freedom

Match specificity to task fragility:

| Freedom Level | When to Use | Format |
|---------------|-------------|--------|
| **High** | Multiple valid approaches | Text instructions |
| **Medium** | Preferred pattern exists | Pseudocode with parameters |
| **Low** | Fragile operations | Specific scripts |

## Common Mistakes to Avoid

❌ **Don't**:
- Put "when to use" logic in body (it won't be read before triggering)
- Create README.md, CHANGELOG.md, or other meta-docs
- Explain things Claude already knows
- Exceed 500 lines in SKILL.md without splitting

✅ **Do**:
- Make description comprehensive (it's your triggering logic)
- Split large skills into references/
- Test all scripts before packaging
- Use imperative voice ("Read X", not "You can read X")

## Iteration Checklist

After first use:
- [ ] Did it trigger correctly? (Fix description if not)
- [ ] Was SKILL.md too long? (Split into references if yes)
- [ ] Did Claude recreate code that should be a script?
- [ ] Were there missing references or assets?

## Resources

- Anthropic Official Guide: https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf
- OpenClaw skill-creator: /usr/lib/node_modules/openclaw/skills/skill-creator/
