# Contributing to Anthropic Skill Builder

Thank you for your interest in contributing! This document provides guidelines and best practices for contributing to this project.

## 🎯 Types of Contributions

We welcome:

- **New design patterns** — Share patterns you've discovered
- **Bug fixes** — Fix issues in existing patterns or scripts
- **Documentation** — Improve clarity, add examples
- **Scripts** — Useful tools for skill development
- **Examples** — Real-world skill examples

## 📝 How to Contribute

### 1. Fork and Clone

```bash
# Fork on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/anthropic-skill-builder.git
cd anthropic-skill-builder

# Add upstream remote
git remote add upstream https://github.com/ORIGINAL_OWNER/anthropic-skill-builder.git
```

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

Use descriptive branch names:
- `feature/add-async-pattern` — New features
- `fix/script-validation-bug` — Bug fixes
- `docs/improve-quick-start` — Documentation

### 3. Make Changes

Follow these guidelines:

#### Code Style
- Python: Follow PEP 8
- Shell scripts: Use shellcheck
- Markdown: Follow [markdownlint](https://github.com/DavidAnson/markdownlint)

#### Documentation
- Keep descriptions concise
- Use concrete examples
- Include "Why" and "When to use"
- Link to related resources

#### Patterns
When adding new patterns:
1. Add to `references/PATTERNS.md`
2. Include:
   - Problem description
   - Solution approach
   - Directory structure
   - Code example
   - When to use / not use

### 4. Test Your Changes

```bash
# For Python scripts
python3 scripts/your_script.py --test

# For shell scripts
shellcheck scripts/your_script.sh
bash scripts/your_script.sh --dry-run

# For skill validation
python3 scripts/validate_skill.py
```

### 5. Commit

Write clear commit messages:

```bash
git commit -m "feat: Add async workflow pattern"
git commit -m "fix: Correct script path in SKILL.md"
git commit -m "docs: Improve Progressive Disclosure explanation"
```

Follow [Conventional Commits](https://www.conventionalcommits.org/):
- `feat:` — New features
- `fix:` — Bug fixes
- `docs:` — Documentation
- `refactor:` — Code refactoring
- `test:` — Adding tests
- `chore:` — Maintenance

### 6. Push and Create PR

```bash
git push origin feature/your-feature-name
```

Then open a Pull Request on GitHub:

1. Go to your fork on GitHub
2. Click "Compare & pull request"
3. Fill in the PR template:
   - **Description** — What does this PR do?
   - **Motivation** — Why is this change needed?
   - **Testing** — How did you test it?
   - **Related Issues** — Link to relevant issues

## 🔍 Code Review Process

1. **Automated checks** — CI runs tests and linting
2. **Maintainer review** — A maintainer will review your PR
3. **Feedback** — Address any requested changes
4. **Approval** — Once approved, your PR will be merged

## 📋 PR Checklist

Before submitting:

- [ ] Code follows style guidelines
- [ ] Self-review of changes completed
- [ ] Commented complex/non-obvious code
- [ ] Documentation updated (if needed)
- [ ] No new warnings generated
- [ ] Tests added/updated (if applicable)
- [ ] All tests pass locally
- [ ] Commit messages are clear and descriptive

## 🐛 Reporting Issues

Found a bug? Please open an issue with:

1. **Clear title** — Summarize the problem
2. **Description** — What went wrong?
3. **Steps to reproduce** — How to trigger the bug?
4. **Expected behavior** — What should happen?
5. **Actual behavior** — What actually happened?
6. **Environment** — OS, OpenClaw version, etc.
7. **Screenshots/logs** — If applicable

**Example:**

```markdown
## Bug: Script validation fails on Windows

**Description**
The `validate_skill.py` script throws a path error on Windows.

**Steps to Reproduce**
1. Clone repo on Windows 11
2. Run `python scripts/validate_skill.py`
3. See error: "FileNotFoundError: [Errno 2] No such file or directory"

**Expected**
Script should validate skill structure.

**Actual**
Script crashes with path error.

**Environment**
- OS: Windows 11
- Python: 3.11.5
- OpenClaw: v2026.2.23
```

## 💡 Suggesting Features

Have an idea? Open an issue with:

1. **Problem statement** — What problem does this solve?
2. **Proposed solution** — How would it work?
3. **Alternatives** — Other approaches considered?
4. **Use cases** — Real-world examples?

## 🎨 Design Principles

When contributing, keep these in mind:

1. **Context is precious** — Minimize tokens loaded
2. **Progressive disclosure** — Show only what's needed
3. **Concrete over abstract** — Examples beat explanations
4. **User-first** — Optimize for skill users, not skill authors
5. **Test everything** — Scripts must work reliably

## 📖 Style Guide

### Markdown
- Use ATX-style headers (`#`)
- One sentence per line (easier diffs)
- Code blocks must specify language
- Link to related sections/files

### Python
```python
# Good
def create_skill(name: str, description: str) -> Path:
    """Create a new skill directory structure.
    
    Args:
        name: Skill name (lowercase-with-hyphens)
        description: One-line description
        
    Returns:
        Path to created skill directory
    """
    # Implementation...
```

### Shell
```bash
#!/usr/bin/env bash
set -euo pipefail  # Exit on error, undefined vars, pipe failures

# Good: Clear function names, descriptive variables
validate_skill_structure() {
    local skill_dir="$1"
    
    if [[ ! -f "${skill_dir}/SKILL.md" ]]; then
        echo "Error: Missing SKILL.md" >&2
        return 1
    fi
}
```

## 🏆 Recognition

Contributors will be:
- Listed in README.md
- Credited in release notes
- Invited to maintainer team (after sustained contributions)

## 📬 Questions?

- **GitHub Discussions** — Ask questions, share ideas
- **Discord** — Join [OpenClaw Community](https://discord.com/invite/clawd)
- **Email** — Contact maintainers (see README)

## 📜 Code of Conduct

Be respectful, inclusive, and constructive. We follow the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/).

---

**Thank you for contributing to Anthropic Skill Builder! 🎉**
