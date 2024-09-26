# WebScrape

Retrieving data from web pages, especially when the data is presented in tables or figures, can be a cumbersome and time-consuming task, particularly when handling large datasets. This Python script automates the process of searching for patient IDs on a portal and extracting the relevant data from the resulting report. The extracted tables are saved in CSV format, making it easy to handle and analyze the data.

Unlike typical web scraping tools like Web Scraper, which work well for static pages or bulk data extraction, this script is designed specifically for cases where you need to search for each patient ID individually on a portal. The report for each ID opens in a separate result page, and conventional scraping tools cannot handle this dynamic interaction efficiently. This tool was developed to solve this specific problem for 1,730 patients, saving hours of manual effort.

# Features

Automated Search: The script searches for patient IDs on the portal.  
Data Extraction: Extracts tables from the report pages and saves them as CSV files.  
Random Buffer Time: Introduces a random delay between searches to avoid overloading the server or triggering anti-bot mechanisms.  
Batch Processing: Handles multiple patient IDs in a single run, significantly reducing manual effort.  

# Requirments

Before running this script, ensure you have the following dependencies installed:

Python 3.12.2  
Requests: For handling HTTP requests  
BeautifulSoup (bs4): For parsing and scraping HTML  
Pandas: For handling and saving data in CSV format  
Selenium: For automating the search and navigation on dynamic web pages  
