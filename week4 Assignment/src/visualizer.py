import matplotlib.pyplot as plt
import seaborn as sns

class NLPVisualizer:
    @staticmethod
    def plot_word_counts(df):
        
        plt.figure(figsize=(10, 6))
        sns.barplot(x='file', y='word_count', data=df, palette='viridis')
        plt.title('Word Count per News Article')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_sentiment_distribution(df):
        
        plt.figure(figsize=(8, 5))
        sns.histplot(df['sentiment'], kde=True, color='skyblue')
        plt.title('Sentiment Polarity Distribution')
        plt.xlabel('Polarity (-1 to 1)')
        plt.show()