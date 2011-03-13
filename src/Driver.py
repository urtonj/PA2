import nltk
from nltk.corpus import treebank

test_set = ['wsj_0001.pos', 'wsj_0002.pos', 'wsj_0006.pos', 'wsj_0007.pos', 'wsj_0009.pos',
            'wsj_0013.pos', 'wsj_0014.pos', 'wsj_0027.pos', 'wsj_0055.pos', 'wsj_0067.pos', 
            'wsj_0070.pos', 'wsj_0074.pos', 'wsj_0076.pos', 'wsj_0080.pos', 'wsj_0081.pos', 
            'wsj_0084.pos', 'wsj_0096.pos', 'wsj_0115.pos', 'wsj_0131.pos', 'wsj_0147.pos',
            'wsj_0153.pos', 'wsj_0154.pos']

#grammar2 = "NP: {<PRP$>?<CD>?<DT>?<JJ.*>*<NN.*>*<POS>?<NN.*>*<JJ>?<CD>?}"    
grammar = r"""
    NP: {<NN.*><CD><JJ>?}
        {<CD><NN.*>*<CD>?<JJ>?}
        {<DT|PP\$>?<CD>?<VBG>?<JJ|RB>*<NN.*>+<VBG>?<JJ>*<NN.*>*}
        }<CD><NNS><JJ>{
        {<CD><NNS>}
        }<NNS><JJ>{
        {<NNS>}
        {<WDT>}
"""

chunks = nltk.corpus.treebank_chunk.chunked_sents(test_set)
parser = nltk.RegexpParser(grammar)

index = 16

result = parser.parse(treebank.tagged_sents()[index])
print "My parse: \n" + str(result) + "\n"
print "Actual parse: \n" + str(nltk.corpus.treebank_chunk.chunked_sents()[index])

print parser.evaluate(chunks)
