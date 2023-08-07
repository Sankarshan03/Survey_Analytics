from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)

val = input("Enter a URL: ")
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 1000000000000)
driver.get(val)
wait.until(EC.url_to_be(val))

search_button = driver.find_element(By.ID,"forward")
search_button.click()

# Wait for the table to appear after clicking the search button
wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
try:
    # Wait for the alert to appear
    alert = wait.until(EC.alert_is_present())

    # Handle the alert by accepting it
    alert.accept()

except UnexpectedAlertPresentException:
    # If the alert is already present, handle it here
    alert = driver.switch_to.alert
    alert.accept()

# Wait for 5 seconds before locating the table element
time.sleep(5)

# Extract the table data
table_element = WebDriverWait(driver, 10000).until(
    EC.presence_of_element_located((By.ID, 'example'))
)
table_rows = search_button.find_elements(By.TAG_NAME, "tr")  # Locate all table rows
table_data = []
for row in table_rows:
    row_data = [cell.text for cell in row.find_elements(By.TAG_NAME, "td")]  # Get the text from each cell in the row
    table_data.append(row_data)

# Print the table data
for row_data in table_data:
    print(row_data)
driver.switch_to.default_content()

driver.quit()