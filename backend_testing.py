import requests
import random

user_id = random.randint(0,999) #Generate random User Id
user_name = "User " + str(user_id) #Define User Name
post_response = requests.post(f"http://127.0.0.1:5000/users/{user_id}", json={"user_name": f"{user_name}"})
if post_response.ok:
    print("Response OK: " + str(post_response.json()))
else:
    print("Response NOK: " + str(post_response.json()))

get_response = requests.get(f"http://127.0.0.1:5000/users/{user_id}")
if get_response.ok:
    response_json = get_response.json()
    if response_json['user_name'] == user_name:
    	print(f"User {response_json['user_name']} added successfully")