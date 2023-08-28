from flask import Flask, request
from rest_app import get_user
import os
import signal
app = Flask(__name__)

@app.route("/test")
def test():
	return 'Test OK', 200 # status code

@app.route("/stop_server")
def stop():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return "Server stopped"

@app.route('/users/get_user_data/<user_id>') #http://127.0.0.1:5001/users/get_user_data/1
def get_user_data(user_id):
	try:
		user = get_user(user_id)
		if user != "":
			if not user.startswith("Error"):
				data_return = f"<h1 id='user'>{user}</h1>",200
			else:
				data_return = f"<h1 id='error'>{user}</h1>",200
		else:
				data_return = f"<h1 id='error'>User {user} not found</h1>",200
	except Exception as e:
		data_return = f"<h1 id='error'>An exception has occurred. {str(e)}</h1>",500
		raise Exception(str(e))

	return data_return

if __name__ == "__main__":
	app.run(host='127.0.0.1', debug=True, port=5001)