from nltk.corpus import wordnet
from input import hypernymList

words = []
#adds to the current list
words.append(hypernymList)
syns = {w : [] for w in words}
#variables
synsets = 0
hypernyms = 0
instance_hypernyms = 0

synsets = synsets+1
hypernyms = hypernyms+1
instance_hypernyms = instance_hypernyms+1

m=0

while(m<2):
    for k, v in syns.items():
        for synset in wordnet.synsets(k):
            synsets+=1
            for hypernym in synset.hypernyms():
                hypernyms+=1
                for lemma in synset.lemmas():
                        instance_hypernyms+=1
                        v.append(lemma.name())
                        m+=1
                        if (synsets>1):
                                        print('Found!',synsets,'Synset')
                        else:
                                        print('None Found!')
#this is the code that searches for custom words
