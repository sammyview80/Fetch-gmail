from __future__ import print_function

import os
import json

from utils.search_message import search_messages
from utils.read_message import read_message
from utils.delete_message import delete_messages_with_query, delete_message_with_id
from authenticate.get_authenticate import get_authenticate
from utils.pdf_detector import is_pdf_ppt_docx


class Main: 
    def __init__(self):
        self.creds = None
        self.service = get_authenticate()

    def fetch_result(self, query=None):
        """Request a list of all the messages"""
        return self.service.users().messages().list(userId="me", q=query).execute() if query else self.service.users().messages().list(userId="me").execute()
    
    def display_message(self, message_id):
        """This will save the mail in the Mails folder and display on command line"""
        read_message(self.service, message_id)

    def search_message(self, query):
        """This will return the message Id and you have to read the message with function display_message"""
        return search_messages(self.service, query)

    def delete_message_with_id(self, message_id):
        """This will delete the message with the id"""
        return delete_message_with_id(self.service, message_id)
    
    def delete_messages_with_query(self, query):    
        """This will delete the message with the query"""
        return delete_messages_with_query(self.service, query)
    
    def main(self):
        messages = self.search_message('Nepal Engineering College')
        for msg in messages:
            self.display_message(msg)
    

class ClassifyMail: 
    def __init__(self, root_path=os.getcwd()):
        self.root_path = root_path

    def classify(self):
        pass

    def check_pdf(self, mail):
        mail_path = os.path.join(self.root_path, mail)
        for folders in os.listdir(mail_path):
            folder_path = os.path.join(mail_path, folders)
            print('\n')
            print(f'Checking folder: {folder_path}')
            try: 
                for file in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, file)
                    if is_pdf_ppt_docx(file_path):
                        print(f'{file} is a PDF.')
                        if os.path.exists(os.path.join(self.root_path, 'Pdf_file_paths.json')):
                            with open('Pdf_file_paths.json', 'r') as f:
                                try: 
                                    file = json.load(f)
                                except Exception as e:
                                    print(f"Error: {e}.")
                            with open('Pdf_file_paths.json', 'w') as f:
                                pdf_file_path_array = file['paths']
                                pdf_file_path_array.append(file_path) if file_path not in pdf_file_path_array else None
                                json.dump({'paths': pdf_file_path_array}, f)

                        else:
                            with open(os.path.join(self.root_path, 'Pdf_file_paths.json'), 'w') as f:
                                json.dump({'paths': [file_path]}, f)

                    else:
                        try:
                            os.remove(file_path)
                            print(f'{file} is not a PDF. So Removed it.')
                        except OSError as e:
                            print(f"Error: {e.file} - {e.strerror}.")

            except NotADirectoryError as e:
                print(f"Error: {e}.")
            try:
                if(os.listdir(folder_path) == []):
                    os.rmdir(folder_path)
            except Exception as e:
                print(f"Error: {e}.")

if __name__ == "__main__":
    # Main().main()
    ClassifyMail().check_pdf('Mails')
