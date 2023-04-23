import pandas as pd
import matplotlib.pyplot as plt

# Load the volcano dataset into a pandas DataFrame
df = pd.read_csv('volcan.csv')

# Set the figure size
fig, ax = plt.subplots(figsize=(10, 8))

# Create a scatter plot of volcano elevation vs. type
plt.scatter(df['Elevation (Meters)'], df['Type'])

# Set the chart title and axis labels
plt.title('Volcano Elevation vs Type')
plt.xlabel('Elevation (Meters)')
plt.ylabel('Volcano Type')

# Display the chart
plt.show()
