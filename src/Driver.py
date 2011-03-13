import nltk
from nltk.corpus import treebank

test_set = [0,1,5,6,8,12,13,26,54,66,69,73,75,79,80,83,95,114,130,146,152,153]
chunks = nltk.corpus.treebank_chunk.chunked_sents()

#grammar2 = "NP: {<PRP$>?<CD>?<DT>?<JJ.*>*<NN.*>*<POS>?<NN.*>*<JJ>?<CD>?}"
grammar = r"""
    NP: {<NN.*><CD><JJ>?}
        {<CD><NN.*>*<CD>?<JJ>?}
        {<DT|PP\$>?<JJ|RB>*<NN.*>+<VBG>?<IN>?<JJ>*<NN.*>*}
        {}
"""

cp = nltk.RegexpParser(grammar)
result = cp.parse(treebank.tagged_sents()[test_set[0]])
print "My parse: \n" + str(result) + "\n"
print "Actual parse: \n" + str(chunks[test_set[0]])

eval = cp.evaluate(chunks[test_set[0]], grammar)
    
    