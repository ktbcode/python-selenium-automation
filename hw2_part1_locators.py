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

driver.get('https://www.amazon.com')
driver.find_element(By.XPATH, "//a[@data-nav-role='signin']").click()
sleep(3)

# Amazon Logo
if driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']"):
    print("Found Amazon logo")

# Email field
if driver.find_element(By.ID, 'ap_email'):
    print("Found email field")

# Continue button
if driver.find_element(By.XPATH, "//input[@aria-labelledby='continue-announce']"):
    print("Found continue button")
# Conditions of use link
if driver.find_element(By.XPATH, "//a[contains(@href,'ap_signin_notification_condition_of_use')]"):
    driver.find_element(By.XPATH, "//a[contains(@href,'ap_signin_notification_condition_of_use')]").click()
    print("Found Conditions of Use link")
    driver.back()
# Privacy Notice link
if driver.find_element(By.XPATH, "//a[contains(@href,'ap_signin_notification_privacy_notice')]"):
    driver.find_element(By.XPATH, "//a[contains(@href,'ap_signin_notification_privacy_notice')]").click()
    print("Found privacy notice link")
    driver.back()
    sleep(3)
# Need help link
if driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']"):
    driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']").click()
    print("Found need help link ")
    sleep(3)
# Forgot your password link
if driver.find_element(By.ID, 'auth-fpp-link-bottom'):
    print("Found forgot password link")
# Other issues with Sign-In link
if driver.find_element(By.ID, 'ap-other-signin-issues-link'):
    print("Found other issues link")
# Create your Amazon account button
if driver.find_element(By.ID, 'createAccountSubmit'):
    driver.find_element(By.ID, 'createAccountSubmit').click()
    print("Found create amazon account button")
    sleep(5)



