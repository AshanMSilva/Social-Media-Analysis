import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC


documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)
random.shuffle(documents)
random.shuffle(documents)

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:5000]

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

##print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev), category) for (rev, category) in documents]

# set that we'll train our classifier with
##print(len(featuresets))
training_set = featuresets[:1600]

# set that we'll test against.
testing_set = featuresets[1600:]

#classifier = nltk.NaiveBayesClassifier.train(training_set)

classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

print("Original Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

##save_classifier = open("naivebayes.pickle","wb")
##pickle.dump(classifier, save_classifier)
##save_classifier.close()


#multinomial NB
MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MultinomialNB Classifier accuracy percent:",(nltk.classify.accuracy(MNB_classifier, testing_set))*100)


#Gaussian NB
#GaussianNB_classifier = SklearnClassifier(GaussianNB())
#GaussianNB_classifier.train(training_set)
#print("Gaussian NB Classifier accuracy percent:",(nltk.classify.accuracy(GaussianNB_classifier, testing_set))*100)


#Bernoulli NB
BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print("Bernoulli NB Classifier accuracy percent:",(nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)


#LogisticRegression
LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression Classifier accuracy percent:",(nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)


#SGDClassifier
SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print("SGDClassifier accuracy percent:",(nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)


###SVC
SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(training_set)
print("SVC Classifier accuracy percent:",(nltk.classify.accuracy(SVC_classifier, testing_set))*100)


#LinearSVC
LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC Classifier accuracy percent:",(nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)


#NuSVC
NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC Classifier accuracy percent:",(nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)

