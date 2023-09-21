#!/usr/bin/env python
# coding: utf-8

# Part 1. 

# I choose to have all the package imported and store here. 

# In[35]:


# First import the packages we need

# Lets us talk to other servers on the web
import requests

# Use BeautifulSoup to parse some HTML
from bs4 import BeautifulSoup

# Safetly quoting strings for URLs
from urllib.parse import unquote, quote

# Handling dates and times
from datetime import datetime

# DataFrames!
import pandas as pd
import numpy as np

# Data visualization
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sb


# here below I call the covid-19 api and first i choose to use the link on the example by changing the south africa to USA to find the total cnfirms cases in the united states. 

# In[36]:


# API calls come in the form of URLs


url = "https://api.covid19api.com/total/country/usa/status/confirmed"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

response.json()


# In[37]:


confirm_cases = response.json()
confirm_cases[-1]["Cases"]


# after printing the code i went up on the data to check if the data is correct and the data that is in thefiles is the same as the one here. 

# I choisse to divide the two because I think it would be much easier for me to solve the problem.

# Below i imported the summary of the covid-19 api and now I am going to find the total confirms deaths.

# In[28]:


#import requests

url = "https://api.covid19api.com/summary"


response = requests.get(url)

data = response.json()["Countries"]
print(data)


# I am calling an empty list to solve for max country and assign a 0 to the maximum death variable and use the for loop to solve for the maximum death as the countries are already called from the list.  

# In[32]:


max_deaths = 0
max_country = []

for country_data in data:
    if country_data["TotalDeaths"] > max_deaths:
        max_deaths = country_data["TotalDeaths"]
        max_country = country_data["Country"]

print(f"The country with the most COVID deaths is {max_country} with {max_deaths} deaths.")


# In[ ]:


Part 2. 


# In[177]:


nasa_url = 'https://api.nasa.gov/planetary/apod?api_key=ygrbjdKyYxNshuGv2pbv39hnnJrpYhcQeIQ0mHK3'

response = requests.get(nasa_url)

print(response.json())
respone = response.json()
response


# for the code above I only get to request the code and run for the url and now I am running out of time.

# Here below I imported the url and I run the api and get below the information see below.

# In[180]:



space_url = 'https://api.spacexdata.com/v4/launches/latest'

response = requests.get(space_url)
data = response.json()
print(data)
data


# In[181]:


print(data['name'])


# here  as there are many data and other link so i only chose to look for the name of the launched spaceship. 
# I think there would be a lot I would be done to expand the code but I fell like i do  not wanna focus more on redoing the same we did in class. 

# Part 3

# I run the url and I found the data that it's contructed with. see below

# In[41]:


# Create a variable called URL
url = "http://www.guitarsite.com/fuzz-pedals/"

# Use requests.get to grab the html
html = requests.get(url)

# Examine it -- what does it look like? What format is it?
print(html.text)


# In[152]:


# Now let's turn it into soup
# The first argument is our HTML, which we can access with .text
# The second argument is our parser -- we can use lxml, html, and there are others...
soup = BeautifulSoup(html.text, 'html')


# i called the soup function to get acces for other and now I print it below. 

# In[43]:


print(soup)


# In[44]:


tables = soup.find_all("table")


# In[49]:


len(tables)


# above I called the table variable and nfind the lenght of the table which is 7

# In[55]:


tables


# In[58]:


table = soup.find('table', {'id': 'amptb'})
print(table)


# In[61]:


titles = table.find_all('h3')

for title in titles:
    print(title.text)


# with this passage of code I realized that with html we can have moore accees to the different funtion and variable that the text are contruct with or website. I have learned and I still want to profound my knowledge to this.  

# In[ ]:


Part 4


# I requested the data of one of my high scholl and run it. see information below.

# In[102]:


url = "https://www.uwc.org/schools/uwc-adriatic"

# Use requests.get to grab the html
html = requests.get(url)

# Examine it -- what does it look like? What format is it?
print(html.text)
html


# here I called an empty list and append the link that content href and see result below. 

# In[112]:


links = []
for link in soup.find_all('a', href=True):
    links.append(link['href'])

print(links)


# I called soup below and here I have it below.

# In[123]:


soup = BeautifulSoup(html.text, 'html')


# In[124]:


soup


# In[131]:


soup.find("a")


# In[132]:


# The first h1
soup.find("h1")


# In[133]:


soup.find("h1").text


# In[134]:


images = soup.find_all('img')

print(len(images))


# In[135]:


# The first unordered list
soup.find("ul")


# In[139]:


links = soup.find_all("a")
links


# In[145]:


print(len(links))


# In[146]:


print(links)


# In[147]:


for l in links:
    print(l.text)


# In[148]:


# Get the URL of an a tag using .get('href')
for l in links:
    print(l.get('href'))


# In[149]:


# Start by finding all of the 'h2' tags
soup.find_all('h2')


# for part 4 I almost relied the class notes for the coding and for the function because I fell like it would have save me time of course It would be better to explore different option but I will do it on my own time. 

# Thanks 
