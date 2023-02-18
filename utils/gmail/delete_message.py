from utils.gmail.search_message import search_messages

def delete_messages_with_query(service, query):
    messages_to_delete = search_messages(service, query)
    # it's possible to delete a single message with the delete API, like this:
    # service.users().messages().delete(userId='me', id=msg['id'])
    # but it's also possible to delete all the selected messages with one query, batchDelete
    return service.users().messages().batchDelete(
      userId='me',
      body={
          'ids': [ msg['id'] for msg in messages_to_delete]
      }
    ).execute()

def delete_message_with_id(service, message_id):
    return service.users().messages().delete(userId='me', id=message_id).execute()