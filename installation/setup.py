import os
import json
from getpass import getpass

def initialize_system():
    print("Welcome to the Business Management System (BMS) Setup Wizard!")
    system_settings = {
        'apiKeys': {},
        'userPreferences': {},
        'systemSettings': {}
    }

    # Prompt for API keys
    print("\nPlease enter the API keys for the social media platforms:")
    system_settings['apiKeys']['instagram'] = getpass("Instagram API Key: ")
    system_settings['apiKeys']['youtube'] = getpass("YouTube API Key: ")
    system_settings['apiKeys']['facebook'] = getpass("Facebook API Key: ")
    system_settings['apiKeys']['linkedin'] = getpass("LinkedIn API Key: ")
    system_settings['apiKeys']['twitter'] = getpass("Twitter API Key: ")
    system_settings['apiKeys']['tiktok'] = getpass("TikTok API Key: ")

    # Set up user preferences
    print("\nSetting up user preferences...")
    system_settings['userPreferences']['email_priority'] = input("Set default email priority (High, Medium, Low): ")
    system_settings['userPreferences']['content_schedule_view'] = input("Set default view for content schedule (Daily, Weekly, Monthly): ")

    # Set up global system settings
    print("\nConfiguring system settings...")
    system_settings['systemSettings']['cloud_storage_provider'] = input("Enter your preferred cloud storage provider: ")
    system_settings['systemSettings']['encryption_key'] = getpass("Enter a secure encryption key: ")

    # Save the configuration to a JSON file
    with open('system_config.json', 'w') as config_file:
        json.dump(system_settings, config_file, indent=4)

    print("\nSetup completed successfully! Your BMS is now configured.")

if __name__ == "__main__":
    initialize_system()