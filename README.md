# Anthropic Skill Builder for OpenClaw

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw Compatible](https://img.shields.io/badge/OpenClaw-Compatible-blue.svg)](https://openclaw.ai)

**Create production-quality Claude/OpenClaw skills following Anthropic's official design patterns.**

This skill helps you design, structure, and refactor OpenClaw skills using **Progressive Disclosure** principles from [Anthropic's Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf).

## 🎯 What This Skill Does

Anthropic Skill Builder guides you through creating well-structured skills that:

- ✅ **Minimize context usage** — Only load what Claude needs, when it needs it
- ✅ **Follow official patterns** — Proven design patterns from Anthropic
- ✅ **Scale gracefully** — Handle simple and complex use cases efficiently
- ✅ **Are maintainable** — Clear structure, easy to update

## 🚀 Quick Start

### Installation

```bash
# For OpenClaw users
cd ~/.openclaw/skills
git clone https://github.com/YOUR_USERNAME/anthropic-skill-builder.git

# Restart OpenClaw gateway
openclaw gateway restart
```

### Usage

Once installed, the skill triggers automatically when you ask about:

- Creating new skills
- Improving existing skills
- Refactoring skill structure
- Applying progressive disclosure patterns

**Example prompts:**
```
"Help me create a skill for PDF processing"
"Refactor my database-query skill to use progressive disclosure"
"My skill is too long, how do I split it into references?"
```

## 📖 Core Concepts

### Progressive Disclosure (3 Levels)

Skills should reveal information progressively, not dump everything into context at once:

1. **Metadata** (~100 words, always loaded)
   - Skill name + comprehensive description
   - All triggering logic goes here

2. **SKILL.md** (<500 lines, loaded when triggered)
   - Core workflow and navigation
   - Links to detailed references

3. **Resources** (loaded as needed)
   - `scripts/` — Executable code
   - `references/` — Detailed documentation
   - `assets/` — Templates, images, etc.

### The Golden Rule

> **The context window is a public good.**
> 
> Every token counts. Ask: "Does Claude really need this?"
>
> Skills should provide **only non-obvious procedural knowledge**, not general capabilities Claude already has.

## 🏗️ Skill Structure

```
my-skill/
├── SKILL.md                 # Main skill file (< 500 lines)
├── scripts/                 # Executable scripts (avoid rewriting fragile code)
│   ├── example.py
│   └── helper.sh
├── references/              # Detailed docs (loaded on demand)
│   ├── API_REFERENCE.md
│   ├── ADVANCED_PATTERNS.md
│   └── TROUBLESHOOTING.md
└── assets/                  # Templates, images, config files
    ├── template.json
    └── icon.png
```

## 📚 Design Patterns

### Pattern 1: Multi-Framework Skill
For skills supporting multiple frameworks/domains (AWS/GCP/Azure):

```
cloud-deploy/
├── SKILL.md              # Overview + framework selection
└── references/
    ├── aws.md            # AWS-specific details
    ├── gcp.md            # GCP-specific details
    └── azure.md          # Azure-specific details
```

### Pattern 2: Basic + Advanced Skill
Common operations in SKILL.md, complex cases in references:

```
pdf-processing/
├── SKILL.md              # Common operations
└── references/
    ├── FORMS.md          # Form filling
    ├── ENCRYPTION.md     # Password protection
    └── OCR.md            # Text extraction
```

### Pattern 3: Database Query Skill
Split schemas by domain to avoid loading irrelevant tables:

```
database-analytics/
├── SKILL.md              # Query patterns
└── references/
    ├── finance_schema.md
    ├── sales_schema.md
    └── product_schema.md
```

[See more patterns in references/PATTERNS.md](references/PATTERNS.md)

## 🛠️ Workflow

1. **Understand** — Gather 3-5 concrete examples
2. **Plan** — Identify scripts, references, assets needed
3. **Structure** — Create directory layout
4. **Write SKILL.md** — Core workflow + navigation
5. **Create references** — Split domain-specific details
6. **Add scripts** — Package fragile/repetitive code
7. **Test** — Validate all scripts work

## 📋 Best Practices

### ✅ Do:
- Put ALL triggering logic in description (not body)
- Keep SKILL.md under 500 lines
- Split large skills into references/
- Use imperative voice: "Read X", not "You can read X"
- Test all scripts before committing

### ❌ Don't:
- Create README.md, CHANGELOG.md in skill directory (meta-docs belong in repo root)
- Exceed 500 lines in SKILL.md without splitting
- Explain things Claude already knows
- Nest references deeper than one level

## 📖 Documentation

- **[SKILL.md](SKILL.md)** — Core skill implementation
- **[PATTERNS.md](references/PATTERNS.md)** — Detailed design patterns with examples
- **[QUICK_REFERENCE.md](references/QUICK_REFERENCE.md)** — Cheat sheet for common tasks
- **[USAGE.md](references/USAGE.md)** — Detailed usage guide with examples

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-pattern`)
3. Commit your changes (`git commit -m 'Add amazing pattern'`)
4. Push to the branch (`git push origin feature/amazing-pattern`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Anthropic** for the [Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)
- **OpenClaw** team for the extensible skill system
- All contributors who help improve skill design patterns

## 🔗 Resources

- [Anthropic Official Guide (PDF)](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)
- [OpenClaw Documentation](https://docs.openclaw.ai)
- [OpenClaw GitHub](https://github.com/openclaw/openclaw)
- [Skill Creator Skill](https://github.com/openclaw/skills/tree/main/skill-creator)

## 📧 Support

- **Issues**: [GitHub Issues](https://github.com/YOUR_USERNAME/anthropic-skill-builder/issues)
- **Discord**: [OpenClaw Community](https://discord.com/invite/clawd)
- **Documentation**: [OpenClaw Docs](https://docs.openclaw.ai)

---

**Made with ❤️ for the OpenClaw community**
