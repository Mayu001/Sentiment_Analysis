import pickle
from nltk.tokenize import word_tokenize
univtrained={}
posunigrams = []
negunigrams = []
with (open("common_posUnigrams.pkl", "rb")) as openfile:
    while True:
        try:
            posunigrams=(pickle.load(openfile))
        except EOFError:
            break
with (open("most_common_negUnigrams.pkl", "rb")) as openfile:
    while True:
        try:
            negunigrams=(pickle.load(openfile))
        except EOFError:
            break
posbigrams = []
with (open("most_common_posBigrams.pkl", "rb")) as openfile:
    while True:
        try:
            posbigrams=(pickle.load(openfile))
        except EOFError:
            break
negbigrams = []
with (open("most_common_negBigrams.pkl", "rb")) as openfile:
    while True:
        try:
            negbigrams=(pickle.load(openfile))
        except EOFError:
            break
postrigrams = []
with (open("most_common_posTrigrams.pkl", "rb")) as openfile:
    while True:
        try:
            postrigrams=(pickle.load(openfile))
        except EOFError:
            break
negtrigrams = []
with (open("most_common_negTrigrams.pkl", "rb")) as openfile:
    while True:
        try:

            negtrigrams=(pickle.load(openfile))
        except EOFError:
            break
##comparing    *****************************
for line in open("positive_sentences.txt", encoding="utf-8").read().split("\n")[:-1]:
    positive = 0
    abc = word_tokenize(line)
    unigram = []
    for a in abc:
        if a.isalnum():
            unigram.append(a)
    bigram=[]
    trigram=[]
    trainedlist=[]
    i=0
    while i<len(unigram)-1:
        bigram.append(unigram[i] + unigram[i+1])
        i+=1
    i=0
    while i<len(unigram)-2:
        trigram.append(unigram[i] + unigram[i + 1] + unigram[i + 2])
        i+=1
    #check for unigrams

    positive = 0
    negative = 0
    abcd=[]
    word =""
    if any(word in unigram for word in posunigrams):
      positive+=1
    if any(word in unigram for word in negunigrams):
      negative-=1
    if positive >negative:
        abcd.append(positive)
    else:
        abcd.append(negative)
    positive=0
    negative=0
    word=""
    if any(word in bigram for word in posbigrams):
      positive+=1
    if any(word in bigram for word in negbigrams):
      negative-=1
    if positive >negative:
        abcd.append(positive)
    else:
        abcd.append(negative)
    positive = 0
    negative = 0
    word = ""
    if any(word in trigram for word in postrigrams):
      positive+=1
    if any(word in trigram for word in negtrigrams):
      negative-=1
    if positive >negative:
        abcd.append(positive)
    else:
        abcd.append(negative)
    print(abcd)
    univtrained
print(univtrained)

