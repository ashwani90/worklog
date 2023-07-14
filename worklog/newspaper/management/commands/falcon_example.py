from newspaper.models import News
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
from django.core.management.base import BaseCommand, CommandError
# from langchain import PromptTemplate, HuggingFaceHub, LLMChain
from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch
from langchain import HuggingFacePipeline
from langchain import PromptTemplate,  LLMChain




os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'

model_name = "tiiuae/falcon-7b-instruct"
# torch_dtype=torch.float32
model=AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True, torch_dtype=torch.bfloat16, device_map='auto',offload_folder='./')



class Command(BaseCommand):
    help = "Get answers to questions"

    # def add_arguments(self, parser):
    #     /parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True, torch_dtype=torch.bfloat16, device_map='auto', offload_folder="./")
        pipeline = transformers.pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            torch_dtype=torch.bfloat16,
            trust_remote_code=True,
            device_map="auto",
            max_length=200,
            do_sample=True,
            top_k=10,
            num_return_sequences=1,
            eos_token_id=tokenizer.eos_token_id
        )
        llm = HuggingFacePipeline(pipeline = pipeline, model_kwargs = {'temperature':0})
        template = """
        You are a intelligent chatbot. You reply should be in a funny way.
        Question: {query}
        Answer:"""
        prompt = PromptTemplate(template=template, input_variables=["query"])


        llm_chain = LLMChain(prompt=prompt, llm=llm)
        query = "How to reach the moon?"

        print(llm_chain.run(query))
        
        
        # sequences = pipeline(
        # "Create a list of 3 important things to reduce global warming"
        # )

        # print(sequences)
        # for seq in sequences:
        #     print(f"Result: {seq['generated_text']}")
