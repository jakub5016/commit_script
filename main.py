import openai
OPENAI_API_KEY = None

# Get the api key
with open('OPENAI_API_KEY.txt', 'r') as file:
    data = file.readline().replace('\n', '')
    OPENAI_API_KEY = data[4:]