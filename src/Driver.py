import nltk

eval_set_pos = ['wsj_0023.pos', 'wsj_0054.pos', 'wsj_0057.pos', 'wsj_0063.pos', 
                'wsj_0066.pos', 'wsj_0068.pos', 'wsj_0069.pos', 'wsj_0084.pos', 
                'wsj_0124.pos', 'wsj_0197.pos']

grammar = r"""
    NP: {<DT>?<NN.*>+<VBG><NN.*>+}
        {<DT><CD>?<VBN><NN.*>*}
        {<DT><CD><VBG>?<NN.*>+}
        {<PDT>?<DT|WDT|PR.*>?<\$>?<CD>*<JJ.*>*<NN.*>*<POS>?<NN.*>*<\$>?<CD>*}
        {<WP.*>}
        {<EX>}  
"""

def create_parser(grammar):
    return nltk.RegexpParser(grammar)

def create_chunks_from_files(files):
    return nltk.corpus.treebank_chunk.chunked_sents(files)
   
def evaluate_grammar(parser, chunks):
    return parser.evaluate(chunks)   
       
def run():
    parser = create_parser(grammar)
    chunks = create_chunks_from_files(eval_set_pos)
    print evaluate_grammar(parser, chunks)

run()