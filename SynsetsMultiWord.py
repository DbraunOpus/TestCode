from nltk.corpus import wordnet as wn
from itertools import chain
from itertools import groupby

noun_lemmas_in_wordnet = set(chain(*[ss.lemma_names() for ss in wn.all_synsets(pos='n')]))

actual_list = []

list2 = noun_lemmas_in_wordnet
actual_list.append(list2)
actual_list = " ".join(list2)

char_list = ['_']

res = [ele for ele in list2 if all(ch in ele for ch in char_list)]

print ("The filtered words are : " + str(res))
