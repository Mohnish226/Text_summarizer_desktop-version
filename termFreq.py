#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 23:59:33 2018

@author: Mohnish_Devadiga
"""

import nltk, math

dataset = {
    "tfidf-1": open("/Users/Mohnish_Devadiga/Desktop/Data/data/tfidf-1.txt").read(),
    "tfidf-2": open("/Users/Mohnish_Devadiga/Desktop/Data/data/tfidf-2.txt").read(),
    "tfidf-3": open("/Users/Mohnish_Devadiga/Desktop/Data/data/tfidf-3.txt").read(),
    "tfidf-4": open("/Users/Mohnish_Devadiga/Desktop/Data/data/tfidf-4.txt").read(),
    "tfidf-5": open("/Users/Mohnish_Devadiga/Desktop/Data/data/tfidf-5.txt").read(),
    "tfidf-6": open("/Users/Mohnish_Devadiga/Desktop/Data/data/tfidf-6.txt").read(),
    "tfidf-7": open("/Users/Mohnish_Devadiga/Desktop/Data/data/tfidf-7.txt").read(),
    "tfidf-8": open("/Users/Mohnish_Devadiga/Desktop/Data/data/tfidf-8.txt").read(),
    "tfidf-9": open("/Users/Mohnish_Devadiga/Desktop/Data/data/tfidf-9.txt").read(),
    "tfidf-10": open("/Users/Mohnish_Devadiga/Desktop/Data/data/tfidf-10.txt").read(),
}

'''
for item in dataset.keys():
    print(item)
'''

def tf(dataset, file_name):  # Term Frequence
    text = dataset[file_name]
    tokens = nltk.word_tokenize(text)
    fd = nltk.FreqDist(tokens)
    return fd

# print(tf(dataset,"tfidf-1"))

def idf(dataset, term):
    count = [term in dataset[file_name] for file_name in dataset]
    inv_df = math.log(len(count) / sum(count))
    return inv_df

'''
print(idf(dataset,"world"))
print(idf(dataset,"PYTHON")) # Word not present
'''

def tfidf(dataset, file_name, n):
    term_score = {}
    file_fd = tf(dataset, file_name)
    for term in file_fd:
        if term.isalpha():
            idf_val = idf(dataset, term)
            tf_val = tf(dataset, file_name)[term]
            tfidf_val = tf_val * idf_val
            term_score[term] = round(tfidf_val, 2)
    return sorted(term_score.items(), key=lambda x: -x[1])[:n]

def run_tfidf():
    tfidf(dataset, "tfidf-1", 5)
    for file_name in dataset:
        print("{0}: \n {1} \n".format(file_name, tfidf(dataset, file_name, 10)))