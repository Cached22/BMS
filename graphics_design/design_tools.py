import requests
from PIL import Image
from io import BytesIO
from api_integration.design_api import fetchDesignData, uploadToCloud

# Define the API key for DALL-E from the shared dependencies
from shared_dependencies import apiKeys

# Define the Design schema from the shared dependencies
from shared_dependencies import Design

class DesignTools:
    def __init__(self):
        self.dalle_api_key = apiKeys['DALL-E']
        self.dalle_url = "https://api.openai.com/v1/images/generations"

    def generate_ai_design(self, prompt, num_images=1):
        headers = {
            'Authorization': f'Bearer {self.dalle_api_key}',
            'Content-Type': 'application/json'
        }
        payload = {
            'prompt': prompt,
            'n': num_images
        }
        response = requests.post(self.dalle_url, headers=headers, json=payload)
        if response.status_code == 200:
            designs = []
            for data in response.json()['data']:
                image_data = data['image']
                image = Image.open(BytesIO(base64.b64decode(image_data)))
                designs.append(image)
            return designs
        else:
            raise Exception(f"Error generating design: {response.text}")

    def save_design(self, design, filename):
        design_path = f'graphics_design/saved_designs/{filename}'
        design.save(design_path)
        uploadToCloud(design_path)
        return design_path

    def create_template_design(self, template_id, customization_data):
        # Fetch the template data using the shared function
        template_data = fetchDesignData(template_id)
        # Customize the template based on the provided data
        # This is a placeholder for the actual template customization logic
        customized_design = template_data.customize(customization_data)
        return customized_design

# Example usage:
# design_tools = DesignTools()
# ai_designs = design_tools.generate_ai_design("A futuristic cityscape", num_images=3)
# for idx, design in enumerate(ai_designs):
#     design_tools.save_design(design, f"cityscape_{idx}.png")