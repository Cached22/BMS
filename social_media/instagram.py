import requests
from datetime import datetime
from .agent import deployAgentSwarm
from api_integration.social_media_api import fetchSocialMediaData, schedulePost
from security.encryption import encryptData
from security.authentication import authenticateUser

class InstagramManager:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.instagram.com/v1"
        self.session = requests.Session()
        self.session.headers.update({'Authorization': f'Bearer {self.api_key}'})

    def post_image(self, image_path, caption):
        url = f"{self.base_url}/media/upload"
        data = {
            'caption': caption,
            'image': open(image_path, 'rb')
        }
        response = self.session.post(url, files=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error posting to Instagram: {response.text}")

    def schedule_post(self, image_path, caption, post_time):
        if datetime.now() < post_time:
            deployAgentSwarm(schedulePost, args=(self.post_image, image_path, caption, post_time))
        else:
            print("Post time must be in the future.")

    def get_analytics(self, post_id):
        url = f"{self.base_url}/media/{post_id}/insights"
        response = self.session.get(url)
        if response.status_code == 200:
            return encryptData(response.json())
        else:
            raise Exception(f"Error fetching analytics: {response.text}")

    def track_engagement(self):
        url = f"{self.base_url}/users/self/media/recent"
        response = self.session.get(url)
        if response.status_code == 200:
            return fetchSocialMediaData(response.json())
        else:
            raise Exception(f"Error tracking engagement: {response.text}")

if __name__ == "__main__":
    authenticateUser()
    api_key = apiKeys['instagram']
    instagram_manager = InstagramManager(api_key)
    # Example usage:
    # instagram_manager.schedule_post('path/to/image.jpg', 'Your caption here', datetime(2023, 5, 17, 12, 0))
    # print(instagram_manager.get_analytics('post_id'))
    # print(instagram_manager.track_engagement())