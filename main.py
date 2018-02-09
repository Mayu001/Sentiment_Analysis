from collections import Counter
from nltk.tokenize import word_tokenize
samplestring='I am a good boy I amm good good am boy girl'
samplestring1='I am a bad boy I amm bad bad am boy girl'
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


