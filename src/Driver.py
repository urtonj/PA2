import nltk
from nltk.corpus import treebank

index = 0

corpus = treebank.tagged_sents()[index]

grammar2 = "NP: {<PRP$>?<CD>?<DT>?<JJ.*>*<NN.*>*<POS>?<NN.*>*<JJ>?<CD>?}"
grammar = r"""
    NP: {<NN.*><CD><JJ>?}
        {<CD><NN.*>*<CD>?<JJ>?}
        {<DT|PP\$>?<JJ|RB>*<NN.*>+<VBG>?<IN>?<JJ>*<NN.*>*}
        {}

"""

#cp = nltk.RegexpParser(grammar)
cp = nltk.RegexpChunkParser(grammar)
result = cp.parse(corpus)
print result
#print cp.evaluate() #insert gold standard here - a subset of nltk.corpus.treebank_chunk



#print result
#print treebank.tagged_sents()[index]
#print result, "\n", treebank.parsed_sents()[index]
#for sentence in corpus:
    
    