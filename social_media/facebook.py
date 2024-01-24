import requests
from datetime import datetime
from shared_dependencies import apiKeys, systemSettings, User, Post, schedulePost, fetchSocialMediaData

class FacebookManager:
    BASE_URL = "https://graph.facebook.com/v12.0"
    
    def __init__(self, user: User):
        self.user = user
        self.access_token = apiKeys['facebook']
    
    def create_post(self, message: str, scheduled_time: datetime = None):
        post_data = {
            'message': message,
            'access_token': self.access_token
        }
        if scheduled_time:
            post_data['scheduled_publish_time'] = int(scheduled_time.timestamp())
            post_data['published'] = False
        
        response = requests.post(f"{self.BASE_URL}/{self.user.facebook_page_id}/feed", data=post_data)
        return response.json()
    
    def get_page_insights(self):
        params = {
            'access_token': self.access_token,
            'metric': 'page_impressions,page_engagement',
            'period': 'day'
        }
        response = requests.get(f"{self.BASE_URL}/{self.user.facebook_page_id}/insights", params=params)
        return response.json()
    
    def schedule_post(self, post: Post):
        scheduled_time = datetime.strptime(post.scheduled_time, '%Y-%m-%dT%H:%M:%S')
        return self.create_post(post.content, scheduled_time)
    
    def fetch_posts(self):
        params = {
            'access_token': self.access_token
        }
        response = requests.get(f"{self.BASE_URL}/{self.user.facebook_page_id}/posts", params=params)
        return response.json()

# Example usage
if __name__ == "__main__":
    user = User(facebook_page_id='your_page_id')
    fb_manager = FacebookManager(user)
    
    # Schedule a post
    post = Post(content="This is a scheduled post for Facebook.", scheduled_time="2023-04-15T10:00:00")
    schedule_response = fb_manager.schedule_post(post)
    print(schedule_response)
    
    # Fetch insights
    insights = fb_manager.get_page_insights()
    print(insights)
    
    # Fetch posts
    posts = fb_manager.fetch_posts()
    print(posts)