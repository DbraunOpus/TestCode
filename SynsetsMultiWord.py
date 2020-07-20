from nltk.corpus import wordnet

words = ['big_dog', 'little_girl', 'tall_man', 'good_morning', 'huge_cat']
syns = {w : [] for w in words}
synsets = 0
hypernyms = 0
instance_hypernyms = 0

synsets = i+1
hypernyms = j+1
instance_hypernyms = l+1

Integ
instanceCounter=0

while(instanceCounter<2):
    for k, v in syns.items():
        for synset in wordnet.synsets(k):
            synsets+=1
            for hypernym in synset.hypernyms():
                hypernyms+=1
                for lemma in synset.lemmas():
                       instance_hypernyms +=1
                        v.append(lemma.name())
                        m+=1
                        print(syns)
print('synsets',synsets)
print('hypernyms',hypernyms)
print('instance_hypernysms',instance_hypernyms)
