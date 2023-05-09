import wikipedia
wikipedia.set_lang("vi")
data=wikipedia.summary("người Việt Nam").split(".")
print(data[0])
data.pop(0)
print(data[0])
