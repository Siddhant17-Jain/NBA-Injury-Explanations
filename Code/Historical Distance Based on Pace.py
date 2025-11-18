import matplotlib.pyplot as plt
import pandas as pd

# Load the data from the new CSV file
input_file = "Historical Pace with Feet.csv"
df = pd.read_csv(input_file)

# Ensure the DataFrame is sorted by Season
df = df.sort_values("Season")

# Create a more spacious line plot
plt.figure(figsize=(20, 14))  # Increased size
plt.plot(df["Season"], df["Feet/Min"], marker='o', color='blue', linestyle='-')  # Color changed to blue

# Add titles and labels
plt.title("Estimated Feet/Min by Season (Based on Historical Pace)", fontsize=14)
plt.xlabel("Season", fontsize=12)
plt.ylabel("Estimated Feet/Min", fontsize=12)

# Rotate x-axis labels for better spacing
plt.xticks(rotation=45, ha='right')

# Customize y-axis ticks and gridlines
plt.yticks(range(330, 421, 10))  # Major gridlines at intervals of 10 (330 to 420)
plt.gca().yaxis.grid(True, which='major', color='black', linestyle='-', linewidth=1)  # Solid line for major ticks
plt.gca().yaxis.grid(True, which='minor', color='gray', linestyle=':', linewidth=0.5)  # Dotted line for minor ticks

# Set minor ticks every 2 units on the y-axis
plt.minorticks_on()

# Hide labels for minor ticks (intervals of 2)
plt.tick_params(axis='y', which='minor', labelleft=False)

# Add gridlines for minor ticks (dotted lines)
plt.grid(True, which='major',color='black', axis='x', linestyle='-', linewidth=1)

# Add padding for better layout
plt.tight_layout(pad=3.0)

# Show the plot
plt.show()
