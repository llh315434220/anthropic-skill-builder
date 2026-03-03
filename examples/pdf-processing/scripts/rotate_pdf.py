#!/usr/bin/env python3
"""
Rotate PDF pages without quality loss.

Usage:
    python3 rotate_pdf.py input.pdf --pages 1,3,5 --angle 90 --output rotated.pdf
    python3 rotate_pdf.py input.pdf --angle 180 --output rotated.pdf  # Rotate all pages
"""

import argparse
from pathlib import Path
from pypdf import PdfReader, PdfWriter


def rotate_pages(input_pdf: Path, output_pdf: Path, pages: list[int] | None, angle: int):
    """Rotate specified pages in PDF.
    
    Args:
        input_pdf: Input PDF file path
        output_pdf: Output PDF file path
        pages: List of page numbers to rotate (1-indexed), or None for all pages
        angle: Rotation angle (90, 180, 270)
    """
    if angle not in [90, 180, 270]:
        raise ValueError("Angle must be 90, 180, or 270")
    
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    
    for i, page in enumerate(reader.pages):
        page_num = i + 1  # 1-indexed for user
        
        if pages is None or page_num in pages:
            page.rotate(angle)
        
        writer.add_page(page)
    
    with open(output_pdf, 'wb') as f:
        writer.write(f)
    
    print(f"✅ Rotated PDF saved to: {output_pdf}")


def main():
    parser = argparse.ArgumentParser(description="Rotate PDF pages without quality loss")
    parser.add_argument('input', type=Path, help="Input PDF file")
    parser.add_argument('--pages', type=str, help="Pages to rotate (comma-separated, 1-indexed). Omit to rotate all.")
    parser.add_argument('--angle', type=int, required=True, choices=[90, 180, 270], help="Rotation angle")
    parser.add_argument('--output', type=Path, required=True, help="Output PDF file")
    
    args = parser.parse_args()
    
    # Parse pages
    pages = None
    if args.pages:
        pages = [int(p.strip()) for p in args.pages.split(',')]
    
    rotate_pages(args.input, args.output, pages, args.angle)


if __name__ == '__main__':
    main()
