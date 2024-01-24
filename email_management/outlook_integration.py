import requests
from typing import List, Dict
from security.encryption import encryptData
from security.authentication import authenticateUser
from api_integration.email_api import sendEmail
from shared_dependencies import apiKeys, userPreferences, systemSettings, Email

class OutlookIntegration:
    def __init__(self):
        self.base_url = "https://outlook.office.com/api/v2.0"
        self.access_token = self.authenticate_outlook()

    def authenticate_outlook(self) -> str:
        # Placeholder for authentication process
        # In a real-world scenario, this would involve OAuth2.0 flow
        return authenticateUser(apiKeys['outlook'])

    def get_headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def get_inbox_emails(self) -> List[Email]:
        response = requests.get(
            f"{self.base_url}/me/mailfolders/inbox/messages",
            headers=self.get_headers()
        )
        response.raise_for_status()
        emails = response.json().get('value', [])
        return [self.map_to_email_schema(email) for email in emails]

    def map_to_email_schema(self, email_data: Dict) -> Email:
        return Email(
            id=email_data.get('Id'),
            subject=email_data.get('Subject'),
            sender=email_data.get('From').get('EmailAddress').get('Address'),
            received_time=email_data.get('ReceivedDateTime'),
            body_preview=email_data.get('BodyPreview'),
            is_read=email_data.get('IsRead')
        )

    def send_email(self, email: Email):
        email_data = {
            "Message": {
                "Subject": email.subject,
                "Body": {
                    "ContentType": "Text",
                    "Content": email.body
                },
                "ToRecipients": [
                    {
                        "EmailAddress": {
                            "Address": email.receiver
                        }
                    }
                ]
            },
            "SaveToSentItems": "true"
        }
        response = requests.post(
            f"{self.base_url}/me/sendmail",
            headers=self.get_headers(),
            json=email_data
        )
        response.raise_for_status()
        return response.json()

    def track_email(self, email_id: str) -> Email:
        response = requests.get(
            f"{self.base_url}/me/messages/{email_id}",
            headers=self.get_headers()
        )
        response.raise_for_status()
        email_data = response.json()
        return self.map_to_email_schema(email_data)

    def set_email_reminder(self, email_id: str, reminder_time: str):
        # This is a placeholder for setting a reminder for an email
        # The actual implementation would depend on the Outlook API capabilities and business logic
        pass

    def prioritize_email(self, email_id: str, priority_level: str):
        # This is a placeholder for prioritizing an email
        # The actual implementation would depend on the Outlook API capabilities and business logic
        pass

# Example usage
if __name__ == "__main__":
    outlook_integration = OutlookIntegration()
    inbox_emails = outlook_integration.get_inbox_emails()
    for email in inbox_emails:
        print(email.subject, email.sender, email.received_time)