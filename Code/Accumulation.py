import os
import pandas as pd
import matplotlib.pyplot as plt

# Define folder and output file
input_folder = "speed and distance"
output_file = "totals.csv"

# Initialize dictionary to store results
data_totals = {}

# Loop through files in the folder
for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):  # Ensure we only process CSV files
        filepath = os.path.join(input_folder, filename)

        # Extract year from filename (assuming format like '2013-14.csv')
        year = filename.replace(".csv", "")

        # Read the CSV file
        df = pd.read_csv(filepath)

        # Sum up all columns
        column_sums = df.sum(numeric_only=True).round(2)  # Round to 2 decimal places

        # Store results in dictionary
        data_totals[year] = column_sums

# Convert dictionary to DataFrame
totals_df = pd.DataFrame.from_dict(data_totals, orient='index')

# Recalculate specific columns
totals_df["Avg Speed"] = (totals_df["MIN"] / totals_df["Dist. Miles"]).round(2)

# Create new column Miles/Min
totals_df["Miles/Min"] = (totals_df["Dist. Feet"] / totals_df["MIN"]).round(5)

# Add a "Year" column and set it as the index
totals_df["Year"] = totals_df.index

# Sort the DataFrame by "Year" in ascending order
sorted_df = totals_df.sort_values("Year")

# Set the "Year" column to be the second column
sorted_df = sorted_df[["Year", "W", "L", "MIN", "Dist. Miles", "Dist. Feet", "Avg Speed", "Miles/Min"]]

# Drop the first column (which is the index column that was added)
sorted_df = sorted_df.reset_index(drop=True)

# Save to CSV
sorted_df.to_csv(output_file, index=False)

print(f"Totals saved to {output_file}")
