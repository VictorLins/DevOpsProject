import requests

try:
    requests.get("http://127.0.0.1:5000/stop_server")
except Exception as e:
    print("[ clean_environment // stop 5000] ** EXCEPTION ** - " + str(e))

try:
    requests.get("http://127.0.0.1:5001/stop_server")
except Exception as e:
    print("[ clean_environment // stop 5001] ** EXCEPTION ** - " + str(e))
    raise Exception(str(e))