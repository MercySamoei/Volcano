import pandas as pd
import matplotlib.pyplot as plt

# Load the volcano dataset into a pandas DataFrame
df = pd.read_csv('volcano.csv')

# Count the frequency of each volcano name and store the result in a new DataFrame
name_counts = df['Name'].value_counts()

# Select the top 10 most common names
top_names = name_counts.head(10)

# Filter the dataframe to only include the top 10 most frequent volcano names
df_top = df[df['Name'].isin(top_names.index)]

# Group the data by Country and count the number of occurrences
country_counts = df_top.groupby('Country')['Name'].count()

# Create a bar chart of the country counts
plt.bar(country_counts.index, country_counts.values)

# Set the chart title and axis labels
plt.title('Countries with the Most Frequent Volcanoes')
plt.xlabel('Country')
plt.xticks(rotation=90)
plt.ylabel('Frequency')

# Display the chart
plt.show()
