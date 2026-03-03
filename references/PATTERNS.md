# Anthropic Skill Design Patterns

## Table of Contents
- Pattern 1: Multi-Framework/Domain Skill
- Pattern 2: Basic + Advanced Skill
- Pattern 3: Database Query Skill
- Pattern 4: Template-Based Skill
- Pattern 5: Script-Heavy Skill
- Key Design Principles

## Pattern 1: Multi-Framework/Domain Skill

**Problem**: Skill supports multiple frameworks (AWS/GCP/Azure) or domains (finance/sales/marketing). Loading all details wastes context.

**Solution**: Keep overview in SKILL.md, split framework-specific details into separate references.

### Structure
```
cloud-deploy/
├── SKILL.md              # Core workflow + framework selection
└── references/
    ├── aws.md            # AWS-specific patterns
    ├── gcp.md            # GCP-specific patterns
    └── azure.md          # Azure-specific patterns
```

### SKILL.md Example
```markdown
# Cloud Deployment

## Quick Start
1. User selects cloud provider (AWS/GCP/Azure)
2. Read provider-specific guide

## Provider Guides
- **AWS**: See [aws.md](references/aws.md) for AWS deployment patterns
- **GCP**: See [gcp.md](references/gcp.md) for GCP deployment patterns  
- **Azure**: See [azure.md](references/azure.md) for Azure deployment patterns

## Common Steps
[Shared workflow that applies to all providers]
```

## Pattern 2: Basic + Advanced Skill

**Problem**: Skill has simple common use cases and complex edge cases. Don't want to load advanced details for simple queries.

**Solution**: Show basic workflow in SKILL.md, link to advanced guides.

### Structure
```
pdf-processing/
├── SKILL.md
└── references/
    ├── FORMS.md          # Form filling
    ├── ENCRYPTION.md     # Password protection
    └── OOXML.md          # Low-level XML editing
```

### SKILL.md Example
```markdown
# PDF Processing

## Quick Start
Most common operations:

**Extract text**:
```python
import pdfplumber
with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

**Rotate pages**: Use `scripts/rotate_pdf.py`

## Advanced Features
- **Form filling**: See [FORMS.md](references/FORMS.md)
- **Encryption**: See [ENCRYPTION.md](references/ENCRYPTION.md)  
- **OOXML editing**: See [OOXML.md](references/OOXML.md)

## Scripts
- `scripts/rotate_pdf.py` — Rotate pages without quality loss
- `scripts/merge_pdfs.py` — Combine multiple PDFs
```

## Pattern 3: Database Query Skill

**Problem**: Database queries require knowing schemas, but schemas are huge. Don't want to load irrelevant tables.

**Solution**: Split schema by domain. Claude loads only relevant domain.

### Structure
```
bigquery-analytics/
├── SKILL.md                # Query patterns + domain navigation
└── references/
    ├── finance_schema.md   # Revenue, billing tables
    ├── sales_schema.md     # Opportunities, pipeline tables
    └── product_schema.md   # Features, usage tables
```

### SKILL.md Example
```markdown
# BigQuery Analytics

## Query Process
1. Identify domain (finance/sales/product)
2. Read relevant schema
3. Write query

## Domain Schemas
- **Finance**: See [finance_schema.md](references/finance_schema.md)
- **Sales**: See [sales_schema.md](references/sales_schema.md)
- **Product**: See [product_schema.md](references/product_schema.md)

## Common Patterns
```sql
-- Date filtering template
SELECT * FROM table
WHERE date >= '2024-01-01'
  AND date < '2024-02-01'
```
```

## Pattern 4: Template-Based Skill

**Problem**: Skill generates documents/code from templates. Templates are large binary/boilerplate files.

**Solution**: Store templates in assets/, provide brief usage instructions.

### Structure
```
frontend-webapp/
├── SKILL.md
└── assets/
    ├── react-template/   # Boilerplate React app
    ├── html-template/    # Vanilla HTML/CSS/JS
    └── styles.css
```

### SKILL.md Example
```markdown
# Frontend Webapp Builder

## Quick Start
1. Ask user to choose framework (React or vanilla HTML)
2. Copy appropriate template from assets/
3. Customize based on requirements

## Templates
- `assets/react-template/` — React 18 with Vite
- `assets/html-template/` — Vanilla HTML5/CSS3/ES6

## Customization Steps
1. Update title and meta tags
2. Modify color scheme in styles.css
3. Add required components
4. Test in browser
```

## Pattern 5: Script-Heavy Skill

**Problem**: Task requires running multiple fragile/complex scripts. Claude shouldn't rewrite them.

**Solution**: Store tested scripts, provide clear usage docs.

### Structure
```
video-processing/
├── SKILL.md
└── scripts/
    ├── extract_frames.py
    ├── add_subtitles.py
    └── compress_video.sh
```

### SKILL.md Example
```markdown
# Video Processing

## Available Scripts

### Extract Frames
```bash
python3 scripts/extract_frames.py input.mp4 --fps 1 --output frames/
```

### Add Subtitles
```bash
python3 scripts/add_subtitles.py input.mp4 subtitles.srt --output output.mp4
```

### Compress Video
```bash
bash scripts/compress_video.sh input.mp4 output.mp4 --quality medium
```

## Common Workflows
1. **Create thumbnail**: Extract frame at 00:00:05
2. **Add captions**: Use add_subtitles.py with SRT file
3. **Optimize size**: Run compress_video.sh with quality=medium
```

## Key Design Principles

### 1. Load Order Matters
Claude sees this order:
1. Description (always loaded)
2. SKILL.md body (when triggered)
3. References (when Claude reads them)

**Implication**: Put triggering logic in description, not body.

### 2. One Reference Level Deep
❌ Don't:
```
references/
  ├── advanced/
  │   ├── patterns.md    # Nested!
  │   └── examples.md
```

✅ Do:
```
references/
  ├── advanced_patterns.md
  └── advanced_examples.md
```

### 3. Table of Contents for Long References
For files >100 lines:
```markdown
# Database Schema

## Table of Contents
- Users Table
- Orders Table
- Products Table
- Relationships

## Users Table
[Details...]
```

### 4. Avoid Duplication
Information should exist in ONLY ONE place:
- Core workflow → SKILL.md
- Domain-specific details → references/
- Executable code → scripts/
- Output templates → assets/

### 5. Test All Scripts
```bash
# Before packaging
cd scripts/
python3 example_script.py --test
./another_script.sh --dry-run
```
