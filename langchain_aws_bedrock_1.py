#Imports
import boto3
from langchain_aws import BedrockLLM

#Create the bedrock client
boto3_client = boto3.client('bedrock-runtime')

#setting model inference parameters
inference_modifier = {
  "temperature" : 0.5,
  "top_p" : 1,
  "max_tokens_to_sample" : 1000
}

#Create the llm
llm = BedrockLLM(
  model_id="anthropic.claude-instant-v1",
  client = boto3_client,
  model_kwargs= inference_modifier
)

#Generate the response
response = llm.invoke ("""
  Human: Escreva um brinde de casamento para os noivos José e Maria,
  parabenizando pelo casamento e contendo alguns conselhos para recém-casados do padrinho Cláudio.
                       
  Answer:""")


#Display the result
print (response)