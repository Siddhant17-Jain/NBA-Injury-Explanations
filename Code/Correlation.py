import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Step 1: Load and sort Pace vs Feet data based on the Year column
input_file = "Pace vs Feet.csv"
df = pd.read_csv(input_file)

# Sort the data by Year in ascending order
df = df.sort_values("Year")

# Step 2: Calculate the correlation between Pace and Feet/Min
pace = df["Pace"]
feet_min = df["Feet/Min"]

# Calculate the correlation coefficient and R-squared value
correlation = pace.corr(feet_min)
slope, intercept, r_value, p_value, std_err = linregress(pace, feet_min)
r_squared = r_value**2

# Step 3: Plot the data and the regression line
plt.figure(figsize=(10, 6))
plt.scatter(pace, feet_min, color='blue', label='Data points')
plt.plot(pace, slope * pace + intercept, color='red', label=f'Fitted line (R²={r_squared:.3f})')

# Adding titles and labels
plt.title("Pace vs Feet/Min")
plt.xlabel("Pace")
plt.ylabel("Feet/Min")
plt.legend()
plt.grid(True)

# Display the plot
plt.tight_layout()
plt.show()

# Step 4: Output the R-squared value
print(f"R-squared value: {r_squared:.3f}")
# Step 5: Output the regression line formula
print(f"Regression line formula: Feet/Min = {slope:.3f} * Pace + {intercept:.3f}")
