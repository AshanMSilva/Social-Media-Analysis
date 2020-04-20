import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize


class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers
        

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    
    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf


short_positive = open("short_reviews/positive.txt","r").read()
short_negative = open("short_reviews/negative.txt","r").read()

documents =[]
all_words = []

#  j is adjectives, r is adverbs, and v is verbs
#allowed_word_types = ["J","R","V"]
allowed_word_types = ["J"]

for p in short_positive.split('\n'):
    documents.append( (p, "pos") )
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())

    
for p in short_negative.split('\n'):
    documents.append( (p, "neg") )
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())



save_documents = open("pickled_algos/documents.pickle","wb")
pickle.dump(documents, save_documents)
save_documents.close()


all_words = nltk.FreqDist(all_words)


word_features = list(all_words.keys())[:5000]


save_word_features = open("pickled_algos/word_features5k.pickle","wb")
pickle.dump(word_features, save_word_features)
save_word_features.close()

#for r in short_positive.split('\n'):
#    documents.append((r,"pos"))

#for r in short_negative.split('\n'):
#    documents.append((r,"neg"))


#short_positive_words = word_tokenize(short_positive)
#short_negative_words = word_tokenize(short_negative)

#for word in short_positive_words:
#    all_words.append(word.lower())

#for word in short_negative_words:
#    all_words.append(word.lower())


def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

##print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev), category) for (rev, category) in documents]

random.shuffle(featuresets)
random.shuffle(featuresets)
print(len(featuresets))

# set that we'll train our classifier with
##print(len(featuresets))
training_set = featuresets[:9000]

# set that we'll test against.
testing_set = featuresets[9000:]

save_featuresets = open("pickled_algos/featuresets.pickle", "wb")
pickle.dump(featuresets, save_featuresets)
save_featuresets.close()


classifier = nltk.NaiveBayesClassifier.train(training_set)

#classifier_f = open("naivebayes.pickle", "rb")
#classifier = pickle.load(classifier_f)
#classifier_f.close()

print("Original Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

##save_classifier = open("naivebayes.pickle","wb")
##pickle.dump(classifier, save_classifier)
##save_classifier.close()

save_classifier = open("pickled_algos/originalnaivebayes5k.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()


#multinomial NB
MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MultinomialNB Classifier accuracy percent:",(nltk.classify.accuracy(MNB_classifier, testing_set))*100)

save_classifier = open("pickled_algos/MNB_classifier5k.pickle","wb")
pickle.dump(MNB_classifier, save_classifier)
save_classifier.close()


#Gaussian NB
#GaussianNB_classifier = SklearnClassifier(GaussianNB())
#GaussianNB_classifier.train(training_set)
#print("Gaussian NB Classifier accuracy percent:",(nltk.classify.accuracy(GaussianNB_classifier, testing_set))*100)


#Bernoulli NB
BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print("Bernoulli NB Classifier accuracy percent:",(nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)

save_classifier = open("pickled_algos/BernoulliNB_classifier5k.pickle","wb")
pickle.dump(BernoulliNB_classifier, save_classifier)
save_classifier.close()


#LogisticRegression
LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression Classifier accuracy percent:",(nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

save_classifier = open("pickled_algos/LogisticRegression_classifier5k.pickle","wb")
pickle.dump(LogisticRegression_classifier, save_classifier)
save_classifier.close()


#SGDClassifier
SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print("SGDClassifier accuracy percent:",(nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)


#####SVC
##SVC_classifier = SklearnClassifier(SVC())
##SVC_classifier.train(training_set)
##print("SVC Classifier accuracy percent:",(nltk.classify.accuracy(SVC_classifier, testing_set))*100)
save_classifier = open("pickled_algos/SGDC_classifier5k.pickle","wb")
pickle.dump(SGDClassifier_classifier, save_classifier)
save_classifier.close()



#LinearSVC
LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC Classifier accuracy percent:",(nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

save_classifier = open("pickled_algos/LinearSVC_classifier5k.pickle","wb")
pickle.dump(LinearSVC_classifier, save_classifier)
save_classifier.close()


#NuSVC
NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC Classifier accuracy percent:",(nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)

##
##voted_classifier = VoteClassifier(classifier,
##                                  NuSVC_classifier,
##                                  LinearSVC_classifier,
##                                  SGDClassifier_classifier,
##                                  MNB_classifier,
##                                  BernoulliNB_classifier,
##                                  LogisticRegression_classifier)
##
##print("voted_classifier accuracy percent:", (nltk.classify.accuracy(voted_classifier, testing_set))*100)
##
##print("Classification:", voted_classifier.classify(testing_set[0][0]), "Confidence %:",voted_classifier.confidence(testing_set[0][0])*100)
##print("Classification:", voted_classifier.classify(testing_set[1][0]), "Confidence %:",voted_classifier.confidence(testing_set[1][0])*100)
##print("Classification:", voted_classifier.classify(testing_set[2][0]), "Confidence %:",voted_classifier.confidence(testing_set[2][0])*100)
##print("Classification:", voted_classifier.classify(testing_set[3][0]), "Confidence %:",voted_classifier.confidence(testing_set[3][0])*100)
##print("Classification:", voted_classifier.classify(testing_set[4][0]), "Confidence %:",voted_classifier.confidence(testing_set[4][0])*100)
##print("Classification:", voted_classifier.classify(testing_set[5][0]), "Confidence %:",voted_classifier.confidence(testing_set[5][0])*100)
##
##
 
