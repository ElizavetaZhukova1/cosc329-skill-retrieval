from functools import reduce
import pandas as pd
import numpy as np
from scipy.sparse import data 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
import csv 
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

dataset = pd.read_csv('all_skills_4k.csv')
dataset = dataset["new_skills"]

count = CountVectorizer()
tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)

words = [eval(line) for line in dataset]
words = reduce(lambda x, y: x+y, words)
word_count = count.fit_transform(words)
tfidf_transformer.fit(word_count)
df_idf = pd.DataFrame(tfidf_transformer.idf_, index=count.get_feature_names(),columns=["idf_weights"])
df_idf.sort_values(by=['idf_weights'])

pd.set_option("display.max_rows", len(df_idf))
#print(df_idf)
pd.reset_option("display.max_rows")

wcss = []
for i in range(1,8):
    kmeans = KMeans(i)
    kmeans.fit(df_idf)
    wcss_iter = kmeans.inertia_
    wcss.append(wcss_iter)

numClusters = range(1,8)
plt.plot(numClusters, wcss)
plt.title('Elbow Method Graph')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()


'''
#tfidf 
tf_idf_vector = tfidf_transformer.transform(df_idf)
feature_names = count.get_feature_names()

first_document_vector = tf_idf_vector[1]
df_tfifd = pd.DataFrame(first_document_vector.T.todense(), index=feature_names, columns=["tfidf"])
df_tfifd.sort_values(by=["tfidf"], ascending=False)

print(df_tfifd)
'''
#print(df_idf.head())


#print(word_count)
# tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
# tfidf_transformer.fit(word_count)
# df_idf = pd.DataFrame(tfidf_transformer.idf_, index=count.get_feature_names(),columns=["idf_weights"])
# df_idf.sort_values(by=['idf_weights'])
# print(df_idf)



# l = eval(dataset[1181])
# print(l)
# print(type(l))
# word_count = count.fit_transform(l)
# print(count.get_feature_names())
#words = [eval(line) for line in dataset]