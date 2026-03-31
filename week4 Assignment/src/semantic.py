from textblob import TextBlob
import nltk

class SemanticAnalyzer:
    
    def sentiment(self, text):
        blob = TextBlob(text)
        return blob.sentiment
    
    def named_entities(self, text):
        tokens = nltk.word_tokenize(text)
        tags = nltk.pos_tag(tokens)
        tree = nltk.ne_chunk(tags)
        
        entities = []
        for subtree in tree:
            if hasattr(subtree, 'label'):
                entity = " ".join(word for word, tag in subtree)
                entities.append((entity, subtree.label()))
        
        return entities