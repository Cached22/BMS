import requests
from typing import Dict, List
from security.encryption import encryptData
from security.authentication import authenticateUser

# Import shared dependencies
from shared_dependencies import apiKeys, userPreferences, systemSettings

class EmailAPI:
    def __init__(self):
        self.base_url = "https://outlook.office.com/api/v2.0"
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {apiKeys["outlook"]}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })

    def send_email(self, recipient: str, subject: str, content: str, content_type: str = 'HTML') -> Dict:
        """
        Send an email using the Outlook API.

        :param recipient: The email address of the recipient.
        :param subject: The subject of the email.
        :param content: The content of the email.
        :param content_type: The type of the content ('HTML' or 'Text').
        :return: A dictionary with the response data.
        """
        # Ensure user is authenticated
        if not authenticateUser():
            raise PermissionError("User authentication failed.")

        # Encrypt email content
        encrypted_content = encryptData(content)

        # Construct the email message
        message = {
            'Message': {
                'Subject': subject,
                'Body': {
                    'ContentType': content_type,
                    'Content': encrypted_content
                },
                'ToRecipients': [
                    {
                        'EmailAddress': {
                            'Address': recipient
                        }
                    }
                ]
            },
            'SaveToSentItems': 'true'
        }

        # Send the email
        response = self.session.post(f'{self.base_url}/me/sendmail', json=message)
        return response.json()

    def track_email(self, email_id: str) -> Dict:
        """
        Track the status of an email using the Outlook API.

        :param email_id: The ID of the email to track.
        :return: A dictionary with the email status.
        """
        # Ensure user is authenticated
        if not authenticateUser():
            raise PermissionError("User authentication failed.")

        # Get the email status
        response = self.session.get(f'{self.base_url}/me/messages/{email_id}')
        return response.json()

    def get_inbox_emails(self, top: int = 10) -> List[Dict]:
        """
        Retrieve a list of emails from the user's inbox.

        :param top: The number of emails to retrieve.
        :return: A list of dictionaries with email data.
        """
        # Ensure user is authenticated
        if not authenticateUser():
            raise PermissionError("User authentication failed.")

        # Get the top emails from the inbox
        response = self.session.get(f'{self.base_url}/me/mailfolders/inbox/messages?$top={top}')
        return response.json().get('value', [])

# Example usage
if __name__ == "__main__":
    email_api = EmailAPI()
    # Send an email
    send_response = email_api.send_email(
        recipient="example@example.com",
        subject="Test Email",
        content="<h1>This is a test email</h1>"
    )
    print(send_response)

    # Track an email
    track_response = email_api.track_email(email_id="AQMkADAwATM0MD...")
    print(track_response)

    # Get inbox emails
    inbox_emails = email_api.get_inbox_emails(top=5)
    print(inbox_emails)