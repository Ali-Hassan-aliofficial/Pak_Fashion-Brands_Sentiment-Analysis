from googletrans import Translator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import time

# Load cleaned data
df = pd.read_excel("final_cleaned_daraz_reviews.xlsx")

# Initialize translator and sentiment analyzer
translator = Translator()
analyzer = SentimentIntensityAnalyzer()

# Translate Roman Urdu to English
def translate_text(text):
    try:
        translated = translator.translate(text, dest='en')
        return translated.text
    except:
        return ""

df['Translated_Review'] = df['Cleaned_Review'].apply(translate_text)
time.sleep(1)  # To avoid rate-limiting

# Apply VADER sentiment analysis
def get_vader_sentiment(text):
    if not text.strip():
        return "neutral"
    score = analyzer.polarity_scores(text)
    compound = score['compound']
    if compound >= 0.05:
        return 'positive'
    elif compound <= -0.05:
        return 'negative'
    else:
        return 'neutral'

df['Sentiment'] = df['Translated_Review'].apply(get_vader_sentiment)

# Save final result
df.to_excel("vader_sentiment_translated_reviews.xlsx", index=False)
print("✅ Translated, analyzed, and saved with accurate sentiments.")
