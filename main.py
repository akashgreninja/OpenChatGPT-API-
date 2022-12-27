from dotenv import load_dotenv
load_dotenv()
import openai
import os

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv('api_key')

response = openai.Completion.create(model="code-davinci-002", prompt="write a code sending a http request in py", temperature=0, max_tokens=4000)
print(response["choices"][0]["text"])


