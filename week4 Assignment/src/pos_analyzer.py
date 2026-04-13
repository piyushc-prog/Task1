import nltk
from collections import Counter

class POSAnalyzer:
    
    def analyze(self, text):
        tokens = nltk.word_tokenize(text)
        pos_tags = nltk.pos_tag(tokens)
        
        freq = Counter(tag for word, tag in pos_tags)
        
        return freq, pos_tags
    
    def noun_phrases(self, text):
        grammar = "NP: {<DT>?<JJ>*<NN>}"
        cp = nltk.RegexpParser(grammar)
        
        tokens = nltk.word_tokenize(text)
        tags = nltk.pos_tag(tokens)
        
        tree = cp.parse(tags)
        
        return [" ".join(word for word, tag in subtree)
                for subtree in tree.subtrees()
                if subtree.label() == "NP"]