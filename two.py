import pandas as pd
import matplotlib.pyplot as plt

# Load the volcano dataset into a pandas DataFrame
df = pd.read_csv('volcano.csv')

# Count the frequency of each volcano name and store the result in a new DataFrame
name_counts = df['Name'].value_counts()

# Select the top 10 most common names
top_names = name_counts.head(10)

# Create a bar chart of the top name counts
plt.bar(top_names.index, top_names.values)

# Set the chart title and axis labels
plt.title('Top 10 Most Common Volcano Names')
plt.xlabel('Volcano Name')
plt.xticks(rotation=90)
plt.ylabel('Frequency')

# Display the chart
plt.show()
