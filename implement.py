from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from numpy import array
from sklearn.metrics import accuracy_score
import pickle
####taking lists of common lexicons
posgram=[]
testpattern=[]
r=0;
neggram=[]
trainedprediction=[]
posunigrams = []
negunigrams = []
predictedlabels=[]
for word in open("positivelexicon.txt", encoding="utf-8").read().split("\n")[:-1]:
    abc = word_tokenize(word)
    for a in abc:
        posgram.append(a)
for word in open("negativelexicon.txt", encoding="utf-8").read().split("\n")[:-1]:
    abc = word_tokenize(word)
    for a in abc:
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

###mayadarling ka code
label=[]
for word in open("data_to_predict_label.txt", encoding="utf-8").read().split("\n")[:-1]:
    abc = word_tokenize(word)
    for a in abc:
        label.append(int(a))
for word in open("datatopredict.txt", encoding="utf-8").read().split("\n")[:-1]:
    dtp=[]
    abc = word_tokenize(word)
    for a in abc:
        if a.isalnum():
            dtp.append(a)
    # test_string=input("Enter a sentences\n")
    unigram=dtp
    bigram=[]
    trigram=[]
    stop_words = set(stopwords.words('english'))
    stop_words.remove('not')
    stop_words.remove('don')
    stop_words.remove('t')
    #    abc=word_tokenize(test_string)
    # for a in abc:
    #     if a.isalnum():
    #         unigram.append(a)
    unigram = [w for w in unigram if not w in stop_words]
    i=0
    while i<len(unigram)-1:
        bigram.append(unigram[i] + unigram[i+1])
        i+=1
    i=0
    while i<len(unigram)-2:
        trigram.append(unigram[i] + unigram[i + 1] + unigram[i + 2])
        i+=1
    ##comparing inputted data with previously stored data and forming pattern
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
    elif positive==negative:
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
    elif positive==negative:
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
    elif positive==negative:
        abcd.append(0)
    for word in unigram:
        positive += posgram.count(word)
    for word in unigram:
        negative += neggram.count(word)
    if positive > negative:
        abcd.append(1)
    elif positive<negative:
        abcd.append(2)
    elif positive==negative:
        abcd.append(0)
    # from numpy import array
    # abcd=array(abcd)
    print(r)
    r+=1
    with open("Trained_clf.pkl", "rb") as a:
        clfPicked= pickle.load(a)
    p=clfPicked.predict([abcd])
    for i in p:
        trainedprediction.append(i)
acc=accuracy_score(label,trainedpredictiongnb)
print(acc)

