import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()
a = "This is a good movie."
print(sid.polarity_scores(a))