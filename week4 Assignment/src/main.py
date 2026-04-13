import os
import nltk
from nltk.tokenize import word_tokenize
import pandas as pd

from text_processor import TextProcessor
from regex_analyzer import RegexAnalyzer
from pos_analyzer import POSAnalyzer
from morphology import MorphologyAnalyzer
from semantic import SemanticAnalyzer
from visualizer import NLPVisualizer


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('maxent_ne_chunker')
nltk.download('words')

tp = TextProcessor()
ra = RegexAnalyzer()
pa = POSAnalyzer()
mo = MorphologyAnalyzer()
sa = SemanticAnalyzer()

results = []

for file in os.listdir("../data"):
    
    with open(f"../data/{file}", encoding="utf-8") as f:
        text = f.read()
    
    clean = tp.clean_text(text)
    stats = tp.get_stats(clean)
    
    words = word_tokenize(clean)
    lemmas = mo.lemmatize(words)
    
    pos_tags, freq = pa.analyze(words)
    
    results.append({
        "file": file,
        **stats,
        "dates": len(ra.extract_dates(clean)),
        "percent": len(ra.extract_percentages(clean)),
        "sentiment": round(sa.sentiment(clean), 3),
        "top_pos": freq.most_common(3),
        "entities": sa.named_entities(pos_tags)[:3]
    })

df = pd.DataFrame(results)
print(df)
viz = NLPVisualizer()
viz.plot_word_counts(df)
viz.plot_sentiment_distribution(df)