---
name: pdf-processing
description: "PDF manipulation with rotation, merging, splitting, and text extraction. Use when: user mentions PDF files, asks to rotate/merge/split documents, needs to extract text from PDFs, works with scanned documents, or requires form filling or password protection."
---

# PDF Processing

Process PDF files: rotate, merge, split, extract text, and more.

## Quick Start

### Common Operations

**Rotate PDF pages**:
```bash
python3 scripts/rotate_pdf.py input.pdf --pages 1,3,5 --angle 90 --output rotated.pdf
```

**Merge multiple PDFs**:
```bash
python3 scripts/merge_pdfs.py file1.pdf file2.pdf file3.pdf --output merged.pdf
```

**Extract text** (basic):
```python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        print(text)
```

## Advanced Features

For complex scenarios, see:

- **Form Filling**: [FORMS.md](references/FORMS.md) — Fill PDF forms programmatically
- **Password Protection**: [ENCRYPTION.md](references/ENCRYPTION.md) — Add/remove passwords

## Scripts Available

### rotate_pdf.py
Rotate pages without quality loss.

```bash
# Rotate specific pages
python3 scripts/rotate_pdf.py input.pdf --pages 1,3,5 --angle 90 --output output.pdf

# Rotate all pages
python3 scripts/rotate_pdf.py input.pdf --angle 180 --output output.pdf
```

### merge_pdfs.py
Combine multiple PDFs into one.

```bash
# Basic merge
python3 scripts/merge_pdfs.py file1.pdf file2.pdf --output merged.pdf

# Preserve bookmarks
python3 scripts/merge_pdfs.py file1.pdf file2.pdf --preserve-bookmarks --output merged.pdf
```

## Dependencies

```bash
pip install pypdf pdfplumber
```

## Common Workflows

1. **Prepare scanned documents**:
   - Rotate pages to correct orientation
   - Merge multiple scans into one PDF
   - Extract text with pdfplumber

2. **Process forms**:
   - Read [FORMS.md](references/FORMS.md)
   - Fill fields using scripts
   - Flatten to prevent further editing

3. **Secure documents**:
   - Read [ENCRYPTION.md](references/ENCRYPTION.md)
   - Add password protection
   - Set permissions (print/copy restrictions)
