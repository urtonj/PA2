import nltk
from nltk.corpus import treebank

index = 0

trees = nltk.corpus.treebank_chunk
chunks = trees.chunked_sents()
test = chunks[0]

corpus = treebank.tagged_sents()[index]
#print corpus

grammar2 = "NP: {<PRP$>?<CD>?<DT>?<JJ.*>*<NN.*>*<POS>?<NN.*>*<JJ>?<CD>?}"
grammar = r"""
    NP: {<NN.*><CD><JJ>?}
        {<CD><NN.*>*<CD>?<JJ>?}
        {<DT|PP\$>?<JJ|RB>*<NN.*>+<VBG>?<IN>?<JJ>*<NN.*>*}
        {}
"""
grammar3 = ""

#cp = nltk.RegexpParser(grammar)
cp = nltk.RegexpChunkParser(grammar)
result = cp.evaluate(test)
print result



#print result
#print type(nltk.corpus.treebank_chunk.chunked_sents())
#print cp.evaluate(nltk.corpus.treebank_chunk.chunked_words())
#print cp.evaluate(treebank.tagged_sents()[index])
#print cp.evaluate() #insert gold standard here - a subset of nltk.corpus.treebank_chunk



#print result
#print treebank.tagged_sents()[index]
#print result, "\n", treebank.parsed_sents()[index]
#for sentence in corpus:
    
    