from newspaper.models import News
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
from transformers import pipeline
from django.core.management.base import BaseCommand, CommandError
from langchain import PromptTemplate, HuggingFaceHub, LLMChain

os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'

class Command(BaseCommand):
    help = "Get answers to questions"

    # def add_arguments(self, parser):
    #     /parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        template = """Question: {question}

        Answer: Let's think step by step."""
        prompt = PromptTemplate(template=template, input_variables=["question"])
        llm=HuggingFaceHub(repo_id="google/flan-t5-xl", model_kwargs={"temperature":1e-10})

        question = "When was Google founded?"

        print(llm.run(question))

# def run():
#     template = """Question: {question}

#     Answer: Let's think step by step."""
#     prompt = PromptTemplate(template=template, input_variables=["question"])
#     llm=HuggingFaceHub(repo_id="google/flan-t5-xl", model_kwargs={"temperature":1e-10})

#     question = "When was Google founded?"

#     print(llm_chain.run(question))
    # template = """
    #         The following is a conversation between a parent and a 
    #         child. The parent tends to give funny to child's questions:
    #         Child: {query}
    #         ParentL:
    #  """
    
    # unmasker = pipeline('fill-mask', model='roberta-base')

    # prompt = PromptTemplate(
    #     input_variables=["query"],
    #     template=template
    #  )

    # llm = models_higging face 
    # print(llm(prompt.format(query='Why is sky blue?')))
