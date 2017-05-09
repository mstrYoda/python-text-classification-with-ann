# -*- coding:utf-8 -*-
import re

import numpy as np
import json

import tweepy
from tweepy import StreamListener

from zemberek import Stemmer

stemmer = Stemmer()


# probability threshold
ERROR_THRESHOLD = 0.01
# load our calculated synapse values

synapse_file = 'synapses.json'
with open(synapse_file) as data_file:
    synapse = json.load(data_file)

    synapse_0 = np.asarray(synapse['synapse0'])
    synapse_1 = np.asarray(synapse['synapse1'])
    words = synapse['words']
    classes = synapse['classes']

# compute sigmoid nonlinearity
def sigmoid(x):
    output = 1 / (1 + np.exp(-x))
    return output


# convert output of sigmoid function to its derivative
def sigmoid_output_to_derivative(output):
    return output * (1 - output)


def myStemmer(word):
    # kelime köklerini bulma işlemi yapılacak
    word = stemmer.stem(word)
    return word.lower()


def clean_up_sentence(sentence):
    sentence = sentence.strip()
    sentence_words = sentence.split(' ')

    words = [myStemmer(w) for w in sentence_words]
    stemmer.close()

    sentence_words = [w.replace('Ğ', 'g') for w in words]
    sentence_words = [w.replace('ğ', 'g') for w in words]
    sentence_words = [w.replace('Ç', 'c') for w in words]
    sentence_words = [w.replace('ç', 'c') for w in words]
    sentence_words = [w.replace('ü', 'u') for w in words]
    sentence_words = [w.replace('Ü', 'u') for w in words]
    sentence_words = [w.replace('Ü', 'u') for w in words]
    sentence_words = [w.replace('Ö', 'o') for w in words]
    sentence_words = [w.replace('ö', 'o') for w in words]
    sentence_words = [w.replace('İ', 'i') for w in words]
    sentence_words = [w.replace('I', 'i') for w in words]
    sentence_words = [w.replace('ı', 'i') for w in words]
    sentence_words = [w.replace('Ş', 's') for w in words]
    sentence_words = [w.replace('ş', 's') for w in words]

    sentence_words = [w.replace('\'', '') for w in words]
    sentence_words = [w.replace('"', '') for w in words]
    sentence_words = [w.replace('?', '') for w in words]
    sentence_words = [w.replace('!', '') for w in words]
    sentence_words = [w.replace('.', '') for w in words]
    sentence_words = [w.replace(',', '') for w in words]
    sentence_words = [w.replace(':', '') for w in words]
    sentence_words = [w.replace(';', '') for w in words]
    sentence_words = [w.replace('#', '') for w in words]
    sentence_words = [w.replace('-', ' ') for w in words]

    sentence_words = list(set(sentence_words))

    return sentence_words


# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return (np.array(bag))



def think(sentence, show_details=False):
    #verilen cümlenin bag of words vektörünü hesaplıyor
    x = bow(sentence, words, show_details)
    #cümleyi ve bow u ekranda gösteriyor
    if show_details:
        print ("sentence:", sentence, "\n bow:", x)

    # input layer is our bag of words
    #layer 0 bag of words vektörü
    l0 = x
    # matrix multiplication of input and hidden layer
    # ağırlıklarla layer 0 vektörünün çarpımı layer 1 in inputu oluyor
    l1 = sigmoid(np.dot(l0, synapse_0))
    # output layer
    # çıkış verisi layer1 ile ağırlık 1 in çarpımı
    l2 = sigmoid(np.dot(l1, synapse_1))

    return l2


def classify(sentence, show_details=False):
    #çıkış verisini alıyor
    results = think(sentence, show_details)
    #eşik değerinden yüksek olan çıkış verisi çiftlerini alıyor
    #örn [2,0.953531243] 2 = class number, 0.95 = olasılık
    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD ]

    #verileri sıralıyor
    results.sort(key=lambda x: x[1], reverse=True)

    return_results =[[classes[r[0]],r[1]] for r in results]

    print ("%s \n classification: %s" % (sentence, return_results))
    return return_results


classify("Cumhurbaşkanı Erdoğan, Hindistan Cumhurbaşkanlığı Sarayında ", True)