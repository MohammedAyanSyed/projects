# 📱 Flipkart Mobiles 
A Python Based web scraping project to collect smartphone specifications and price from [flipkart](https://www.flipkart.com/search?q=mobile)

# 📝 Introduction
* A collection of Python scripts for scraping and extracting data from flipkart
* It uses Python along with Requests for fetching HTML page and BeautifulSoup for parsing and extracting information

## 🧱 Folder Structure
``` text
Flipkart_Mobiles/
│── flipkart_mobile_scraper.py
│── flipkart_mobiles.csv
│── readme.md
```
## 🛠️ Tech Stack
* Python 🐍 (3.8+ recommended)
* Requests 
* BeautifulSoup
* Pandas 🐼

## ▶️ How to Run
1. Make sure you have Python installed
2. Install the required libraries

``` bash

pip install requests beautifulsoup4 pandas
```

## 📊 Output
* The scraped data is saved in flipkart_mobiles.csv file.
* Below is a sample preview of the output

```csv
obile,Price (₹),MRP,Discount (%),Rating,Storage,Display,Camera,Battery (MAH),Processor
"Samsung Galaxy F36 5G (Red, 128 GB)","15,999","22,999",30,4.3,6 GB RAM & 128 GB ROM & Expandable Upto 2 TB,17.02 cm (6.7 inch) Full HD+ Display,50MP + 8MP + 2MP | 13MP Front Camera,5000,Samsung Exynos 1380 Processor
"Samsung Galaxy F36 5G (Black, 256 GB)","19,499","27,499",29,4.2,8 GB RAM & 256 GB ROM & Expandable Upto 2 TB,17.02 cm (6.7 inch) Full HD+ Display,50MP + 8MP + 2MP | 13MP Front Camera,5000,Samsung Exynos 1380 Processor
"IQOO Z10X 5G (Titanium, 128 GB)","14,399","17,499",17,4.4,6 GB RAM & 128 GB ROM,17.02 cm (6.7 inch) Display,50MP Rear Camera,6500,
"POCO C71 (Cool Blue, 128 GB)","6,799","9,999",32,4.1,6 GB RAM & 128 GB ROM & Expandable Upto 2 TB,17.48 cm (6.88 inch) HD+ Display,32MP Rear Camera | 8MP Front Camera,5200,Unisoc T7250Max clock speed: 2 x A75@1.8GHz6 x A55@1.6GHz Processor
```
## 🔄 Data Variability
The data shown in the sample output is only for demonstration. The actual scraped data may change over time as the website updates its content.

## 📄 License
This project is licensed under the MIT License.