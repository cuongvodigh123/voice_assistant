import wikipedia
wikipedia.set_lang("vi")
data=wikipedia.summary("Việt Nam").split(".")
print(data[0])
