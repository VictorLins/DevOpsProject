from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# SET DRIVER
# driver = webdriver.Chrome(service=Service("e:/Not Sync/Study/DevOps Training/Class 3 - 24.07.23/ChromeWebDriver_version114_-chrome-win64/chrome-win64/"))
driver = webdriver.Chrome(service=Service())

try:
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("http://127.0.0.1:5001/users/get_user_data/11") # Open the webpage related to the selected user ID
    user_field = driver.find_elements(By.ID, "user") # Get the field USER
    if len(user_field) == 0:
        print("Field not found")
    else:
        print("Field Found. Value: ", user_field[0].text)
except Exception as e:
    print(str(e))
    raise Exception(str(e))

exit()
