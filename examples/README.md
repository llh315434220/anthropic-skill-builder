# Example Skills

This directory contains real-world examples of well-structured skills following Anthropic's design patterns.

## Available Examples

### 1. [PDF Processing](pdf-processing/)
**Pattern**: Basic + Advanced Skill

Demonstrates:
- Common operations in SKILL.md
- Advanced features in references/
- Executable scripts for fragile operations
- Progressive disclosure in action

**Structure**:
```
pdf-processing/
├── SKILL.md              # Core workflow (rotate, merge, extract)
├── scripts/
│   ├── rotate_pdf.py     # Lossless rotation
│   └── merge_pdfs.py     # Combine multiple PDFs
├── references/
│   ├── FORMS.md          # Form filling guide
│   └── ENCRYPTION.md     # Password protection
└── assets/
    └── template.pdf      # Blank template
```

**Key Features**:
- ✅ SKILL.md < 200 lines (well under 500 limit)
- ✅ Scripts for fragile operations (avoid rewriting)
- ✅ Advanced features split into references
- ✅ Clear navigation from main skill

**When to use this pattern**:
- You have 3-5 common operations (80% of use cases)
- Advanced features exist but rarely used
- Some operations are fragile (rotation, encryption)

## Using These Examples

### Copy as Starting Point

```bash
# Copy example to your skills directory
cp -r examples/pdf-processing ~/.openclaw/skills/my-pdf-skill

# Customize for your use case
cd ~/.openclaw/skills/my-pdf-skill
# Edit SKILL.md, scripts, references
```

### Learn from Structure

Study how these examples:
1. **Minimize SKILL.md** — Keep under 500 lines
2. **Split references** — Domain-specific details separate
3. **Package scripts** — Don't make Claude rewrite fragile code
4. **Navigate clearly** — Easy to find what you need

### Adapt Patterns

Take the pattern, not the exact code:
- **PDF Processing** → Image Processing, Video Editing
- **Database Query** → API Integration, Log Analysis
- **Multi-Framework** → Multi-Cloud, Multi-Language

## More Examples Coming Soon

- [ ] **database-query** — Split schemas by domain
- [ ] **cloud-deploy** — Multi-framework (AWS/GCP/Azure)
- [ ] **frontend-webapp** — Template-based generation
- [ ] **video-processing** — Script-heavy workflow

## Contributing Examples

Have a well-structured skill? Share it!

1. Create example in `examples/your-skill-name/`
2. Add entry to this README
3. Document key design decisions
4. Submit PR

See [CONTRIBUTING.md](../CONTRIBUTING.md) for details.
