from src.text_processor import TextProcessor
from src.morphology import MorphologyAnalyzer 

def test_clean():
    tp = TextProcessor()
    text = "Hey this code!!! working !! 123 right"
    
    cleaned = tp.clean_text(text)
    assert "!" not in cleaned

def test_stats():
    tp = TextProcessor()
    text = "Hello world"
    
    stats = tp.get_stats(text) 
    assert stats['word_count'] == 2

def test_lemmatization():
    mo = MorphologyAnalyzer()
    text = "running cats"
    
    lemmas = mo.lemmatize_text(text) 
    assert "cat" in lemmas