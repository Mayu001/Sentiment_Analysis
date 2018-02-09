from collections import Counter
from nltk.tokenize import word_tokenize
#unigram bigrams trigrams

for line in open("positive_sentences.txt", encoding="utf-8").read().split("\n")[:-1]:
    #posUnigrams=word_tokenize(line)
    posUnigrams=line.split(" ")
    posBigrams=[]
    posTrigrams=[]
    i=0
    while i<len(posUnigrams)-1:
        posBigrams.append(posUnigrams[i] + posUnigrams[i+1])
        i+=1
    i=0
    while i<len(posUnigrams)-2:
        posTrigrams.append(posUnigrams[i] + posUnigrams[i + 1] + posUnigrams[i + 2])
        i+=1
#frequent items
most_common_posUnigrams= [word for word, word_count in Counter(posUnigrams).most_common(3)]  #unigram
most_common_posBigrams= [word for word, word_count in Counter(posBigrams).most_common(3)] #bigram
most_common_posTrigrams= [word for word, word_count in Counter(posTrigrams).most_common(3)] #trigram
print(most_common_posUnigrams,most_common_posBigrams,most_common_posTrigrams)

for line in open("negative_sentences.txt", encoding="utf-8").read().split("\n")[:-1]:
    #negUnigrams=word_tokenize(line)
    negUnigrams=line.split(" ")
    negBigrams=[]
    negTrigrams=[]
    i=0
    while i<len(negUnigrams)-1:
        negBigrams.append(negUnigrams[i] + negUnigrams[i+1])
        i+=1
    i=0
    while i<len(negUnigrams)-2:
        negTrigrams.append(negUnigrams[i] + negUnigrams[i + 1] + negUnigrams[i + 2])
        i+=1
#frequent items
#unigram
most_common_negUnigrams= [word for word, word_count in Counter(negUnigrams).most_common(3)]
#bigram
most_common_negBigrams= [word for word, word_count in Counter(negBigrams).most_common(3)]
#trigram
most_common_negTrigrams= [word for word, word_count in Counter(negTrigrams).most_common(3)]
print(most_common_negUnigrams,most_common_negBigrams,most_common_negTrigrams)

