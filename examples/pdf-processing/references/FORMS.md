# PDF Form Filling

Fill PDF forms programmatically using PyPDF.

## Table of Contents
- Reading Form Fields
- Filling Form Fields
- Flattening Forms
- Common Issues

## Reading Form Fields

```python
from pypdf import PdfReader

reader = PdfReader("form.pdf")
fields = reader.get_fields()

# Print all field names
for field_name, field_data in fields.items():
    print(f"Field: {field_name}")
    print(f"  Type: {field_data.get('/FT')}")
    print(f"  Value: {field_data.get('/V')}")
```

## Filling Form Fields

```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader("form.pdf")
writer = PdfWriter()

# Clone pages
for page in reader.pages:
    writer.add_page(page)

# Fill fields
writer.update_page_form_field_values(
    writer.pages[0],  # Page containing the form
    {
        "name": "John Doe",
        "email": "john@example.com",
        "date": "2026-03-03"
    }
)

# Save
with open("filled_form.pdf", "wb") as f:
    writer.write(f)
```

## Flattening Forms

After filling, flatten to prevent further editing:

```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader("filled_form.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

# Flatten: merge form fields into page content
writer.flatten()

with open("flattened_form.pdf", "wb") as f:
    writer.write(f)
```

## Common Issues

### Issue: Field names not found
**Solution**: Extract field names first:
```python
fields = reader.get_fields()
print(list(fields.keys()))
```

### Issue: Values not appearing
**Cause**: Field type mismatch or wrong page
**Solution**: Check field type and page number:
```python
for page_num, page in enumerate(reader.pages):
    annotations = page.get("/Annots")
    if annotations:
        print(f"Page {page_num} has form fields")
```

### Issue: Form appears blank after filling
**Cause**: Need to flatten
**Solution**: Call `writer.flatten()` before saving

## Advanced: Multi-Page Forms

```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader("multipage_form.pdf")
writer = PdfWriter()

# Clone all pages
for page in reader.pages:
    writer.add_page(page)

# Fill fields on each page
form_data = {
    0: {"page1_field": "Value 1"},  # Page 0 fields
    1: {"page2_field": "Value 2"},  # Page 1 fields
}

for page_num, fields in form_data.items():
    writer.update_page_form_field_values(
        writer.pages[page_num],
        fields
    )

with open("filled_multipage.pdf", "wb") as f:
    writer.write(f)
```

## Resources

- PyPDF Documentation: https://pypdf.readthedocs.io/
- PDF Form Field Types: https://www.adobe.com/devnet-docs/acrobatetk/tools/DigSig/Acrobat_DigitalSignatures_in_PDF.pdf
