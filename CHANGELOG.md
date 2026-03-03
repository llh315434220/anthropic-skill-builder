# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-03-03

### Added
- Initial release of Anthropic Skill Builder
- Core skill creation workflow
- Progressive disclosure implementation
- Five key design patterns:
  - Multi-Framework/Domain Skill
  - Basic + Advanced Skill
  - Database Query Skill
  - Template-Based Skill
  - Script-Heavy Skill
- Documentation:
  - SKILL.md — Core skill implementation
  - PATTERNS.md — Detailed design patterns
  - QUICK_REFERENCE.md — Cheat sheet
  - USAGE.md — Usage guide
- Scripts:
  - create_skill.py — Scaffold new skills
  - validate_skill.py — Validate skill structure
- Comprehensive README with examples
- MIT License
- Contributing guidelines

### Documentation
- Based on Anthropic's Complete Guide to Building Skills for Claude
- Includes real-world examples from production skills
- Progressive disclosure principles explained with diagrams
- Best practices and common mistakes

### Community
- GitHub repository structure
- Issue templates (planned)
- PR templates (planned)
- Code of Conduct reference

## [Unreleased]

### Planned
- GitHub Actions CI/CD
- Automated skill validation on PR
- More design pattern examples
- Video tutorials
- Skill template generator
- Integration with OpenClaw skill marketplace

---

## Version History

### Version Numbering

We use Semantic Versioning (MAJOR.MINOR.PATCH):
- **MAJOR** — Incompatible API changes
- **MINOR** — New features (backward compatible)
- **PATCH** — Bug fixes (backward compatible)

### Release Process

1. Update CHANGELOG.md
2. Update version in scripts
3. Tag release: `git tag v1.0.0`
4. Push tags: `git push --tags`
5. Create GitHub release with notes

---

[1.0.0]: https://github.com/llh315434220/anthropic-skill-builder/releases/tag/v1.0.0
