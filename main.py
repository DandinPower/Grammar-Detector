import gradio as gr
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
    return res.choices[0].message.content

def check_grammar(sentence):
    # Do something with the input sentence
    # For example, you can check the grammar using a language model
    # and return the corrected sentence
    corrected_sentence = CheckGrammar(sentence)
    return corrected_sentence

input_text = gr.inputs.Textbox(label="Input Sentence")
output_text = gr.outputs.Textbox(label="Corrected Sentence")

gr.Interface(fn=check_grammar, inputs=input_text, outputs=output_text).launch()