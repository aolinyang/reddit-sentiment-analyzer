import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def setup():
    nltk.download('vader_lexicon')
    sid = SentimentIntensityAnalyzer()

def get_scores():
    pass