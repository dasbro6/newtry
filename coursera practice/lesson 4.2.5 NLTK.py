# from nltk.corpus import stopwords
# stopwords = stopwords.words('english')
# print(stopwords)
import nltk
from nltk.corpus import brown
print(brown.words(categories = 'news'))
print(brown.words(fileids = 'ca16'))

# print(help(nltk.ConditionalFreqDist))
cfd = nltk.ConditionalFreqDist((genre, word)
           for genre in brown.categories()
           for word in brown.words(categories = genre))
genres = ['news', 'romance']
modals = ['can', 'could', 'may', 'might', 'must', 'will', 'would']
cfd.tabulate(conditions = genres, samples = modals)
cfd.plot(conditions = genres, samples = modals)