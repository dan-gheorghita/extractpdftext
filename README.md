# extractpdftext.py

**Description of the Python Code**

This Python script extracts text from a PDF file and saves it to a new text file. It utilizes two different libraries, `pypdf` and `pdfminer`, to achieve this functionality. The script is designed to be robust and handle any potential errors that may occur during the text extraction process.

**Step-by-Step Explanation**

1. **Importing Libraries**: The script starts by importing the necessary libraries, `pypdf` and `pdfminer.high_level`, which are used for working with PDF files.
2. **Defining File Variables**: The script defines two variables, `PDF_FILENAME` and `TEXT_FILENAME`, which represent the input PDF file and output text file, respectively.
3. **Initializing an Empty String**: An empty string `text` is initialized to store the extracted text from the PDF file.
4. **Text Extraction Attempt**: The script attempts to use the `pypdf` library to read the PDF file and extract text