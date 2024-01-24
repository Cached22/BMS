import requests
from datetime import datetime
from shared_dependencies import apiKeys, systemSettings, User, Post, SocialMediaUpdate, schedulePost, fetchSocialMediaData

class YouTubeManager:
    BASE_URL = "https://www.googleapis.com/youtube/v3"
    
    def __init__(self, user: User):
        self.api_key = apiKeys['youtube']
        self.user = user

    def _make_api_call(self, endpoint, params):
        params['key'] = self.api_key
        response = requests.get(f"{self.BASE_URL}/{endpoint}", params=params)
        response.raise_for_status()
        return response.json()

    def get_channel_stats(self, channel_id):
        stats = self._make_api_call('channels', params={
            'part': 'statistics',
            'id': channel_id
        })
        return stats

    def schedule_video_post(self, video_details: Post):
        # This is a placeholder function as YouTube API does not support direct video uploads
        # Instead, this function should integrate with a service that uploads videos to YouTube
        # For example, using Google API client libraries
        schedule_time = video_details.schedule_time.isoformat() if video_details.schedule_time else datetime.now().isoformat()
        print(f"Scheduling video post for {schedule_time}")
        # Actual implementation would involve more complex interactions with YouTube's API
        schedulePost(video_details)

    def get_video_analytics(self, video_id):
        analytics = self._make_api_call('videos', params={
            'part': 'statistics',
            'id': video_id
        })
        return analytics

    def track_engagement(self, video_id):
        engagement_data = self._make_api_call('videos', params={
            'part': 'statistics,snippet',
            'id': video_id
        })
        return engagement_data

    def fetch_latest_videos(self, channel_id, max_results=5):
        videos = self._make_api_call('search', params={
            'channelId': channel_id,
            'part': 'snippet',
            'order': 'date',
            'maxResults': max_results
        })
        return videos

# Example usage:
# user = User(...)
# yt_manager = YouTubeManager(user)
# channel_stats = yt_manager.get_channel_stats('CHANNEL_ID')
# video_analytics = yt_manager.get_video_analytics('VIDEO_ID')
# yt_manager.schedule_video_post(Post(...))
# latest_videos = yt_manager.fetch_latest_videos('CHANNEL_ID')