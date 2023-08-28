import pymysql
import requests
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# ------------------
# WEB API TEST
# ------------------
try:
    user_id = random.randint(0, 999) #Generate random User Id
    user_name = "User " + str(user_id)  #Define User Name
    requests.post(f"http://127.0.0.1:5000/users/{user_id}", json={"user_name": f"{user_name}"}) #Add user
    get_response = requests.get(f"http://127.0.0.1:5000/users/{user_id}")
    if get_response.ok and get_response.json()['user_name'] == user_name:
        print(f"API TEST: Test Successful | User {user_name} added.")
    else:
       raise Exception("API Test failed")
except Exception as e:
    print(str(e))

# ------------------
# MYSQL TEST
# ------------------
try:
    connection_string_host = '127.0.0.1'
    connection_string_port = 3306
    connection_string_user = 'sandbox_user'
    connection_string_password = 'DefaultPassword123'
    connection_string_schema = "mydb"

    conn = pymysql.connect(host=connection_string_host, port=connection_string_port, user=connection_string_user,passwd=connection_string_password, db=connection_string_schema)
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {connection_string_schema}.users where id = {user_id}")
    for row in cursor:
        if row[0] == user_id and str(row[1]) == user_name:
            print(f"MYSQL TEST: Test Successful | User: {str(row[1])}")
        else:
            raise Exception(f"MySQL Test failed - User Not Found")
    cursor.close()
    conn.close()
except Exception as e:
    print(str(e))

# ------------------
# SELENIUM TEST
# ------------------
driver = webdriver.Chrome(service=Service())
try:
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(f"http://127.0.0.1:5001/users/get_user_data/{user_id}")
    user_field = driver.find_elements(By.ID, "user")
    if len(user_field) == 0:
        print("Field not found")
        raise Exception(f"Selenium Test failed - Field Not Found")
    else:
        print("SELENIUM TEST: Test Successful | Field Found. Value: ", user_field[0].text)
except Exception as e:
    print(str(e))
