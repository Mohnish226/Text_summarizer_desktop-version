# -*- coding: utf-8 -*-
import wikipedia
import os



def topic(topic_name):
    try:
        data = wikipedia.page(topic_name)
        '''
        print(data.title)
        print(data.content)
        print(data.url)
        '''
        #output_file = filepath+"/output.txt"
        #f = open(output_file,'w')
        #print(data.content)
        if not data.content:
            print("Error! No Content found")
        else:
            #print(data.content)
            clean(data.content)
    except:
        print("Page Error!")
    return()
    
def link(url):
    url_topic = url.split("/")
    #print(url_topic[-1])
    topic_name = ""
    topic_name += url_topic[-1]
    #topic_name = [word.replace("/"," ") for word in url_topic[-1]]
    #print(topic_name.replace("_"," "))
    topic(topic_name.replace("_"," "))
    return

def clean(content):
    #print(content)
    temp_content = content.split("\n\n")
    #print(len(a))
    #print(a[1])
    for word in temp_content:
        word = word.strip()
        if "==" in word:
            word[0]==""
            word = word.replace("=","")
        #print(word)
        print(content.summary)

# Testing
#link("https://en.wikipedia.org/wiki/Battle_of_Plassey")

data = wikipedia.page("Battle of Plassey")
print(data.summary)