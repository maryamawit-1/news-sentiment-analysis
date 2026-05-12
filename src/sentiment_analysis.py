from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()


def calculate_sentiment(headline):

    score = sia.polarity_scores(headline)

    return score['compound']