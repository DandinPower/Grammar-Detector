import openai
from dotenv import load_dotenv
import os
load_dotenv()  # Load variables from .env file

OPENAI_KEY = os.getenv('OPENAI_KEY')
MODEL = os.getenv('MODEL')
openai.api_key = OPENAI_KEY

def CheckGrammar(sentence):
    systemPrompt = 'Please act as an English Grammar Expert, Please indicated my grammar error but do not rewrite my article. if i have no major grammar error please tell me.'
    res = openai.ChatCompletion.create(
    model=MODEL,
    messages=[
            {"role": "system", "content": systemPrompt},
            {"role": "user", "content": sentence}
    ])
    print(res.choices[0].message.content)    

if __name__ == "__main__":
    while True:
        sentence = input('Please Type Your Sentence : ')
        if sentence == '-1': break 
        CheckGrammar(sentence)