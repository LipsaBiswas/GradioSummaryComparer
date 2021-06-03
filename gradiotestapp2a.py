# -*- coding: utf-8 -*-
"""GradioTestApp2A.ipynb

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
# from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import pipeline

# from parrot import Parrot

# parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=False)

def GenerateModelTokenizer_summary(inp,pretrained_model_selected,max_word_count):
    summary_generated=""
    max_length =max_word_count
    pretrained_model_selected = pretrained_model_selected.lower()
    try:
      if pretrained_model_selected=="bert":
        bert_model=Summarizer()
        summary_generated = bert_model(inp)
      elif pretrained_model_selected=="google/pegasus-pubmed" or pretrained_model_selected=='google/pegasus-xsum' or pretrained_model_selected=="mayu0007/pegasus_large_covid"or pretrained_model_selected=="google/pegasus-wikihow" or pretrained_model_selected=="deep-learning-analytics/wikihow-t5-small":
        
        # model = AutoModelForSeq2SeqLM.from_pretrained(pretrained_model_selected)
        # tokenizer = AutoTokenizer.from_pretrained(pretrained_model_selected)
        # inputs = tokenizer.encode("summarize: " + inp, return_tensors="pt", max_length=1024, truncation=True)
        # outputs = model.generate(
        #   inputs, 
        #   max_length=max_length, 
        #   min_length=50, 
        #   length_penalty=2.0, 
        #   num_beams=4, 
        #   early_stopping=True)
        # summary_generated=tokenizer.decode(outputs[0])

        summarizer = pipeline("summarization", model=pretrained_model_selected) 
        summary=summarizer(inp)
        # summary=summarizer(inp ,min_length = int(0.3 * len(inp)), max_length =int(0.3 * len(inp)))
        summary_generated= summary[0]['summary_text']
        
      else:
        summary_generated=" No summary generated, please check with the admin"
    except Exception as e:
        summary_generated=" Error occured, please check with the admin:"+ str(e)
    # paraphrased_summary_generated = parrot.augment(input_phrase=summary_generated)
    paraphrased_summary_generated ="Not implemented, check with admin"
    return summary_generated,paraphrased_summary_generated

# pip install git+https://github.com/PrithivirajDamodaran/Parrot_Paraphraser.git

#Init models (make sure you init ONLY once if you integrate this to your code)
# parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=False)

# phrases = ["Can you recommed some upscale restaurants in Newyork?",
#            "What are the famous places we should not miss in Russia?"
# ]



def SummarizeText(inp, pretrained_model_selected, max_word_count):
  print(pretrained_model_selected)
  summary_generated,paraphrased_summary_generated=GenerateModelTokenizer_summary(inp,pretrained_model_selected,max_word_count)
  return summary_generated ,paraphrased_summary_generated



iface = gr.Interface(
  fn=SummarizeText, 
  inputs=[gr.inputs.Textbox(label="Abstract (*Enter paragraphs)",lines=20, placeholder="Enter abstract text here...") ,
          gr.inputs.Radio(["deep-learning-analytics/wikihow-t5-small","Bert", "google/pegasus-pubmed", "mayu0007/pegasus_large_covid","google/pegasus-wikihow","google/pegasus-xsum"]),
          gr.inputs.Slider(150, 200,label="Max word count")
        ],
    
  outputs=[
           gr.outputs.Textbox(label=" Summary"),gr.outputs.Textbox(label=" Paraphrased Summary")],title= "Auto summarization and Summary comparision(beta)"  )
iface.launch(debug=False)

a ='''
Severe Acute Respiratory Syndrome Coronavirus-2 (SARS-CoV-2), causing Coronavirus Disease 19 (COVID-19), emerged at the end of 2019 and quickly spread to cause a global pandemic with severe socio-economic consequences. The early sequencing of its RNA genome revealed its high similarity to SARS, likely to have originated from bats. The SARS-CoV-2 non-structural protein 10 (nsp10) displays high sequence similarity with its SARS homologue, which binds to and stimulates the 3'-to-5' exoribonuclease and the 2'-O-methlytransferase activities of nsps 14 and 16, respectively. Here, we report the biophysical characterization and 1.6 Å resolution structure of the unbound form of nsp10 from SARS-CoV-2 and compare it to the structures of its SARS homologue and the complex-bound form with nsp16 from SARS-CoV-2. The crystal structure and solution behaviour of nsp10 will not only form the basis for understanding the role of SARS-CoV-2 nsp10 as a central player of the viral RNA capping apparatus, but will also serve as a basis for the development of inhibitors of nsp10, interfering with crucial functions of the replication-transcription complex and virus replication
'''

# SummarizeText(a,"google/pegasus-pubmed")