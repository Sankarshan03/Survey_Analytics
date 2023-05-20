from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import csv
from selenium.webdriver.common.by import By


val = input("Enter a URL: ")
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get(val)
wait.until(EC.url_to_be(val))

#Extracting data from District section

district_data = Select(driver.find_element(By.ID,'district_code'))
selected_options_district = [option.text for option in district_data.options]

filename = 'District.csv'
with open(filename, 'w', newline='') as f:
    Information_District = csv.writer(f)
    Information_District.writerow(selected_options_district)  # Writing to CSV
    df = pd.DataFrame([selected_options_district])
    df.to_excel('District.xlsx', index=False, header=False)  # Writing to Excel file

# Repeat the same steps for other sections (Block, School, Phase, Class)

# Extracting data from Block section
# Wait for the element with ID 'block_code' to be visible
selected_options_block=[]
for district_option in selected_options_district:
    # Select the district option
    district_data.select_by_visible_text(district_option)

    # Wait for the block options to be populated
    block_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'block_code'))
    )

    # Extracting data from Block section for the selected district
    block_data = Select(block_element)
    selected_options_block_1 = [option.text for option in block_data.options]
    selected_options_block.extend(selected_options_block_1)

filename1 = 'Block.csv'
with open(filename1, 'w', newline='') as f:
    Information_Block = csv.writer(f)
    Information_Block.writerow(selected_options_block)  # Writing to CSV
    df1 = pd.DataFrame([selected_options_block])
    df1.to_excel('Block.xlsx', index=False, header=False)  # Writing to Excel file

# Extracting data from School section
selected_options_School=[]
for block_option in selected_options_block:
    # Select the block option
    block_data.select_by_visible_text(block_option)

    # Wait for the School options to be populated
    School_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'school_code'))
    )

    # Extracting data from School section for the selected block
    School_data = Select(School_element)
    selected_options_School_1 = [option.text for option in School_data.options]
    selected_options_School.extend(selected_options_School_1)

filename2 = 'School.csv'
with open(filename2, 'w', newline='') as f:
    Information_School = csv.writer(f)
    Information_School.writerow(selected_options_School)  # Writing to CSV
    df2 = pd.DataFrame([selected_options_School])
    df2.to_excel('School.xlsx', index=False, header=False)  # Writing to Excel file

# Extracting data from Phase section
selected_options_Phase=[]
for School_option in selected_options_School:
    # Select the district option
    School_data.select_by_visible_text(School_option)

    # Wait for the block options to be populated
    Phase_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'phase'))
    )

    # Extracting data from Block section for the selected district
    Phase_data = Select(Phase_element)
    selected_options_Phase_1 = [option.text for option in Phase_data.options]
    selected_options_Phase.extend(selected_options_Phase_1)

filename3 = 'Phase.csv'
with open(filename3, 'w', newline='') as f:
    Information_Phase = csv.writer(f)
    Information_Phase.writerow(selected_options_Phase)  # Writing to CSV
    df3 = pd.DataFrame([selected_options_Phase])
    df3.to_excel('Phase.xlsx', index=False, header=False)  # Writing to Excel file

# Extracting data from Class section
Class_data = Select(driver.find_element(By.ID,'class_code'))
selected_options_Class = [option.text for option in Class_data.options]

filename4 = 'Class.csv'
with open(filename4, 'w', newline='') as f:
    Information_Class = csv.writer(f)
    Information_Class.writerow(selected_options_Class)  # Writing to CSV
    df4 = pd.DataFrame([selected_options_Class])
    df4.to_excel('Class.xlsx', index=False, header=False)  # Writing to Excel file
