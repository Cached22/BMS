from cryptography.fernet import Fernet

# This is a utility class for handling encryption and decryption operations
class EncryptionManager:
    def __init__(self, key=None):
        self.key = key or self.generate_key()
        self.fernet = Fernet(self.key)

    @staticmethod
    def generate_key():
        """
        Generates a new key for encryption.
        """
        return Fernet.generate_key()

    def encrypt_data(self, data):
        """
        Encrypts the provided data using the Fernet key.
        :param data: Data to be encrypted (bytes).
        :return: Encrypted data (bytes).
        """
        return self.fernet.encrypt(data)

    def decrypt_data(self, encrypted_data):
        """
        Decrypts the provided data using the Fernet key.
        :param encrypted_data: Data to be decrypted (bytes).
        :return: Decrypted data (bytes).
        """
        return self.fernet.decrypt(encrypted_data)

    def save_key_to_file(self, file_path):
        """
        Saves the encryption key to a file.
        :param file_path: Path to the file where the key will be saved.
        """
        with open(file_path, 'wb') as key_file:
            key_file.write(self.key)

    def load_key_from_file(self, file_path):
        """
        Loads the encryption key from a file.
        :param file_path: Path to the file from which the key will be loaded.
        """
        with open(file_path, 'rb') as key_file:
            self.key = key_file.read()
            self.fernet = Fernet(self.key)

# Example usage:
# encryption_manager = EncryptionManager()
# encrypted_data = encryption_manager.encrypt_data(b'Some sensitive data')
# decrypted_data = encryption_manager.decrypt_data(encrypted_data)
# encryption_manager.save_key_to_file('path_to_key_file')
# encryption_manager.load_key_from_file('path_to_key_file')