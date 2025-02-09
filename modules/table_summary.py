from huggingface_hub import login
login('HuggingFaceToken')
import re
import torch
from transformers import BitsAndBytesConfig
from langchain import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# regexp = re.compile("(?<=</table> ' \[/INST\] </s>)(?s)(.*$)")
regexp = re.compile("(?<=\[/INST] </s>)(?s)(.*$)") 

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
)

model_4bit = AutoModelForCausalLM.from_pretrained( "mistralai/Mistral-7B-Instruct-v0.1", device_map="auto",quantization_config=quantization_config, )
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")

pipeline_inst = pipeline(
        "text-generation",
        model=model_4bit,
        tokenizer=tokenizer,
        use_cache=True,
        device_map="auto",
        max_length=2500,
        do_sample=True,
        top_k=5,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
        pad_token_id=tokenizer.eos_token_id,
)

llm = HuggingFacePipeline(pipeline=pipeline_inst)

template = """<s>[INST]
You are Inclusive Insight, an empathetic and detail-oriented assistant committed to making data accessible for visually impaired users. You excel at summarizing complex tables and charts into clear, concise, and meaningful information.

Your passion for inclusivity drives you to break down intricate data and technical jargon into simple explanations, ensuring everyone can understand key points and trends. With patience and attentiveness, you empower users by providing vivid descriptions and highlighting significant details.

Your goal is to create an inclusive environment where everyone has equal access to knowledge.

Summarize the table below for a visually impaired user:
{question} [/INST] </s>
"""

def generate_summary(question):
  prompt = PromptTemplate(template=template, input_variables=["question"])
  llm_chain = LLMChain(prompt=prompt, llm=llm)
  response = llm_chain.run({"question":question})
  summary = regexp.search(response).group(1)

  return summary

def html_table_summary(list_of_htmltable):
    """generates list of table summary including the table so that we can display both the table and the summary in the UI

    Args:
        list_of_htmltable (list): list of html tables extracted from pdf/url web scraping

    Returns:
        _type_: list of table summary with tables
    """
    tableSummaryList = []
    
    for html_table in list_of_htmltable:
        question_prompt = "Write a summary for the following table : ' "+ str(html_table)+ " '"
        prompt = PromptTemplate(template=template, input_variables=["question"])
        llm_chain = LLMChain(prompt=prompt, llm=llm)

        try:
            response = llm_chain.run({"question":question_prompt})
            # print("===>",response)
        except Exception as e:
            response = str(e)
        
        # summary = response
        try:
            summary = regexp.search(response).group(1)
        except:
            summary = "======== ERROR======="
        
        html_text = "Summary for Table:" + str(html_table) + "<br>" # to show in UI
        html_text = html_text+ "Summary: "+ summary + "<br><br>"
        tableSummaryList.append(html_text)
    return tableSummaryList

    