import pdfplumber


def extract_pdf_text(filepath):

    pages_text = []

    with pdfplumber.open(filepath) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:
                pages_text.append(text)

    return "\n".join(pages_text)