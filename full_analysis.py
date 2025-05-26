import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

# Load the dataset
df = pd.read_excel("vader_sentiment_reviews.xlsx")

# 🛠️ Clean 'Date' column: convert and drop bad entries
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # Convert valid dates only
df = df.dropna(subset=['Date'])                           # Drop rows with invalid dates

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M').astype(str)

# Set Seaborn style
sns.set(style="whitegrid")

# Create PDF report
pdf = PdfPages("Sentiment_Report_Fashion_Brands.pdf")

# --- 1. Pie chart of overall sentiment ---
plt.figure(figsize=(6, 6))
df['Sentiment'].value_counts().plot.pie(autopct='%1.1f%%', colors=['#8BC34A','#FFC107','#F44336'])
plt.title("Overall Sentiment Distribution")
plt.ylabel("")
pdf.savefig()
plt.close()

# --- 2. Monthly sentiment trend (all brands) ---
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Month', hue='Sentiment', palette='Set2')
plt.title("Sentiment Trend Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
pdf.savefig()
plt.close()

# --- 3. Sentiment count per brand ---
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Brand', hue='Sentiment', palette='Set1')
plt.title("Sentiment Distribution by Brand")
plt.xticks(rotation=45)
plt.tight_layout()
pdf.savefig()
plt.close()

# --- 4. Stacked bar: Total sentiment per brand ---
sentiment_counts = df.groupby(['Brand', 'Sentiment']).size().unstack().fillna(0)
sentiment_counts.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='viridis')
plt.title("Stacked Sentiment per Brand")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=45)
plt.tight_layout()
pdf.savefig()
plt.close()

# --- 5. Heatmap: Brand vs Month sentiment volume ---
heatmap_data = df.groupby(['Month', 'Brand']).size().unstack().fillna(0)
plt.figure(figsize=(12, 6))
sns.heatmap(heatmap_data, annot=True, fmt='.0f', cmap='YlGnBu')
plt.title("Volume of Reviews by Brand and Month")
plt.tight_layout()
pdf.savefig()
plt.close()

# --- 6. Top Performing Brands Summary (text in console) ---
summary = sentiment_counts.sort_values(by='positive', ascending=False)
print("Top brands by positive sentiment:\n", summary)

# --- 7. Line plot: Monthly trend of each sentiment ---
monthly_trend = df.groupby(['Month', 'Sentiment']).size().reset_index(name='Counts')
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_trend, x='Month', y='Counts', hue='Sentiment', marker='o', palette='muted')
plt.title("Monthly Sentiment Trend (Line Plot)")
plt.xticks(rotation=45)
plt.xlabel("Month")
plt.ylabel("Number of Reviews")
plt.tight_layout()
pdf.savefig()
plt.close()

# --- 8. Box plot: Review frequency by brand ---
review_counts = df.groupby('Brand').size().reset_index(name='Review Count')
plt.figure(figsize=(10, 6))
sns.boxplot(data=review_counts, y='Review Count')
plt.title("Review Frequency Spread Across Brands")
plt.tight_layout()
pdf.savefig()
plt.close()

# --- 9. Bar Plot: Total Reviews Per Brand ---
total_reviews = df['Brand'].value_counts().reset_index()
total_reviews.columns = ['Brand', 'Total Reviews']
plt.figure(figsize=(10, 6))
sns.barplot(data=total_reviews, x='Brand', y='Total Reviews', palette='coolwarm')
plt.title("Total Reviews per Brand")
plt.xticks(rotation=45)
for i, row in total_reviews.iterrows():
    plt.text(i, row['Total Reviews'] + 1, int(row['Total Reviews']), ha='center')
plt.tight_layout()
pdf.savefig()
plt.close()

# --- 10. Sentiment Ratio Summary Table (printed) ---
sentiment_ratio = sentiment_counts.div(sentiment_counts.sum(axis=1), axis=0).round(2)
print("\n🔎 Sentiment Ratio per Brand (Normalized):\n", sentiment_ratio)

# --- 11. Annotated Heatmap: Brand and Month with review volumes ---
plt.figure(figsize=(12, 6))
sns.heatmap(heatmap_data, annot=True, fmt='.0f', cmap='coolwarm', linewidths=0.5, linecolor='gray')
plt.title("📊 Annotated Review Volume by Brand and Month")
plt.xlabel("Brand")
plt.ylabel("Month")
plt.tight_layout()
pdf.savefig()
plt.close()


# Save all plots to PDF
pdf.close()
print("✅ PDF report 'Sentiment_Report_Fashion_Brands.pdf' created successfully.")
