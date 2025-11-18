import pandas as pd

# Load the data from the CSV file
input_file = "Historical Pace with Feet.csv"
df = pd.read_csv(input_file)

# Calculate Total Feet (Feet/Min * 35 minutes * 70 games)
df["Total Feet"] = (df["Feet/Min"] * 35 * 70).round(2)

# Convert Total Feet to Total Miles (Total Feet / 5280)
df["Total Miles"] = (df["Total Feet"] / 5280).round(2)

# Optional: Save the updated DataFrame to a new CSV file
df.to_csv("Historical Pace with Total Miles.csv", index=False)

# Display the updated DataFrame
print(df.head())
