import pandas as pd
# import LEX
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import numpy as np
from numpy.linalg import norm
# from scipy import spatial
# from sklearn.metrics.pairwise import cosine_similarity
def what():
    print('cuh')
def getcosine(head,art):


    art_tokens = nltk.tokenize.word_tokenize(art)
    head_tokens = nltk.tokenize.word_tokenize(head)

    un_tokens = set(art_tokens).union(set(head_tokens))

    num_art_words = dict.fromkeys(un_tokens,0)
    for word in art_tokens:
    #     print(word)
        num_art_words[word] += 1
    num_head_words = dict.fromkeys(un_tokens,0)
    for word in head_tokens:
    #     print(word)
        num_head_words[word] += 1

    def computeTF(wordDict, bagOfWords):
        tfDict = {}
        bagOfWordsCount = len(bagOfWords)
        for word, count in wordDict.items():
            tfDict[word] = count / float(bagOfWordsCount)
        return tfDict

    def computeIDF(documents):
        import math
        N = len(documents)
        
        idfDict = dict.fromkeys(documents[0].keys(), 0)
        for document in documents:
            for word, val in document.items():
                if val > 0:
                    idfDict[word] += 1
        
        for word, val in idfDict.items():
            idfDict[word] = math.log(N / float(val))
        return idfDict

    def computeTFIDF(tfBagOfWords, idfs):
        tfidf = {}
        for word, val in tfBagOfWords.items():
            tfidf[word] = val * idfs[word]
        return tfidf

    tf_art = computeTF(num_art_words, art_tokens)
    tf_head = computeTF(num_head_words, head_tokens)

    idf = computeIDF([num_art_words,num_head_words])

    tfidf_art = computeTFIDF(tf_art, idf)
    tfidf_head = computeTFIDF(tf_head, idf)

    # cosine similarity

    art_vect = np.array([*tfidf_head.values()])
    head_vect = np.array([*tfidf_art.values()])

    cosine = np.dot(head_vect,art_vect) / (norm(head_vect)*norm(art_vect))
    return cosine

def wordpsen(art):
    totalwords = len(nltk.word_tokenize(art))
    return totalwords/len(nltk.sent_tokenize(art))
def charpword(art):
    word_len = 0
    words = nltk.word_tokenize(art)
    for word in words:
        word_len+=len(word)
    return word_len/len(nltk.word_tokenize(art))