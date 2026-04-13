import re

class TextProcessor:
    def clean_text(self, text):
      
        text = re.sub(r"[^\w\s]", "", text) 
        text = re.sub(r"\s+", " ", text) 
        return text.strip()

    def get_stats(self, text):
       
        words = text.split()
        return {
            "word_count": len(words), 
            "char_count": len(text), 
            "avg_word_length": sum(len(w) for w in words) / len(words) if words else 0 
        }