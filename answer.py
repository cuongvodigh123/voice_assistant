import random
import json

with open('data.json','r',encoding='utf-8') as f:
    data = json.load(f)

def answer(query):
    return random.choice(data[query]['cautraloi'])
