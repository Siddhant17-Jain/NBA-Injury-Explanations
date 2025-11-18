import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the updated CSV file
input_file = "Historical Pace with Total Miles.csv"
df = pd.read_csv(input_file)

# Extract decade from the Season column (e.g., 79-80 -> 1980s)
df['Decade'] = df['Season'].apply(lambda x: str(int(x.split('-')[0]) // 10 * 10) + 's')

# Group by decade and calculate the total miles for each decade
decade_miles = df.groupby('Decade')['Total Miles'].sum()

# Calculate the number of seasons in each decade (for averaging)
seasons_in_decade = df.groupby('Decade').size()

# Calculate the average miles per season for each decade
average_miles_per_season = decade_miles / seasons_in_decade

# Plotting the bar chart
plt.figure(figsize=(18, 12))
average_miles_per_season.plot(kind='bar', color='skyblue')

# Add titles and labels
plt.title("Average Miles per Season by Decade", fontsize=14)
plt.xlabel("Decade", fontsize=12)
plt.ylabel("Average Miles per Season", fontsize=12)

# Customize the y-axis to show gridlines at every 5 units
plt.yticks(range(0, int(average_miles_per_season.max()) + 5, 5))

# Enable gridlines on the y-axis with major lines
plt.grid(True, axis='y', linestyle='-', linewidth=1)

# Display the plot
plt.tight_layout()
plt.show()
