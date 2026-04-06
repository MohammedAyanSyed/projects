# Importing Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = 'https://www.flipkart.com/search?q=mobile'

# Connection
response = requests.get(url)

# Html code
content = response.content

# Soup object
soup = BeautifulSoup(content,'html.parser')

# Name
name_tag = soup.find_all('div',class_='KzDlHZ')
name = [x.get_text() for x in name_tag]

# Price
price_tag = soup.find_all('div',class_='Nx9bqj _4b5DiR')
price = [x.get_text().strip('₹') for x in price_tag]

# MRP
mrp_tag = soup.find_all('div',class_='yRaY8j ZYYwLA')
mrp = [x.get_text().strip('₹') for x in mrp_tag]

# Discount
discount_tag = soup.find_all('div',class_='UkUFwK')
discount = [int(x.get_text().strip('% off')) for x in discount_tag[:24]]

# Ratings
ratings_tag = soup.find_all('div',class_='XQDdHH')
ratings = [float(x.get_text()) for x in ratings_tag[:24]]

specs_tag = soup.find_all('ul',class_='G4BRas')

# Storage
storage = [x.find('li',class_='J+igdf').get_text().replace('|','&') for x in specs_tag]

# Display
display = [x.find_all('li',class_='J+igdf')[1].get_text() for x in specs_tag]

# Camera
camera = [x.find_all('li',class_='J+igdf')[2].get_text() for x in specs_tag]

# Battery
battery = [int(x.find_all('li',class_='J+igdf')[3].get_text().strip('mAh Battery')) for x in specs_tag]

# Processor
processor = [x.find_all('li',class_='J+igdf')[4].get_text().replace('\n','')
             if len(x.find_all('li',class_='J+igdf'))>4 and 'Processor' in
             x.find_all('li', class_='J+igdf')[4].get_text()
             else None for x in specs_tag]

# DataFrame
df = pd.DataFrame({'Mobile':name,'Price (₹)':price,'MRP':mrp,'Discount (%)' : discount,'Rating':ratings,
                          'Storage' : storage,'Display':display,'Camera':camera,'Battery (MAH)':battery,
                            'Processor':processor})
# CSV File
df.to_csv('flipkart_mobiles.csv',index=False)