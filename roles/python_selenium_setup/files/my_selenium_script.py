from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  # Ensure you import By

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service('/usr/local/bin/chromedriver/chromedriver-linux64/chromedriver')

try:
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get('https://www.w3schools.com')  # Replace with your URL

    # Correct method name: find_element
    element = driver.find_element(By.XPATH, '//*[@id="navbtn_services"]')
    print(f"Element text: {element.text}")
    driver.find_element(By.XPATH, '//*[@id="navbtn_services"]').click()
    dhoni=driver.find_element(By.XPATH, '//*[@id="services_list"]/div[1]/div[1]/h2/b').text
    print(dhoni)

finally:
    try:
        driver.quit()
    except NameError:
        print("Driver was not initialized.")
