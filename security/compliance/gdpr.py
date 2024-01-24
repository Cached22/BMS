```python
import json
from datetime import datetime
from security.encryption import encryptData

class GDPRCompliance:
    def __init__(self, user_data):
        self.user_data = user_data

    def anonymize_data(self):
        """
        Anonymize user data to comply with GDPR.
        """
        anonymized_data = {}
        for key, value in self.user_data.items():
            if key not in ['name', 'email', 'address']:
                anonymized_data[key] = value
        return anonymized_data

    def delete_user_data(self, user_id):
        """
        Delete user data to comply with the right to be forgotten under GDPR.
        """
        # Assuming user_data is a dictionary with user_id as key
        if user_id in self.user_data:
            del self.user_data[user_id]
            return True
        return False

    def export_user_data(self, user_id):
        """
        Export user data in a machine-readable format to comply with GDPR.
        """
        if user_id in self.user_data:
            user_data = self.user_data[user_id]
            encrypted_data = encryptData(json.dumps(user_data))
            return encrypted_data
        return None

    def log_consent(self, user_id, consent):
        """
        Log user's consent for data processing activities.
        """
        timestamp = datetime.now().isoformat()
        consent_log = {
            'user_id': user_id,
            'consent': consent,
            'timestamp': timestamp
        }
        # Log the consent to a file or database
        self._log_to_file(consent_log)

    def _log_to_file(self, log_data):
        """
        Helper function to log data to a file.
        """
        with open('gdpr_consent_log.txt', 'a') as file:
            file.write(json.dumps(log_data) + '\n')

# Example usage:
# user_data = {
#     'user_id_123': {
#         'name': 'John Doe',
#         'email': 'john.doe@example.com',
#         'address': '123 Main St',
#         'preferences': {'theme': 'dark'}
#     }
# }
# gdpr = GDPRCompliance(user_data)
# gdpr.anonymize_data()
# gdpr.delete_user_data('user_id_123')
# encrypted_user_data = gdpr.export_user_data('user_id_123')
# gdpr.log_consent('user_id_123', consent=True)
```