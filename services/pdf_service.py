import fitz


def extract_text(upload_file):

    pdf = fitz.open(stream=upload_file.file.read(), filetype="pdf")

    text = ""

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text
