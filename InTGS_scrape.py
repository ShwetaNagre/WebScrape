from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import random
import csv

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-insecure-localhost")

# Set up Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://intgs.nii.ac.in/InTGS/search.php"

# Loop through the IDs
for i in range(1, 1731):
    # Navigate to the search page again for each ID
    driver.get(url)
    
    id_str = f"InTGS{i:06}"
    print(f"Processing ID: {id_str}")

    # Wait for the search box to appear and enter the ID
    search_box = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, 'textBox'))
    )
    search_box.clear()
    search_box.send_keys(id_str)
    search_box.send_keys(Keys.RETURN)

    # Wait for the content to load
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='content']"))
    )

    result_data = driver.page_source
    soup = BeautifulSoup(result_data, 'html.parser')

    # Find all tables
    tables = soup.find_all('table')

    if tables:
        print(f"Extracting data from {len(tables)} table(s) for {id_str}")

        # Open a new CSV file for this ID
        with open(f'{id_str}_data.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            for table_index, table in enumerate(tables):
                rows = table.find_all('tr')  # Find all rows of the table

                # Loop through rows and extract cells (td or th)
                for row in rows:
                    cols = [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]
                    writer.writerow(cols)  # Write each row to the CSV file

                print(f"Table {table_index + 1} data saved for {id_str}")
    else:
        print(f"No tables found for {id_str}")

    # Sleep for a random time between requests to avoid being flagged
    sleep_time = random.uniform(5, 20)
    print(f"Sleeping for {sleep_time:.2f} seconds...")
    time.sleep(sleep_time)

# Close the browser
driver.quit()
