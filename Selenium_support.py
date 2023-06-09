from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import csv
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

val = input("Enter a URL: ")
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 1000000000000)
driver.get(val)
wait.until(EC.url_to_be(val))

#Extracting data from District section

district_data = Select(driver.find_element(By.ID,'district_code'))
selected_options_district = [option.text for option in district_data.options]

selected_options_district.remove("--Select District--")

# Repeat the same steps for other sections (Block, School, Phase, Class)

# Extracting data from Block section
# Wait for the element with ID 'block_code' to be visible
selected_options_block=[]

for district_option in selected_options_district:
    # Select the district option
    district_data.select_by_visible_text(district_option)

    # Wait for the block options to be populated
    block_element = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, 'block_code'))
    )
   
    # Extracting data from Block section for the selected district
    block_data = Select(block_element)
    selected_options_block_1 = [option.text for option in block_data.options]
    selected_options_block.extend(selected_options_block_1)
    selected_options_block.remove("--Select Block--")
    
# # Extracting data from School section
selected_options_School=[]
for block_option in selected_options_block:
    # Select the block option
    try:
        block_data.select_by_visible_text(block_option)

    # Wait for the School options to be populated
        School_element = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.ID, 'school_code'))
        )

    # Extracting data from School section for the selected block
        School_data = Select(School_element)
        selected_options_School_1 = [option.text for option in School_data.options]
        selected_options_School.extend(selected_options_School_1)
        selected_options_School.remove("--Select School--")

    except NoSuchElementException:
        print(f"No block options found for '{district_option}'. Skipping...")
     
# # Extracting data from Phase section
selected_options_Phase=[]
for School_option in selected_options_School:
    # Select the School option
    try:
        School_data.select_by_visible_text(School_option)

    # Wait for the block options to be populated
        Phase_element = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.ID, 'phase'))
        )

    # Extracting data from Block section for the selected district
        Phase_data = Select(Phase_element)
        selected_options_Phase_1 = [option.text for option in Phase_data.options]
        selected_options_Phase.extend(selected_options_Phase_1)
        selected_options_Phase.remove("--Select Phase--")
    except NoSuchElementException:
        print(f"No School options found for '{School_option}'. Skipping...")

# # Extracting data from Class section
selected_options_Class=[]
for Phase_option in selected_options_Phase:
    # Select the phase
    try:
        Phase_data.select_by_visible_text(Phase_option)

    # Wait for the  class to be populated
        Class_element = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.ID, 'class_code'))
        )

    # Extracting class from Phase section for the selected block
        Class_data = Select(Class_element)
        selected_options_Class_1 = [option.text for option in Class_data.options]
        selected_options_Class.extend(selected_options_Class_1)
        selected_options_Class.remove("--Select Class--")
    except NoSuchElementException:
        print(f"No Class options found for '{Phase_option}'. Skipping...")
     
# Find the search button element and click it

search_button = driver.find_element_by_xpath("//a[@class='submit_school_record_btn' and @id='forward']")
search_button.click()

# Wait for the search results to load
wait = WebDriverWait(driver, 10)  # Adjust the timeout value as needed
results_loaded = wait.until(EC.presence_of_element_located((By.XPATH, "xpath_to_search_results")))

# Get all elements in the search results
result_elements = driver.find_elements_by_xpath("xpath_to_each_result_element")

# Iterate over each result element
values = []
for element in result_elements:
    # Retrieve the values from each element and add them to the list
    value = element.text
    values.append(value)

# Write the values to a CSV file
filename = "beneficiary_values.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Value"])  # Write header row
    writer.writerows(values)  # Write values rows

print("Values have been stored in", filename)

# Close the browser
driver.quit()


