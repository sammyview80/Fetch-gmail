import magic

def is_pdf_ppt_docx(file_path):
    mime = magic.Magic(mime=True)
    file_mime_type = mime.from_file(file_path)
    return file_mime_type == 'application/vnd.ms-powerpoint' or file_mime_type == 'application/pdf' or file_mime_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
