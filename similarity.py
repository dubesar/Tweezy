import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re, math
from collections import Counter
import urllib, sys, bs4
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

def cosine_sim(str1,str2):
    text1 = 'This is a foo bar sentence .'
    text2 = 'This sentence is similar to a foo bar sentence .'

    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)

    cosine = get_cosine(vector1, vector2)

    if(cosine>0.75):
        return 1
    return 0


def rank_similarity(dataset):
    counter=0
    total=0
    for i in range(0,len(dataset)):
        total=total+1
        for j in range(i-3,i+3):
            if(j>0 and j<len(dataset)):
                for k in range(i-3,i+3):
                    if(j!=k and k>0 and k<len(dataset)):
                        counter=counter+cosine_sim(dataset[j],dataset[k])
    similarity_rank=(float(counter)/total)*10
    return similarity_rank
