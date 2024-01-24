```python
import boto3
from botocore.exceptions import NoCredentialsError

class CloudStorageService:
    def __init__(self, access_key, secret_key, bucket_name):
        self.s3_client = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
        self.bucket_name = bucket_name

    def upload_to_cloud(self, file_name, object_name=None):
        """Upload a file to an S3 bucket

        :param file_name: File to upload
        :param object_name: S3 object name. If not specified then file_name is used
        :return: True if file was uploaded, else False
        """
        if object_name is None:
            object_name = file_name

        try:
            self.s3_client.upload_file(file_name, self.bucket_name, object_name)
            print(f"{file_name} has been uploaded to {self.bucket_name}/{object_name}")
            return True
        except FileNotFoundError:
            print(f"The file {file_name} was not found")
            return False
        except NoCredentialsError:
            print("Credentials not available")
            return False

    def download_from_cloud(self, object_name, file_name=None):
        """Download a file from an S3 bucket

        :param object_name: S3 object name
        :param file_name: File to download to. If not specified then object_name is used
        :return: True if file was downloaded, else False
        """
        if file_name is None:
            file_name = object_name

        try:
            self.s3_client.download_file(self.bucket_name, object_name, file_name)
            print(f"{object_name} has been downloaded from {self.bucket_name} to {file_name}")
            return True
        except FileNotFoundError:
            print(f"The file {file_name} was not found")
            return False
        except NoCredentialsError:
            print("Credentials not available")
            return False

# Example usage:
# cloud_storage_service = CloudStorageService('ACCESS_KEY', 'SECRET_KEY', 'bucket-name')
# cloud_storage_service.upload_to_cloud('local_file.txt', 's3_file.txt')
# cloud_storage_service.download_from_cloud('s3_file.txt', 'local_file.txt')
```