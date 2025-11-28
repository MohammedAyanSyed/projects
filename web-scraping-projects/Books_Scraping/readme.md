# 📚 BOOKS SCRAPING
This project scrapes book data from [Books to Scrape](http://books.toscrape.com/), 
a practice website designed for learning web scraping
## 📝 Introduction
* A collection of Python scripts for scraping and extracting data from websites
* It uses Python along with Requests for fetching HTML pages and BeautifulSoup for parsing and extracting information.

## 🧱 Folder Structure
``` text
Books_Scraping/
│── Books_Scraping.py
│── Books.csv
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
* The scraped data is saved in Books.csv file.
* Below is a sample preview of the output

```csv
Title,Price,Rating
A Light in the Attic,51.77,3
Tipping the Velvet,53.74,1
Soumission,50.1,1
Sharp Objects,47.82,4
```

## 📄 License
This project is licensed under the MIT License.