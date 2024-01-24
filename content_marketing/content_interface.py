import datetime
from api_integration.content_api import fetchContentData, scheduleContent
from cloud_services.cloud_storage import uploadToCloud, downloadFromCloud
from agent_swarms.agent import deployAgentSwarm

class ContentMarketingInterface:
    def __init__(self, user_preferences):
        self.user_preferences = user_preferences
        self.content_items = downloadFromCloud('content_items') or []

    def add_content_item(self, content_item):
        self.content_items.append(content_item)
        uploadToCloud('content_items', self.content_items)

    def schedule_content(self, content_id, publish_date):
        content_item = next((item for item in self.content_items if item['id'] == content_id), None)
        if content_item:
            scheduleContent(content_item, publish_date)
            content_item['status'] = 'Scheduled'
            content_item['publish_date'] = publish_date
            uploadToCloud('content_items', self.content_items)
            return True
        return False

    def fetch_and_update_content_data(self):
        updated_content_data = fetchContentData()
        for content in updated_content_data:
            existing_content = next((item for item in self.content_items if item['id'] == content['id']), None)
            if existing_content:
                existing_content.update(content)
            else:
                self.content_items.append(content)
        uploadToCloud('content_items', self.content_items)

    def optimize_content_schedule(self):
        deployAgentSwarm(self.content_items, 'optimize_schedule')

    def get_scheduled_content(self, date=None):
        if date is None:
            date = datetime.datetime.now().date()
        return [item for item in self.content_items if item.get('publish_date') == date]

    def get_content_overview(self):
        return {
            'total': len(self.content_items),
            'scheduled': len([item for item in self.content_items if item.get('status') == 'Scheduled']),
            'published': len([item for item in self.content_items if item.get('status') == 'Published']),
            'drafts': len([item for item in self.content_items if item.get('status') == 'Draft']),
        }

# Example usage
if __name__ == "__main__":
    user_preferences = downloadFromCloud('user_preferences')
    content_interface = ContentMarketingInterface(user_preferences)
    
    # Add a new content item
    new_content_item = {
        'id': 'content123',
        'title': '5 Tips for Effective Content Marketing',
        'body': 'Content marketing is essential...',
        'status': 'Draft',
        'publish_date': None
    }
    content_interface.add_content_item(new_content_item)
    
    # Schedule a content item
    content_interface.schedule_content('content123', datetime.datetime(2023, 4, 15))
    
    # Fetch and update content data
    content_interface.fetch_and_update_content_data()
    
    # Get content scheduled for today
    todays_content = content_interface.get_scheduled_content()
    
    # Get an overview of all content
    content_overview = content_interface.get_content_overview()