```python
import requests
from shared_dependencies import apiKeys

class SocialMediaAPI:
    def __init__(self):
        self.platforms = {
            'instagram': 'https://api.instagram.com/',
            'youtube': 'https://www.googleapis.com/youtube/v3/',
            'facebook': 'https://graph.facebook.com/',
            'linkedin': 'https://api.linkedin.com/',
            'twitter': 'https://api.twitter.com/',
            'tiktok': 'https://open-api.tiktok.com/'
        }
        self.api_keys = apiKeys

    def get_headers(self, platform):
        return {
            'Authorization': f'Bearer {self.api_keys[platform]}',
            'Content-Type': 'application/json'
        }

    def fetch_social_media_data(self, platform, endpoint, params=None):
        if platform not in self.platforms:
            raise ValueError(f"Unsupported platform: {platform}")

        url = self.platforms[platform] + endpoint
        headers = self.get_headers(platform)
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def post_to_social_media(self, platform, endpoint, data):
        if platform not in self.platforms:
            raise ValueError(f"Unsupported platform: {platform}")

        url = self.platforms[platform] + endpoint
        headers = self.get_headers(platform)
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()

    def schedule_post(self, platform, data):
        if platform == 'instagram':
            endpoint = 'media_publish'
        elif platform == 'youtube':
            endpoint = 'videos'
        elif platform == 'facebook':
            endpoint = 'feed'
        elif platform == 'linkedin':
            endpoint = 'shares'
        elif platform == 'twitter':
            endpoint = 'statuses/update'
        elif platform == 'tiktok':
            endpoint = 'video/upload'
        else:
            raise ValueError(f"Unsupported platform for scheduling: {platform}")

        return self.post_to_social_media(platform, endpoint, data)

    def get_analytics(self, platform, post_id):
        if platform == 'instagram':
            endpoint = f'media/{post_id}/insights'
        elif platform == 'youtube':
            endpoint = f'videos?part=statistics&id={post_id}'
        elif platform == 'facebook':
            endpoint = f'{post_id}/insights'
        elif platform == 'linkedin':
            endpoint = f'organizationalEntityShareStatistics?q=organizationalEntity&shareId={post_id}'
        elif platform == 'twitter':
            endpoint = f'statuses/show/{post_id}'
        elif platform == 'tiktok':
            endpoint = f'video/data?video_id={post_id}'
        else:
            raise ValueError(f"Unsupported platform for analytics: {platform}")

        return self.fetch_social_media_data(platform, endpoint)

    def track_engagement(self, platform, post_id):
        if platform == 'instagram':
            endpoint = f'media/{post_id}/insights'
        elif platform == 'youtube':
            endpoint = f'videos?part=statistics&id={post_id}'
        elif platform == 'facebook':
            endpoint = f'{post_id}/insights'
        elif platform == 'linkedin':
            endpoint = f'organizationalEntityShareStatistics?q=organizationalEntity&shareId={post_id}'
        elif platform == 'twitter':
            endpoint = f'statuses/show/{post_id}'
        elif platform == 'tiktok':
            endpoint = f'video/data?video_id={post_id}'
        else:
            raise ValueError(f"Unsupported platform for engagement tracking: {platform}")

        return self.fetch_social_media_data(platform, endpoint)

# Example usage:
# api = SocialMediaAPI()
# instagram_data = api.fetch_social_media_data('instagram', 'users/self/media/recent')
# scheduled_post = api.schedule_post('facebook', {'message': 'Scheduled post via BMS'})
```