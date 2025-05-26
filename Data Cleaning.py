import pandas as pd
import re

# Step 1: Load dataset
df = pd.read_excel("Daraz Dataset - Updated.xlsx")

# Step 2: Load custom stopwords from file
with open("stopwords.txt", 'r', encoding='utf-8') as f:
    custom_stopwords = set(f.read().splitlines())

# Step 3: Clean the review text
def clean_text(text):
    if pd.isna(text):
        return ""
    text = text.lower()                               # Convert to lowercase
    text = re.sub(r"[^\w\s]", "", text)               # Remove punctuation/special characters
    text = re.sub(r"\d+", "", text)                   # Remove digits
    tokens = text.split()                             # Tokenize
    tokens = [word for word in tokens if word not in custom_stopwords]  # Remove stopwords
    return " ".join(tokens)

# Step 4: Apply cleaning function
df['Cleaned_Review'] = df['Review'].apply(clean_text)

# Step 5: Clean up dataframe
df = df.drop(columns=["Unnamed: 1"], errors="ignore")         # Remove unwanted columns
df = df.drop_duplicates(subset="Review")                      # Remove duplicate reviews
df = df.dropna(subset=["Review"])                             # Remove rows with missing reviews
df = df.reset_index(drop=True)

# Step 6: Save the cleaned dataset
df.to_excel("final_cleaned_daraz_reviews.xlsx", index=False)
print("✅ Cleaned dataset saved as 'final_cleaned_daraz_reviews.xlsx'")
