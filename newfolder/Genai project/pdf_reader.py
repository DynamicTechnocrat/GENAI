#pip install pypdf
from pypdf import PdfReader

pages = PdfReader("student.pdf").pages

content = []
for page in pages:
    text = page.extract_text()
    content.append(text)
print(len(content))