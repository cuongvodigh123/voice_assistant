import wikipedia
from googlesearch import search

# Tìm kiếm thông tin về Python trên Wikipedia
# query = "Python"
# results = wikipedia.search(query)
# if results:
#     page = wikipedia.page(results[0])
#     print(page.summary)

# Tìm kiếm trên Google
query = "người việt nam"
for url in search(query):
    print(url)