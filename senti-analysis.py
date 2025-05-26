from textblob import TextBlob
import pandas as pd

# Load the cleaned data
df = pd.read_excel("final_cleaned_daraz_reviews.xlsx")

# Define sentiment analysis function
def get_sentiment_label(text):
    if pd.isna(text) or not text.strip():
        return "neutral"
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"

# Apply sentiment analysis
df['Sentiment'] = df['Cleaned_Review'].apply(get_sentiment_label)

# Save updated file with sentiment column
df.to_excel("sentiment_scored_reviews.xlsx", index=False)
print("✅ Sentiment added to 'Sentiment' column and file saved.")


