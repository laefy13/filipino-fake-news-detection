
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
import nltk
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from nltk.corpus import stopwords
import collections
import liwc
from collections import Counter


#Read text dataset
df_train = pd.read_csv("training_data.csv")

#Cleaning 
df_train['text'].astype(str)
df_train['clean_text'] = df_train['text'].str.replace('http\S+|www.\S+', '', case=False) #Removing urls
df_train['clean_text'] = df_train['clean_text'].str.replace('[^A-Za-z0-9]+', ' ') #Removing Punctuations, Numbers, and Special Character 
df_train['clean_text'] = df_train['clean_text'].map(lambda x: x if type(x)!=str else x.lower()) #lowercase
df_train['clean_text'].dropna() #drop NaN values


#Tokenize and drop NaN tokens
split_data = df_train['clean_text'].str.split(" ")
df_train['tokens'] = split_data
nan_value = float("NaN")
df_train.replace("", nan_value, inplace=True)
df_train.dropna(subset = ["tokens"], inplace=True)


# Download "LIWC2015_English.dic" in your system and read as below
parse, category_names = liwc.load_token_parser('LIWC2015_English.dic')


#LIWC Features Extraction
liwc =[] 
for item in df_train.tokens:
    gettysburg_counts = list(collections.Counter(category for token in item for category in parse(token) if category == 'family (Family)').items())
    liwc.append(gettysburg_counts)
liwc_ = np.array(liwc)
df_train['family'] = liwc_

# likewise you can get features for other categories like "achieve (Achievement)","work (Work)", "certain (Certainty)" etc
# in the above for loop , change the "category" == "achieve (Achievement)" etc