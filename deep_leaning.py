import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import random
import json
import pickle
# //////////////////////////////////////
import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)
engine.runAndWait()
def speak_english(audio):
    print(audio,"\n")
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()
def take_english():
    query = input("user said: ")
    # r = sr.Recognizer()
    # with sr.Microphone() as source:
    #     print("..........LISTENING...........")
    #     r.pause_threshold = 1
    #     audio = r.listen(source)
    # try:
    #     print("..........Recognizing.........")
    #     query = r.recognize_google(audio, language='en')
    #     print(f"User said: {query}\n")
    # except Exception:
    #     query = "hãy nói lại"
    return query
    
# ?////////////////////////////////////////
with open("intents.json",encoding='utf-8') as file:
    data = json.load(file)

def load_data():
    print("lỗi 1")
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for i in data["intents"]:
        for pattern in i["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(i["tag"])

        if i["tag"] not in labels:
            labels.append(i["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output  = []

    out_empty = [0 for _ in range(len(labels))]

    for x,doc in enumerate(docs_x):
        bag = []
        
        wrds = [stemmer.stem(w) for w in doc]
        
        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)
        
        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1
        
        training.append(bag)
        output.append(output_row)
        
    training = numpy.array(training)
    output = numpy.array(output)

    with open("data.pickle","wb") as f:
        pickle.dump((words, labels, training, output), f)
try:
    with open("data.pickle","rb") as f:
        words, labels, training, output = pickle.load(f)
except: 
    print("lỗi 1")
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for i in data["intents"]:
        for pattern in i["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(i["tag"])

        if i["tag"] not in labels:
            labels.append(i["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output  = []

    out_empty = [0 for _ in range(len(labels))]

    for x,doc in enumerate(docs_x):
        bag = []
        
        wrds = [stemmer.stem(w) for w in doc]
        
        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)
        
        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1
        
        training.append(bag)
        output.append(output_row)
        
    training = numpy.array(training)
    output = numpy.array(output)

    with open("data.pickle","wb") as f:
        pickle.dump((words, labels, training, output), f)


net = tflearn.input_data(shape=[None, len(training[0] )])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)


try:
    model.load("model.tflearn")
except:
    # print("lỗi 2")
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("model.tflearn")

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)

def chat():
    print("Start talking with the bot (type quit to stop)!")
    while True:
        # inp = input("You: ")
        inp = take_english()
        while inp=="":
            inp = take_english()
        if inp.lower() == "go out":
            return "go out"
            break

        results = model.predict([bag_of_words(inp, words)])
        results_index = numpy.argmax(results)
        tag = labels[results_index]

        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']
        speak_english(random.choice(responses))
        return random.choice(responses)

# chat()