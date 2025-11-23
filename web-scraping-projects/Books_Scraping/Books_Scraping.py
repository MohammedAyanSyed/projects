import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://books.toscrape.com/'
response = requests.get(url)
data = response.content
soup = BeautifulSoup(data,'html.parser')

# Books Title
t = soup.find_all('h3')
title = [i.a['title'] for i in t]

# Books Price
p = soup.find_all('p',class_='price_color')
Price = [float(i.get_text().replace('£','')) for i in p]

# Books Rating
rating_map = {'One':1,'Two':2,'Three':3,'Four':4,'Five':5}
r = soup.find_all('p',class_='star-rating')
Rating = [rating_map[i.get('class')[1]] for i in r]
print(Rating)

# Making DataFrame
df = pd.DataFrame({'Title':title,'Price':Price,'Rating':Rating})

df.to_csv('Books.csv',index=False)