from pypdf import PdfReader

def parse_pdf(study_guide):
    reader = PdfReader(study_guide.file.path)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    
    study_guide.file_text_data = text
    study_guide.save()