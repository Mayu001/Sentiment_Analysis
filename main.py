from collections import Counter
#from nltk.tokenize import word_tokenize
#unigram bigrams trigrams
posUnigram=[]
posBigram=[]
posTrigram=[]

for line in open("positive_sentences.txt", encoding="utf-8").read().split("\n")[:-1]:
    #posUnigrams=word_tokenize(line)
    pU=line.split(" ")
    pB=[]
    pT=[]
    i=0
    while i<len(pU)-1:
        pB.append(pU[i] + pU[i+1])
        i+=1
    i=0
    while i<len(pU)-2:
        pT.append(pU[i] + pU[i + 1] + pU[i + 2])
        i+=1
    posUnigram=posUnigram+pU
    posBigram=posBigram+pB
    posTrigram=posTrigram+pT
#frequent items
most_common_posUnigrams= [word for word, word_count in Counter(posUnigram).most_common(1000)]  #unigram
import pickle
with open("common_posUnigrams.pkl", "wb") as a1:
    pickle.dump(most_common_posUnigrams, a1)
most_common_posBigrams= [word for word, word_count in Counter(posBigram).most_common(1000)] #bigram
with open("most_common_posBigrams.pkl", "wb") as a1:
    pickle.dump(most_common_posBigrams, a1)
most_common_posTrigrams= [word for word, word_count in Counter(posTrigram).most_common(1000)] #trigram
with open("most_common_posTrigrams.pkl", "wb") as a1:
    pickle.dump(most_common_posTrigrams, a1)
print(most_common_posUnigrams,most_common_posBigrams,most_common_posTrigrams)
print('\n\n')
negUnigram=[]
negBigram=[]
negTrigram=[]
for line in open("negative_sentences.txt", encoding="utf-8").read().split("\n")[:-1]:
    #negUnigrams=word_tokenize(line)
    nU=line.split(" ")
    nB=[]
    nT=[]
    i=0
    while i<len(nU)-1:
        nB.append(nU[i] + nU[i+1])
        i+=1
    i=0
    while i<len(nU)-2:
        nT.append(nU[i] + nU[i + 1] + nU[i + 2])
        i+=1
    negUnigram=negUnigram+nU
    negBigram=negBigram+nB
    negTrigram=negTrigram+nT
#frequent items
most_common_negUnigrams= [word for word in Counter(negUnigram).most_common(1000)]  #unigram
with open("most_common_negUnigrams.pkl", "wb") as a1:
    pickle.dump(most_common_negUnigrams, a1)
most_common_negBigrams= [word for word, word_count in Counter(negBigram).most_common(1000)] #bigram
with open("most_common_negBigrams.pkl", "wb") as a1:
    pickle.dump(most_common_negBigrams, a1)
most_common_negTrigrams= [word for word, word_count in Counter(negTrigram).most_common(1000)] #trigram
with open("most_common_negTrigrams.pkl", "wb") as a1:
    pickle.dump(most_common_negTrigrams, a1)
print(most_common_negUnigrams,most_common_negBigrams,most_common_negTrigrams)

