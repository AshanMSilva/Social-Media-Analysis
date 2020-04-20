from nltk.corpus import wordnet

syn = wordnet.synsets("nothing")

print(syn)
print(syn[0])

#######only word
print(syn[0].lemmas()[0].name())

print(syn[0].definition())
print(syn[0].examples())

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("hip.n.01")

print(w1.wup_similarity(w2))
