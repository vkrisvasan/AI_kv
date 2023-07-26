import os
import openai
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# To get a specific section
section = config['DEFAULT']

# To get a specific value
OPENAI_API_KEY = section.get('OPENAI_KEY')
openai.api_key = OPENAI_API_KEY

kvprompt="Write a java code that deomstrates SOLID design principles"

tag_line = openai.Completion.create(
  model="text-davinci-003",
  prompt=kvprompt,
  max_tokens=1000,
  temperature=1,
  n=1
)

for choice in tag_line['choices']:
    print(choice['text'])
    print("=================================")
