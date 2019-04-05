from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.preprocessing import normalize
import pandas as pd

corpus = {1: "The game of life is a game of everlasting learning", 2: "The unexamined life is not worth living", 3: "Never stop learning"}

cvect = CountVectorizer(ngram_range=(1,1), token_pattern='(?u)\\b\\w+\\b')
counts = cvect.fit_transform(corpus.values())
normalized_counts = normalize(counts, norm='l1', axis=1)

tfidf = TfidfVectorizer(ngram_range=(1,1), token_pattern='(?u)\\b\\w+\\b', smooth_idf=False)
tfs = tfidf.fit_transform(corpus.values())
new_tfs = normalized_counts.multiply(tfidf.idf_)

feature_names = tfidf.get_feature_names()
corpus_index = [n for n in corpus]
df = pd.DataFrame(new_tfs.T.todense(), index=feature_names, columns=corpus_index)

print(df.loc[['life', 'learning']])