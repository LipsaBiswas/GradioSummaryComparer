# -*- coding: utf-8 -*-
"""GradioTestApp2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FOom2YjwthqfDcjWHIgQP2t8EUrOzPJ4
"""

# !pip install -q gradio
# !pip install -q transformers
# !pip install -q sentencepiece
# !pip install -q bert-extractive-summarizer

import gradio as gr
import transformers
import sentencepiece
from summarizer import Summarizer

def SummarizeText(inp, pretrained_model_selected):
  print(pretrained_model_selected)
  if pretrained_model_selected.lower()=="bert":
    bert_model=Summarizer()
    summary_generated = bert_model(inp)
  return summary_generated

iface = gr.Interface(
  fn=SummarizeText, 
  inputs=[gr.inputs.Textbox(label="Abstract (*Enter paragraphs)",lines=10, placeholder="Enter abstract text here...") ,
          gr.inputs.Radio(["Bert", "google/pegasus-pubmed", "mayu0007/pegasus_large_covid"]),
        ],
    
  outputs=[
           gr.outputs.Textbox(label=" Summary")],title= "Auto summarization and Summary comparision(beta)"  )
iface.launch(share=True)