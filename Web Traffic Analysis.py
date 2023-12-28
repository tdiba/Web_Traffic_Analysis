#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_excel(r"C:\Users\USER\Documents\Chat GPT Projects\RAW DATA\Website Traffic Analysis\Website_Traffic_Analysis.xlsx")


# In[3]:


df.head()


# In[4]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


# Set the aesthetic style of the plots
sns.set_style("whitegrid")


# In[6]:


# Calculate key metrics
total_sessions = df['Session ID'].nunique()
average_session_duration = df['Session Duration'].mean()
average_pageviews = df['Pageviews'].mean()


# In[9]:


# Create a bar plot for these metrics
metrics = ['Total Sessions', 'Avg. Session Duration (s)', 'Avg. Pageviews']
values = [total_sessions, average_session_duration, average_pageviews]
plt.figure(figsize=(10, 6))
sns.barplot(x=metrics, y=values, palette="viridis")
plt.title('Overview of Website Traffic')
plt.ylabel('Values')
plt.show()


# In[10]:


total_sessions, average_session_duration, average_pageviews


# In[11]:


# Calculate overall bounce rate
bounce_rate = df['Bounce Rate'].mean()


# In[12]:


# Distribution of bounce rates by page
bounce_rate_by_page = df.groupby('Page URL')['Bounce Rate'].mean().sort_values(ascending=False)


# In[13]:


# Visualize the results
plt.figure(figsize=(12, 6))
sns.histplot(bounce_rate_by_page, bins=30, kde=True, color='blue')
plt.title('Distribution of Bounce Rates by Page URL')
plt.xlabel('Bounce Rate')
plt.ylabel('Number of Pages')
plt.axvline(x=bounce_rate, color='red', linestyle='--')
plt.text(bounce_rate + 0.02, 5, f'Overall Bounce Rate: {bounce_rate:.2f}', color='red')
plt.show()


# In[14]:


bounce_rate


# In[15]:


# Extract the top user navigation paths
navigation_paths = df.groupby('Session ID')['Page URL'].apply(lambda x: ' -> '.join(x)).value_counts().head(10)


# In[16]:


# Visualization of top navigation paths
plt.figure(figsize=(12, 8))
sns.barplot(y=navigation_paths.index, x=navigation_paths.values, palette="mako")
plt.title('Top 10 User Navigation Paths')
plt.xlabel('Number of Occurrences')
plt.ylabel('Navigation Paths')
plt.show()


# In[17]:


navigation_paths


# In[18]:


# Calculate overall conversion rate
conversion_rate = df['Conversion'].mean()


# In[19]:


# Relationship between session duration, pageviews, bounce rate, and conversion
conversion_factors = df.groupby('Conversion').agg({
    'Session Duration': 'mean',
    'Pageviews': 'mean',
    'Bounce Rate': 'mean'
})


# In[20]:


# Visualizing the relationship
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

sns.barplot(x=conversion_factors.index, y=conversion_factors['Session Duration'], ax=axes[0])
axes[0].set_title('Average Session Duration vs Conversion')
axes[0].set_xlabel('Conversion')
axes[0].set_ylabel('Average Session Duration (s)')

sns.barplot(x=conversion_factors.index, y=conversion_factors['Pageviews'], ax=axes[1])
axes[1].set_title('Average Pageviews vs Conversion')
axes[1].set_xlabel('Conversion')
axes[1].set_ylabel('Average Pageviews')

sns.barplot(x=conversion_factors.index, y=conversion_factors['Bounce Rate'], ax=axes[2])
axes[2].set_title('Average Bounce Rate vs Conversion')
axes[2].set_xlabel('Conversion')
axes[2].set_ylabel('Average Bounce Rate')

plt.tight_layout()
plt.show()


# In[21]:


conversion_rate, conversion_factors


# In[ ]:




