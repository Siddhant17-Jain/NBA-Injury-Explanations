import os
import pandas as pd
import matplotlib.pyplot as plt

# Define the input file and read the data
input_file = "totals.csv"
df = pd.read_csv(input_file)

# Plot Year vs Miles/Min
plt.figure(figsize=(10, 6))
plt.plot(df["Year"], df["Feet/Min"], marker='o', linestyle='-', color='b', label='Feet/Min')

# Adding titles and labels
plt.title("Year vs Feet/Min")
plt.xlabel("Year")
plt.ylabel("Feet/Min")
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
plt.grid(True)

# Set y-axis limits
plt.ylim(360, 410)

# Set major and minor ticks on the y-axis
plt.yticks(range(360, 411, 10))  # Major ticks at every 10 units
plt.minorticks_on()  # Enable minor ticks
plt.grid(which='minor', linestyle=':', linewidth=0.5)  # Dotted lines for minor ticks

# Adding the legend
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()
