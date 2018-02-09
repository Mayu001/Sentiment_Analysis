import pickle
univtrainedlist=[]
for line in open("positive_sentences.txt", encoding="utf-8").read().split("\n")[:-1]:
    #posUnigrams=word_tokenize(line)
    #print(line)
    positive = 0
    negative = 0
    abc = line.split(" ")
    unigram = []
    for a in abc:
        if a.isalnum():
            unigram.append(a)
    #unigram=line.split(" ")
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
    posunigrams = []
    negunigrams = []
    with (open("common_posUnigrams.pkl", "rb")) as openfile:
        while True:
            try:
                posunigrams.append(pickle.load(openfile))
            except EOFError:
                break
    with (open("most_common_negUnigrams.pkl", "rb")) as openfile:
        while True:
            try:
                negunigrams.append(pickle.load(openfile))
            except EOFError:
                break
    positive = 0
    df=open("positivelexicon.txt",'r')

    # posunigrams=df.readlines()
    # posunigrams=[w[0:-1] for w in posunigrams]
    #
    # df=open("negativelexicon.txt",'r')
    # negunigrams = df.readlines()
    # negunigrams = [w[0:-1] for w in negunigrams]
    abcd=[]
    word = ""
    #print(posunigrams)
    for word in unigram:
        #print(posunigrams)
        if word in posunigrams:
            positive+=1
        if word in negunigrams:
            positive-=1
    abcd.append(positive)
        #trainedlist.insert(0,positive)
        #trainedlist.insert(0, negative)
    #check for bigrams
    posbigrams = []
    with (open("most_common_posBigrams.pkl", "rb")) as openfile:
        while True:
            try:
                posbigrams.append(pickle.load(openfile))
            except EOFError:
                break
    negbigrams = []
    with (open("most_common_negBigrams.pkl", "rb")) as openfile:
        while True:
            try:
                negbigrams.append(pickle.load(openfile))
            except EOFError:
                break
    positive=0
    word=""
    for word in bigram:
        #print(word)
        if word in posbigrams:
            positive += 1
        elif word in negbigrams:
            positive -= 1
    abcd.append(positive)
        #trainedlist.insert(0,positive)
        #trainedlist.insert(0, negative)
    # check for trigrams
    postrigrams = []
    positive = 0
    word = ""
    with (open("most_common_posBigrams.pkl", "rb")) as openfile:
        while True:
            try:
                postrigrams.append(pickle.load(openfile))
            except EOFError:
                break
    negtrigrams = []
    with (open("most_common_negBigrams.pkl", "rb")) as openfile:
        while True:
            try:

                negtrigrams.append(pickle.load(openfile))
            except EOFError:
                break
    for word in trigram:
        if word in postrigrams:
            positive += 1
        if word in negtrigrams:
            positive -= 1
    abcd.append(positive)
        #trainedlist.insert(0,positive)
        #trainedlist.insert(0, negative)
    univtrainedlist.append(abcd)
print(univtrainedlist)