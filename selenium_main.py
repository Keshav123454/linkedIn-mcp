from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

load_dotenv()
driver = webdriver.Chrome()

try:
    LINKEDIN_URL = os.getenv("LINKEDIN_URL")
    PHONE_NO = os.getenv("PHONE_NO")
    PASSWORD = os.getenv("PASSWORD")
    
    driver.get(LINKEDIN_URL)

    wait = WebDriverWait(driver, 10)
    
    email_field = wait.until(EC.element_to_be_clickable((By.ID, "username")))
    email_field.clear()  
    email_field.send_keys(PHONE_NO)

    password_field = wait.until(EC.element_to_be_clickable((By.ID, "password")))
    password_field.clear()
    password_field.send_keys(PASSWORD)

    sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    sign_in_button.click()
    import time
    time.sleep(20)

finally:
    driver.quit()
