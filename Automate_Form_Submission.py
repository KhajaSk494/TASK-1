from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Specify the path to the ChromeDriver
driver_path = 'C:\\Users\\khaja\\OneDrive\\Desktop\\WebDrivers\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'

# Set up the Service with the specified ChromeDriver path
service = Service(executable_path=driver_path)

# Set up the WebDriver with the Service
driver = webdriver.Chrome(service=service)

try:
    # Navigate to the Google form
    driver.get('https://forms.gle/m7an6gxdDX6P5BBi7')

    # Wait for the page to load
    time.sleep(10)

    # Fill in the form fields using the provided XPath

    # Full name
    full_name_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
    full_name = driver.find_element(By.XPATH, full_name_xpath)
    full_name.send_keys('Shaik Khaja Mohiddin')

    # Email
    email_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
    email = driver.find_element(By.XPATH, email_xpath)
    email.send_keys('khajashaik4904@gmail.com')

    # Phone number
    phone_number_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
    phone_number = driver.find_element(By.XPATH, phone_number_xpath)
    phone_number.send_keys('7780440264')

    # Qualification
    qualification_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input'
    qualification = driver.find_element(By.XPATH, qualification_xpath)
    qualification.send_keys('Master of Computer Science')

    # Year of passing
    year_of_passing_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input'
    year_of_passing = driver.find_element(By.XPATH, year_of_passing_xpath)
    year_of_passing.send_keys('2023')

    # City
    city_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input'
    city = driver.find_element(By.XPATH, city_xpath)
    city.send_keys('Vijayawada')

    # State
    state_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input'
    state = driver.find_element(By.XPATH, state_xpath)
    state.send_keys('Andhra Pradesh')

    # Wait for some time
    time.sleep(6)

    # Submit the form
    submit_button_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
    submit_button = driver.find_element(By.XPATH, submit_button_xpath)
    submit_button.click()

    # Wait for the form submission to process
    time.sleep(6)

    # Validate the submission
    # Example: Check if a success message is displayed (modify XPath based on actual success message element)
    success_message_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]'
    success_message = driver.find_element(By.XPATH, success_message_xpath)
    assert 'Form Submitted Successfully' in success_message.text

finally:
    # Close the WebDriver
    driver.quit()
