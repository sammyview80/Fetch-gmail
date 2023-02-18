from __future__ import print_function

import os
import json

from utils.gmail.search_message import search_messages
from utils.gmail.read_message import read_message
from utils.gmail.delete_message import delete_messages_with_query, delete_message_with_id
from utils.gmail.get_authenticate import get_authenticate
from utils.detector import is_pdf, is_ppt, is_docx, is_xlsx, is_image
from utils.convertor import convert_ppt_to_pdf, convert_docx_to_pdf
from utils.directory import make_dir, check_dir, move_file


class FetchMail: 
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
    
    def run(self):
        messages = self.search_message('Nepal Engineering College')
        for msg in messages:
            self.display_message(msg)
    

class CheckMail: 
    def __init__(self, root_dir=os.getcwd()):
        self.root_dir = root_dir

    def convert_to_pdf(self, file_path, folder_path):
        """This will convert the ppt and docx to pdf"""
        file = file_path.split('/')[-1]
        if is_ppt(file_path):
            pdf_file = f'{folder_path}/{file.split(".")[0]}.pdf'
            convert_ppt_to_pdf(file_path, pdf_file)
        if is_docx(file_path):
            pdf_file = f'{folder_path}/{file.split(".")[0]}.pdf'
            convert_docx_to_pdf(file_path, pdf_file)

    def save_path_in_json(self, file_path, save_in_folder, name):
        """This will save the path of the file in json file. With respect to the folder name"""
        if os.path.exists(os.path.join(save_in_folder, f'{name}.json')):
            # Read the json file. With the help of json.load. File name
            with open(os.path.join(save_in_folder, f'{name}.json'), 'r') as f:
                try: 
                    file = json.load(f)
                except Exception as e:
                    print(f"Error: {e}.")
            with open(os.path.join(save_in_folder, f'{name}.json'), 'w') as f:
                pdf_file_path_array = file['paths']
                pdf_file_path_array.append(file_path) if file_path not in pdf_file_path_array else None
                json.dump({'paths': pdf_file_path_array}, f)
        else:
            print(save_in_folder)
            with open(os.path.join(save_in_folder, f'{name}.json'), 'w') as f:
                json.dump({'paths': [file_path]}, f)

    def save_file(self, source_file, destination_folder_name, root_folder_name='data'):
        root_folder= os.path.join(self.root_dir, root_folder_name)

        # Inserted files between destination_folder and root_folder
        destination_folder = f'{root_folder}/files/{destination_folder_name}'

        # Creates all the folder in the path
        make_dir(destination_folder)

        new_file_path = os.path.join(destination_folder, source_file.split('/')[-1])

        # Create a path to create a directory
        save_json_file_path = f'{root_folder}/paths'

        # Create a directory for json file
        make_dir(save_json_file_path)

        # Save the path in json file
        self.save_path_in_json(new_file_path, save_json_file_path, destination_folder_name)

        # Move the file to the destination folder
        move_file(source_file, destination_folder)

    def check_pdf(self, file_path, file):
        """This will check if the file is pdf or not and save in a file with path name. If not then it will remove it."""

        if is_pdf(file_path):
            self.save_file(file_path, 'PDF')
        elif is_docx(file_path):
            self.save_file(file_path, 'DOCX')
        elif is_ppt(file_path):
            self.save_file(file_path, 'PPT')
        elif is_xlsx(file_path):
            self.save_file(file_path, 'XLSX')
        elif is_image(file_path):
            self.save_file(file_path, 'IMG')
        else:
            try:
                os.remove(file_path)
                print(f'{file} is not a PDF. So Removed it.')
            except OSError as e:
                print(f"Error: {e.file} - {e.strerror}.")

    def remove_empty_dir(self, dir):
        """This will check if the directory is empty or not. If empty then it will remove it."""
        try:
            if(os.listdir(dir) == []):
                os.rmdir(dir)
        except Exception as e:
            print(f"Error: {e}.")

    def navigate_folder(self, dir):
        """This will navigate through the folder and check if the file is pdf or not. If not then it will convert it to pdf. Else it will remove it."""
        for folders in os.listdir(dir):
            folder_path = os.path.join(dir, folders)
            print('\n')
            print(f'Checking folder: {folder_path}')
            try: 
                for file in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, file)
                    # self.convert_to_pdf(file_path, folder_path)
                    self.check_pdf(file_path, file)

            except NotADirectoryError as e:
                print(f"Error: {e}.")
            self.remove_empty_dir(folder_path)

    def run(self, dir='Mails'):
        check_dir(dir)
        self.navigate_folder(dir)
        

if __name__ == "__main__":
    choice = input("Do you want to fetch the mail? (y/n): ")
    if(choice == 'y'):
        FetchMail().run()
    else:
        CheckMail().run()
