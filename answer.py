import random
import json
import psutil

with open('data.json','r',encoding='utf-8') as f:
    data = json.load(f)

def answer(query,x):
    return random.sample(data[query]['cautraloi'], x)

def is_chrome_running():
    for process in psutil.process_iter():
        if 'chrome' in process.name():
            return True
    return False
def check_query(query):
    for i in data:
        if i in query:
            x=len(data[i]['cautraloi'])
            return random.sample(data[i]['cautraloi'], x)
    return None