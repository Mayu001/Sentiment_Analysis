samplestring='I am a good boy'
unigrams=samplestring.split(" ")
bigrams=[]
trigrams=[]
i=0
while i<len(unigrams)-1:
    bigrams.append(unigrams[i]+" "+unigrams[i+1])
    i+=1
i=0
while i<len(unigrams)-2:
    trigrams.append(unigrams[i] + " " + unigrams[i + 1] + " " + unigrams[i + 2])
    i+=1
for i in trigrams:
    print(i)
