#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import random

# Define a list of sample search queries (replace with queries of interest)
search_queries = ['python tutorial', 'weather forecast', 'online shopping', 'new movie releases']

# Define date range
start_date = pd.to_datetime('2024-01-01')
end_date = pd.to_datetime('2024-02-29')  # Adjust for desired period

# Create lists to store date, query, and search volume data
dates = []
queries = []
search_volume = []

# Simulate daily search volume for each query (random variation with seasonal trends)
for query in search_queries:
    for date in pd.date_range(start_date, end_date):
        month = date.month  # Consider seasonal variations for specific queries (e.g., higher in winter for 'holiday gifts')
        base_volume = 1000  # Adjust base search volume as needed
        seasonal_factor = 1.1 if month in [12, 1] else 0.9  # Example: Higher volume in December/January
        volume_variation = random.uniform(0.9, 1.1)  # Random variation around base volume

        daily_volume = int(base_volume * seasonal_factor * volume_variation)

        dates.append(date)
        queries.append(query)
        search_volume.append(daily_volume)

# Create DataFrame from lists
search_trends = pd.DataFrame({
    'Date': dates,
    'Search Query': queries,
    'Search Volume': search_volume
})

# Set Date and Search Query as index for multi-level analysis
search_trends.set_index(['Date', 'Search Query'], inplace=True)

# Print a sample of the data
print(search_trends.head())


# In[4]:


import matplotlib.pyplot as plt

# Visualize daily search volume trends for each query
search_trends.unstack(level='Search Query').plot(kind='line', figsize=(12, 6))
plt.xlabel('Date')
plt.ylabel('Search Volume')
plt.title('Daily Search Volume Trends (January - February 2024)')
plt.legend(title='Search Query')
plt.grid(True)
plt.show()

# (Optional) Calculate and visualize daily average, minimum, and maximum search volume per query
daily_stats_query = search_trends['Search Volume'].unstack(level='Search Query').resample('D').agg(['mean', 'min', 'max'])

# Visualize daily stats per query (consider for further insights)
# ... (code similar to daily traffic plot, using daily_stats_query DataFrame)


# In[ ]:




