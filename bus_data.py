driver = webdriver.Chrome()

# Maximize window
driver.maximize_window()

# Initialize empty lists to store extracted data
bus_links = []
bus_routes = []
bus_names = []
bus_types = []
departing_times = []
durations = []
reaching_times = []
star_ratings = []
prices = []
seats_availability = []

# Wait for elements to load
wait = WebDriverWait(driver, 3)

def click_all_view_buses_buttons():
    try:
        while True:
            # Find all "View Buses" buttons
            view_buses_buttons = driver.find_elements(By.XPATH, "//div[@class='button' and contains(text(), 'View Buses')]")
            
            if not view_buses_buttons:
                break

            # Click each button and wait for the details to load
            for button in view_buses_buttons:
                try:
                    driver.execute_script("arguments[0].scrollIntoView(true);", button)  # Scroll to the button
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(button))
                    driver.execute_script("arguments[0].click();", button)  # Click using JavaScript
                    time.sleep(5)  # Wait for additional details to load

                except Exception as e:
                    pass

            # Scroll to the bottom to load more buttons, if any
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)  # Wait for new content to load

            # Check if new buttons appeared; if not, exit the loop
            new_view_buses_buttons = driver.find_elements(By.XPATH, "//div[@class='button' and contains(text(), 'View Buses')]")
            if len(new_view_buses_buttons) == len(view_buses_buttons):
                break

    except Exception as e:
        pass


# Loop over each row in the DataFrame
for index, row in df.iterrows():
    link = row["Route Link"]
    route_name = row["Route Name"]
    
    # Load the bus route link
    driver.get(link)
    time.sleep(5)  # Wait for the page to fully load
    
    # Click on all "View Buses" buttons
    click_all_view_buses_buttons()

    # Extract bus details
    try:
        bus_name_elements = driver.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
        bus_type_elements = driver.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
        departing_time_elements = driver.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
        reaching_time_elements = driver.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
        duration_elements = driver.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")
        star_rating_elements = driver.find_elements(By.XPATH, "//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")
        price_elements = driver.find_elements(By.XPATH, '//*[@class="fare d-block"]')
        seats_availability_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'seat-left')]")

        # Append the data to respective lists
        for i in range(len(bus_name_elements)):
            bus_links.append(link)
            bus_routes.append(route_name)
            bus_names.append(bus_name_elements[i].text if i < len(bus_name_elements) else "N/A")
            bus_types.append(bus_type_elements[i].text if i < len(bus_type_elements) else "N/A")
            departing_times.append(departing_time_elements[i].text if i < len(departing_time_elements) else "N/A")
            reaching_times.append(reaching_time_elements[i].text if i < len(reaching_time_elements) else "N/A")
            durations.append(duration_elements[i].text if i < len(duration_elements) else "N/A")
            star_ratings.append(star_rating_elements[i].text if i < len(star_rating_elements) else "N/A")
            prices.append(price_elements[i].text if i < len(price_elements) else "N/A")
            seats_availability.append(seats_availability_elements[i].text if i < len(seats_availability_elements) else "N/A")

    except Exception as e:
        pass

# Close the WebDriver
driver.quit()

# Create a DataFrame from the extracted data
bus_data = pd.DataFrame({
    "Link": bus_links,
    "Route": bus_routes,
    "Bus Name": bus_names,
    "Bus Type": bus_types,
    "Departing Time": departing_times,
    "Reaching Time": reaching_times,
    "Duration": durations,
    "Star Rating": star_ratings,
    "Price": prices,
    "Seats Availability": seats_availability
})

# Save the DataFrame to a CSV file
bus_data.to_csv("bus_data.csv", index=False)
