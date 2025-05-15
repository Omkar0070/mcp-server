from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def send_email(command):
    # Load credentials from token.json (setup beforehand)
    creds = Credentials.from_authorized_user_file('token.json')
    service = build('gmail', 'v1', credentials=creds)
    message = {
        'raw': 'base64_encoded_email_body_here'  # construct email properly
    }
    send = service.users().messages().send(userId='me', body=message).execute()
    return "Email sent."
