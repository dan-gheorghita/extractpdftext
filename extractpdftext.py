```python
# Import the necessary libraries for working with PDFs
import pypdf
import pdfminer.high_level

# Define the filename of the PDF to be processed and the filename of the output text file
PDF_FILENAME = 'Recursion_Chapter1.pdf'  # Input PDF filename
TEXT_FILENAME = 'recursion.txt'  # Output text filename

# Initialize an empty string to store the extracted text
text = ''

try:
    # Attempt to use the pypdf library to read the PDF
    reader = pypdf.PdfReader(PDF_FILENAME)
    # Iterate through each page of the PDF and extract the text
    for page in reader.pages:
        # Append the extracted text from the current page to the overall text
        text += page.extract_text()
except Exception:
    # If the previous attempt failed, use the pdfminer library as a fallback
    text = pdfminer.high_level.extract_text(PDF_FILENAME)

# Open the output text file in write mode with UTF-8 encoding
with open(TEXT_FILENAME, 'w', encoding='utf-8') as file_obj:
    # Write the extracted text to the output file
    file_obj.write(text)
```