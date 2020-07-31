from nltk.corpus import wordnet as wn
from itertools import islice

synsets = 0
hypernyms = 0
instance_hypernysms = 0

synsets = synsets+1
hypernyms = hypernyms+1
instance_hypernysms = instance_hypernysms+1

iterationCounter=0

while(iterationCounter<2):
        for synset in islice(wn.all_synsets('n'), 5):
            synsets+=1
            for hypernym in synset.hypernyms():
                hypernyms+=1
                for lemma in synset.lemmas():
                        instance_hypernysms+=1
                        iterationCounter+=1

print('Number of synsets',synsets)
print('Number of hypernyms',hypernyms)
print('Number of instance_hypernyms',instance_hypernysms)
