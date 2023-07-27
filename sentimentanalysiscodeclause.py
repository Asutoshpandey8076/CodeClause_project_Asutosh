import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon (run this line only once)
nltk.download('vader_lexicon')

# Create an instance of the SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Sample text for sentiment analysis
sample_text = "I absolutely loved the movie! The plot was captivating, and the acting was superb."

# Perform sentiment analysis
sentiment_scores = analyzer.polarity_scores(sample_text)

# Interpret the sentiment score
if sentiment_scores['compound'] >= 0.05:
    sentiment = 'Positive'
elif sentiment_scores['compound'] <= -0.05:
    sentiment = 'Negative'
else:
    sentiment = 'Neutral'

# Display the results
print("Sample Text:", sample_text)
print("Sentiment:", sentiment)
print("Sentiment Scores:", sentiment_scores)
