from nltk.corpus import wordnet

words = ['big_dog', 'little_girl', 'tall_man', 'good_morning', 'huge_cat']
syns = {w : [] for w in words}
i = 0
j = 0
l = 0

i = i+1
j = j+1
l = l+1


m=0

while(m<2):
    for k, v in syns.items():
        for synset in wordnet.synsets(k):
            i+=1
            for hypernym in synset.hypernyms():
                j+=1
                for lemma in synset.lemmas():
                        l+=1
                        v.append(lemma.name())
                        m+=1
                        print(syns)
print('synsets',i)
print('hypernyms',j)
print('instacne_hypernysms',l)
