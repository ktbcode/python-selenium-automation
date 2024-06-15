from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.target.com/')
driver.find_element(By.XPATH, "//span[@class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']").click()

driver.find_element(By.XPATH, "//span[@class='sc-859e7637-0 hHZPQy']").click()
sleep(3)
# Verification
# Check if text is there
header = driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
assert "Sign into your Target account" in header, f"Error! text in the header is not 'Sign into your Target account'"

# Check if LogIn button is there
driver.find_element(By.ID, 'login')
print("SignIn page is opened")
driver.quit()