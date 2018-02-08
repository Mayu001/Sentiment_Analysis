from collections import Counter
samplestring='I am a good boy I amm good good am boy girl'
#unigram bigrams trigrams
unigrams=samplestring.split(" ")
bigrams=[]
trigrams=[]
i=0
while i<len(unigrams)-1:
    bigrams.append(unigrams[i] + unigrams[i+1])
    i+=1
i=0
while i<len(unigrams)-2:
    trigrams.append(unigrams[i] + unigrams[i + 1] + unigrams[i + 2])
    i+=1
#frequent items
#unigram
most_common_unigrams= [word for word, word_count in Counter(unigrams).most_common(3)]
#bigram
most_common_bigrams= [word for word, word_count in Counter(bigrams).most_common(3)]
#trigram
most_common_trigrams= [word for word, word_count in Counter(trigrams).most_common(3)]
print(most_common_unigrams,most_common_bigrams,most_common_trigrams)