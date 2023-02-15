from __future__ import print_function

from utils.search_message import search_messages
from utils.read_message import read_message
from utils.delete_message import delete_messages_with_query, delete_message_with_id
from authenticate.get_authenticate import get_authenticate


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
    

if __name__ == "__main__":
    Main().main()
