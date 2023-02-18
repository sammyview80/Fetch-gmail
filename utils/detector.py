import magic

def is_pdf(file_path):
    mime = magic.Magic(mime=True)
    file_mime_type = mime.from_file(file_path)
    return file_mime_type == 'application/pdf'

def is_ppt(file_path):
    mime = magic.Magic(mime=True)
    file_mime_type = mime.from_file(file_path)
    return file_mime_type == 'application/vnd.ms-powerpoint'

def is_docx(file_path):
    mime = magic.Magic(mime=True)
    file_mime_type = mime.from_file(file_path)
    return file_mime_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document" or file_mime_type == "application/msword"

def is_xlsx(file_path):
    mime = magic.Magic(mime=True)
    file_mime_type = mime.from_file(file_path)
    return file_mime_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" or file_mime_type == "application/vnd.ms-excel"

def is_image(file_path):
    mime = magic.Magic(mime=True)
    file_mime_type = mime.from_file(file_path)
    return file_mime_type == 'image/jpeg' or file_mime_type == 'image/png' or file_mime_type == 'image/bmp' or file_mime_type == 'image/jpg' or file_mime_type == 'image/webp'