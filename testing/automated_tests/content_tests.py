import unittest
from content_marketing.content_interface import scheduleContent, fetchContentData
from api_integration.content_api import ContentItem
from testing.feedback_loop import collectFeedback

class TestContentMarketingModule(unittest.TestCase):
    def setUp(self):
        # Setup can include initializing API keys, user preferences, etc.
        self.apiKeys = {'contentMarketingKey': 'your-api-key'}
        self.userPreferences = {'timezone': 'UTC', 'language': 'en'}
        self.testContentItem = ContentItem(
            title="Test Content",
            body="This is a test content body.",
            platform="Blog",
            schedule_time="2023-04-01T10:00:00Z"
        )

    def test_schedule_content(self):
        """Test scheduling of content across different platforms."""
        response = scheduleContent(self.testContentItem, self.apiKeys, self.userPreferences)
        self.assertTrue(response['success'], "Content scheduling failed.")

    def test_fetch_content_data(self):
        """Test fetching content data from the API."""
        content_data = fetchContentData(self.apiKeys)
        self.assertIsInstance(content_data, list, "Fetched content data is not a list.")
        self.assertGreater(len(content_data), 0, "No content data fetched.")

    def test_content_data_schema(self):
        """Test the schema of the content data."""
        content_data = fetchContentData(self.apiKeys)
        for content in content_data:
            self.assertIn('title', content, "Title is missing from content data.")
            self.assertIn('body', content, "Body is missing from content data.")
            self.assertIn('platform', content, "Platform is missing from content data.")
            self.assertIn('schedule_time', content, "Schedule time is missing from content data.")

    def test_feedback_loop(self):
        """Test the feedback loop for the content marketing module."""
        feedback = collectFeedback(module="content_marketing")
        self.assertIsNotNone(feedback, "Feedback should not be None.")
        self.assertIsInstance(feedback, dict, "Feedback should be a dictionary.")
        self.assertIn('comments', feedback, "Feedback does not contain comments.")

    # Additional tests can be added here to cover more scenarios

if __name__ == '__main__':
    unittest.main()