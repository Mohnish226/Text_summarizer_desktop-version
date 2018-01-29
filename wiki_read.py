# -*- coding: utf-8 -*-
import wikipedia

#print(wikipedia.summary("Automatic Summarization"))
data = wikipedia.page("Barack")
print(data.title)
print(data.content)
print(data.url)