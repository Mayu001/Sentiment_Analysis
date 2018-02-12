import pickle
from nltk.tokenize import word_tokenize
from sklearn import svm
univtrained=[]
univnature=[]
posgram=[]
neggram=[]
posunigrams = []
negunigrams = []
clf = svm.SVC()
for word in open("positivelexicon.txt", encoding="utf-8").read().split("\n")[:-1]:
    abc = word_tokenize(word)
    for a in abc:
        if a.isalnum():
            posgram.append(a)
for word in open("negativelexicon.txt", encoding="utf-8").read().split("\n")[:-1]:
    abc = word_tokenize(word)
    for a in abc:
        if a.isalnum():
            neggram.append(a)
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
    for word in unigram:
        positive += posunigrams.count(word)
    for word in unigram:
        negative += negunigrams.count(word)
    if positive > negative:
     abcd.append(1)
    elif positive<negative:
     abcd.append(2)
    else:
        abcd.append(0)
    positive=0
    negative=0
    word=""
    for word in bigram:
        positive += posbigrams.count(word)
    for word in bigram:
        negative += negbigrams.count(word)
    if positive > negative:
     abcd.append(1)
    elif positive<negative:
     abcd.append(2)
    else:
        abcd.append(0)
    positive = 0
    negative = 0
    for word in trigram:
        positive += postrigrams.count(word)
    for word in trigram:
        negative += negtrigrams.count(word)
    if positive > negative:
     abcd.append(1)
    elif positive<negative:
     abcd.append(2)
    else:
        abcd.append(0)
    for word in unigram:
        positive += posgram.count(word)
    for word in trigram:
        negative += neggram.count(word)
    if positive > negative:
     abcd.append(1)
    elif positive<negative:
     abcd.append(2)
    else:
        abcd.append(0)
    univtrained.append(abcd)
    univnature.append(1)
for line in open("negative_sentences.txt", encoding="utf-8").read().split("\n")[:-1]:
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
    for word in unigram:
        positive += posunigrams.count(word)
    for word in unigram:
        negative += negunigrams.count(word)
    if positive > negative:
     abcd.append(1)
    elif positive<negative:
     abcd.append(2)
    else:
        abcd.append(0)
    positive=0
    negative=0
    word=""
    for word in bigram:
        positive += posbigrams.count(word)
    for word in bigram:
        negative += negbigrams.count(word)
    if positive > negative:
     abcd.append(1)
    elif positive<negative:
     abcd.append(2)
    else:
        abcd.append(0)
    positive = 0
    negative = 0
    for word in trigram:
        positive += postrigrams.count(word)
    for word in trigram:
        negative += negtrigrams.count(word)
    if positive > negative:
     abcd.append(1)
    elif positive<negative:
     abcd.append(2)
    else:
        abcd.append(0)
    for word in unigram:
        positive += posgram.count(word)
    for word in trigram:
        negative += neggram.count(word)
    if positive > negative:
     abcd.append(1)
    elif positive<negative:
     abcd.append(2)
    else:
        abcd.append(0)
    univtrained.append(abcd)
    univnature.append(0)
clf.fit(univtrained, univnature)
with open("Trained_clf.pkl", "wb") as a:
    pickle.dump(clf, a)
print("training done")
