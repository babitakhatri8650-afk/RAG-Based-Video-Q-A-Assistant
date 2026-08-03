import requests
import os
import json
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib
from openai import OpenAI
from config import api_key

client=OpenAI(api_key=api_key)


df=joblib.load('embeddings.joblib')
def create_embedding(text_list):
    r=requests.post("http://localhost:11434/api/embed",json={
    "model":"bge-m3",
    "input":text_list
    })

    # return r.json()
    
    embedding=r.json()["embeddings"]
    return embedding

def inference(prompt):
    r=requests.post("http://localhost:11434/api/generate",json={
        "model":"llama3.2:1b",
        "prompt":prompt,
        "stream":False
        })
    response=r.json()
    print(response)
    return response

def inference_openai(prompt):
    response=client.responses.create(
        model="gpt-5",
        input=prompt
    )
    return response

incoming_query=input("Ask a question ?")
question_embedding=create_embedding([incoming_query])[0]
# print(question_embedding)

#Find Similarities of question embedding with other 
similarities=cosine_similarity(np.vstack(df['embedding']),[question_embedding]).flatten()
# print(similarities)
top_results=5
max_index = similarities.argsort()[::-1][0:top_results]
# print(max_index)
new_df=df.loc[max_index]
# print(new_df)
# for  only title, number and text
# print(new_df[["file_name","number","text"]])

# for index,item in new_df.iterrows():
#     print(index,item["file_name"],item["number"],item["text"],item["start"],item["end"])


prompt=f'''I'm teaching web development using Sigma web development course.Here are video subtitle chunks containing title, video number,start time in seconds,end time in seconds,the text at that time:

{new_df[["file_name","number","start","end","text"]].to_json()}
------------------------------------------------------------------------------------------------------------------------
{incoming_query}
User asked this question related to video chunks,you have to answer in human way (don't mention the above format it's just for you.) where and how much content is taught where (in which video and at which timestamp) and guide the users to go to that particular video.If user asks unrelated question,tell him that you can only answer question related to the course.'''

with open("prompt.txt","w") as f:
    f.write(prompt)

# response=inference(prompt)

response=inference_openai(prompt)

with open("response.txt","w",encoding="utf-8") as f:
    f.write(response["response"])
