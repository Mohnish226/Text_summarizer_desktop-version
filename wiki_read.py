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
        if not data.content:
            print("Error! No Content found")
        else:
            print(data.content)
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
