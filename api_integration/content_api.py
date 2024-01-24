import requests
from typing import List, Dict, Any

# Import shared dependencies
from shared_dependencies import apiKeys, userPreferences, systemSettings
from shared_dependencies import ContentItem, scheduleContent

# Base URL for content marketing platform API
CONTENT_API_BASE_URL = "https://content.marketing.api"

# Headers for API requests
HEADERS = {
    "Authorization": f"Bearer {apiKeys['contentMarketing']}",
    "Content-Type": "application/json"
}

def fetchContentData(content_type: str, user_id: int) -> List[ContentItem]:
    """
    Fetch content data from the content marketing platform API.
    
    :param content_type: The type of content to fetch (e.g., 'blog', 'social_media').
    :param user_id: The ID of the user whose content is to be fetched.
    :return: A list of ContentItem instances.
    """
    url = f"{CONTENT_API_BASE_URL}/{content_type}/user/{user_id}"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    content_data = response.json()
    return [ContentItem(**item) for item in content_data]

def createOrUpdateContent(content_item: Dict[str, Any]) -> ContentItem:
    """
    Create or update a content item in the content marketing platform.
    
    :param content_item: A dictionary with content item details.
    :return: An instance of ContentItem with the created or updated details.
    """
    url = f"{CONTENT_API_BASE_URL}/content"
    response = requests.post(url, headers=HEADERS, json=content_item)
    response.raise_for_status()
    return ContentItem(**response.json())

def deleteContent(content_id: int) -> None:
    """
    Delete a content item from the content marketing platform.
    
    :param content_id: The ID of the content item to delete.
    """
    url = f"{CONTENT_API_BASE_URL}/content/{content_id}"
    response = requests.delete(url, headers=HEADERS)
    response.raise_for_status()

def scheduleContentPublication(content_id: int, publish_date: str) -> None:
    """
    Schedule a content item for publication on the content marketing platform.
    
    :param content_id: The ID of the content item to schedule.
    :param publish_date: The date and time when the content should be published.
    """
    url = f"{CONTENT_API_BASE_URL}/content/{content_id}/schedule"
    data = {"publish_date": publish_date}
    response = requests.post(url, headers=HEADERS, json=data)
    response.raise_for_status()

# Example usage:
# content_items = fetchContentData('blog', user_id=123)
# new_content = createOrUpdateContent({'title': 'New Blog Post', 'body': 'Content of the blog post'})
# deleteContent(content_id=456)
# scheduleContentPublication(content_id=789, publish_date='2023-04-01T10:00:00Z')