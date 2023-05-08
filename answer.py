import random
import json

with open('data.json','r',encoding='utf-8') as f:
    data = json.load(f)

def answer(query,x):
    return random.sample(data[query]['cautraloi'], x)
