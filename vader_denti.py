import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Step 1: Load cleaned data
df = pd.read_excel("final_cleaned_daraz_reviews.xlsx")

# Step 2: Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Step 3: Define sentiment function using compound score
def get_vader_sentiment(text):
    if pd.isna(text) or not text.strip():
        return "neutral"
    score = analyzer.polarity_scores(text)
    compound = score['compound']
    if compound >= 0.05:
        return 'positive'
    elif compound <= -0.05:
        return 'negative'
    else:
        return 'neutral'

# Step 4: Apply VADER to Cleaned_Review
df['Sentiment'] = df['Cleaned_Review'].apply(get_vader_sentiment)

# Step 5: Save result
df.to_excel("vader_sentiment_reviews.xlsx", index=False)
print("✅ Sentiment added using VADER and file saved as 'vader_sentiment_reviews.xlsx'")
