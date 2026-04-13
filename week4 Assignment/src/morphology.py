from nltk.stem import WordNetLemmatizer

class MorphologyAnalyzer:
    
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
    
    def lemmatize_text(self, text):
        words = text.split()
        return [self.lemmatizer.lemmatize(w) for w in words]
    
    def find_suffix(self, word):
        return word[-3:]
    
    def find_prefix(self, word):
        return word[:3]