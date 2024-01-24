```python
import openai
from shared_dependencies import sendMessage, userPreferences, systemSettings

class ChatAssistant:
    def __init__(self, api_key):
        self.api_key = api_key
        self.openai_api = openai.ChatCompletion.create(api_key=api_key)

    def generate_response(self, message):
        try:
            response = self.openai_api.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": message},
                ]
            )
            return response.choices[0].message['content'].strip()
        except Exception as e:
            print(f"Error generating response: {e}")
            return "I'm sorry, I couldn't process your request."

    def handle_task(self, task):
        if task['type'] == 'schedulePost':
            return sendMessage(task['details'])
        elif task['type'] == 'trackEmail':
            return sendMessage(task['details'])
        elif task['type'] == 'scheduleContent':
            return sendMessage(task['details'])
        elif task['type'] == 'createDesign':
            return sendMessage(task['details'])
        else:
            return "Task type not recognized."

    def assist_user(self, user_input):
        response = self.generate_response(user_input)
        return response

if __name__ == "__main__":
    chat_assistant = ChatAssistant(api_key=systemSettings['openai_api_key'])
    while True:
        user_input = input("How can I assist you today? ")
        if user_input.lower() == 'exit':
            break
        response = chat_assistant.assist_user(user_input)
        print(response)
```