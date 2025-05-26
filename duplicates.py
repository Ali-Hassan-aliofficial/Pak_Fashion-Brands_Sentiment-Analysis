import pandas as pd
import os

def main():
    # Step 1: Load the Excel file
    file_path = "filtered_reviews_without_strap.xlsx"  # Ensure this file exists in your working directory
    
    if not os.path.isfile(file_path):
        print(f"❌ File not found: {file_path}")
        return

    df = pd.read_excel(file_path)

    # Step 2: Check for duplicates in 'Review' column
    initial_count = len(df)
    df_unique = df.drop_duplicates(subset='Review', keep='first')  # Keep only the first occurrence
    duplicates_removed = initial_count - len(df_unique)

    print(f"\n🧹 Found and removed {duplicates_removed} duplicate review(s).")

    # Step 3: Ask if the user wants to save the cleaned file
    save_file = input("Do you want to save the deduplicated file? (y/n): ").strip().lower()

    if save_file == 'y':
        output_path = "deduplicated_reviews.xlsx"
        df_unique.to_excel(output_path, index=False)
        print(f"✅ Deduplicated file saved as: {output_path}")
    else:
        print("❌ File not saved.")

if __name__ == "__main__":
    main()
y