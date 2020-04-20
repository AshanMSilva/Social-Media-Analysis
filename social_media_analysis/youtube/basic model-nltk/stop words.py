from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "This is an example showing nltk features."
stop_words = set(stopwords.words("english"))

words = word_tokenize(text)

filteredsentence = [w for w in words if w not in stop_words]

print(filteredsentence)


