pip install selenium streamlit pymysql

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time

# WebDriver setup
driver = webdriver.Chrome()

# List of bus links
bus_links = ["https://www.redbus.in/online-booking/apsrtc/?utm_source=rtchometile",
             "https://www.redbus.in/online-booking/ksrtc-kerala/?utm_source=rtchometile",
             "https://www.redbus.in/online-booking/rsrtc/?utm_source=rtchometile",
             "https://www.redbus.in/online-booking/south-bengal-state-transport-corporation-sbstc/?utm_source=rtchometile",
             "https://www.redbus.in/online-booking/hrtc/?utm_source=rtchometile",
             "https://www.redbus.in/online-booking/astc/?utm_source=rtchometile",
             "https://www.redbus.in/online-booking/uttar-pradesh-state-road-transport-corporation-upsrtc/?utm_source=rtchometile",
             "https://www.redbus.in/online-booking/wbtc-ctc/?utm_source=rtchometile",
             "https://www.redbus.in/online-booking/tsrtc/?utm_source=rtchometile"
             "https://www.redbus.in/online-booking/bihar-state-road-transport-corporation-bsrtc/?utm_source=rtchometile",]

# Initialize lists to store results
all_links = []
all_routes = []
all_source = []

# Function to extract bus links and routes
def extract_links_and_routes():
    links = []
    routes = []
    for i in range(1, 10):  # Adjust the range according to the pagination
        elements = driver.find_elements(By.XPATH, "//a[@class='route']")
        for elem in elements:
            links.append(elem.get_attribute("href"))
            routes.append(elem.text)
        try:
            pagination = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="DC_117_paginationTable"]')))
            next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()={i+1}]')
            driver.execute_script("arguments[0].scrollIntoView();", next_button)
            time.sleep(3)
            next_button.click()
        except NoSuchElementException:
            print(f"No more pages to paginate at step {i}")
            break
    return links, routes

# Loop through each link to extract data
for link in bus_links:
    driver.get(link)
    time.sleep(3)  # Wait for the page to fully load
    wait = WebDriverWait(driver, 20)
    links, routes = extract_links_and_routes()
    all_links.extend(links)
    all_routes.extend(routes)
    all_source.extend([link] * len(links))

# Convert to DataFrame
df = pd.DataFrame({
    "Route Name": all_routes,
    "Route Link": all_links
})

# Print the DataFrame
df
