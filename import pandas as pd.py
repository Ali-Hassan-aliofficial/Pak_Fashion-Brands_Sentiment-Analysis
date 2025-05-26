import pandas as pd

# Step 1: Load the Excel file
file_path = "filtered_reviews_without_lace.xlsx"
df = pd.read_excel(file_path)

# Step 2: Define the word to remove
word_to_remove = input("Enter the word you want to filter out from 'Review': ").strip().lower()

# Step 3: Find and count matching rows
mask = df['Review'].str.lower().str.contains(word_to_remove, na=False)
count_found = mask.sum()

print(f"\n🔍 The word '{word_to_remove}' was found in {count_found} review(s).")

# Step 4: Filter out the rows
df_filtered = df[~mask]

# Step 5: Ask user if they want to save the filtered file
save_file = input("Do you want to save the filtered file? (y/n): ").strip().lower()

if save_file == 'y':
    output_file = f"filtered_reviews_without_{word_to_remove}.xlsx"
    df_filtered.to_excel(output_file, index=False)
    print(f"✅ Filtered file saved as: {output_file}")
else:
    print("❌ File not saved.")