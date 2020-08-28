# import nltk
# nltk.download()

import nltk.book

# Frequency
dist=nltk.book.FreqDist(nltk.book.text7)
dist.keys()


# Stemmer
k='List listed lists listing listings'
k=k.lower().split(' ')
porter=nltk.PorterStemmer()
[porter.stem(t) for t in k]


udhr=nltk.corpus.udhr.words('English-Latin1')
porter=nltk.PorterStemmer()
[porter.stem(t) for t in udhr[0:10]]




# Lemmatization
udhr=nltk.corpus.udhr.words('English-Latin1')
wnl=nltk.WordNetLemmatizer()
[wnl.lemmatize(t) for t in udhr[0:10]]


# Tokenization
k="Children shouldn't drink a sugary drink before bad."
nltk.word_tokenize(k)



# Sentence Splitting
k="This is the first sentence. A gallon of milk in the U.S. costs $2.99. Is this the third sentence? Yes, it is!"
nltk.sent_tokenize(k)



# Part-of-Speech Tagging
k="Children shouldn't drink a sugary drink before bad."
k=nltk.word_tokenize(k)
nltk.pos_tag(k)
nltk.help.upenn_tagset('NNP')




