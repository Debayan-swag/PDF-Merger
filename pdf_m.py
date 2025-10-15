import os
from PyPDF2 import PdfWriter

# List of PDF files to merge
pdf_files = ["file1.pdf", "file2.pdf"]

# Create a PdfWriter object
merger = PdfWriter()

# Append each PDF safely
for pdf in pdf_files:
    if os.path.exists(pdf):
        merger.append(pdf)
        print(f"Added: {pdf}")
    else:
        print(f"File not found: {pdf}")

# Write the merged PDF
output_file = "merged-pdf.pdf"
merger.write(output_file)
merger.close()

