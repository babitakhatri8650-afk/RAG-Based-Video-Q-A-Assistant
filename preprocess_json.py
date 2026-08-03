import requests
import os
import json
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib
def create_embedding(text_list):
    r=requests.post("http://localhost:11434/api/embed",json={
    "model":"bge-m3",
    "input":text_list
    })

    # return r.json()
    embedding=r.json()["embeddings"]
    return embedding

jsons=os.listdir("json")  # list all the jsons
chunk_id=0

my_dicts=[]
for json_file in jsons:
    with open(f"json/{json_file}",encoding="utf-8") as f:
        content=json.load(f)

    # print(f"Creating Embeddings for {json_file}\n")

    embeddings=create_embedding([c['text'] for c in content['chunks']])
    # print(embeddings)

    for i,chunk in enumerate(content['chunks']):
        chunk['chunk_id']=chunk_id
        chunk['embedding']=embeddings[i]
        chunk_id+=1
        # chunk['embedding']=create_embedding(chunk['text_list'])
        my_dicts.append(chunk)
        
# print(my_dicts)
df=pd.DataFrame.from_records(my_dicts)
# print(df)
# Save Data Frame using Joblib
joblib.dump(df,'embeddings.joblib')

    