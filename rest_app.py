from flask import Flask, request
from db_connector import get_user, update_user, add_user, delete_user
app = Flask(__name__)

@app.route("/test")
def test():
    return 'Test OK', 200 # status code

@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    try:
        # Returns the user name stored in the database for a given user id
        if request.method == 'GET':
            user = get_user(user_id)
            if user != "":
                if not user.startswith("Error"):
                    data_return = {"status": "ok", "user_name": user}, 200
                else:
                    data_return = {"status": "error", "message": user}, 500
            else:
                data_return = {"status": "error", "message": "User not found"}, 500

        # A new user will be created in the database
        elif request.method == 'POST':
            request_data = request.json  # getting the json data payload from request
            # treating request_data as a dictionary to get a specific value from key
            user_name = request_data.get('user_name')
            user = add_user(user_name, user_id)
            if user != "":
                if not user.startswith("Error"):
                    data_return = {"status": "ok", "user_added": user}, 200
                else:
                    data_return = {"status": "error", "reason": user}, 500

        # Will modify existing user name (in the database)
        elif request.method == 'PUT':
            request_data = request.json # getting the json data payload from request
            # treating request_data as a dictionary to get a specific value from key
            user_name = request_data.get('user_name')
            user = update_user(user_name, user_id)
            if user != "":
                if not user.startswith("Error"):
                    data_return = {"status": "ok", "user_name": user}, 200
                else:
                    data_return = {"status": "error", "reason": user}, 500

        # Will delete existing user (from database)
        elif request.method == 'DELETE':
            user = delete_user(user_id)
            if user != "":
                if not user.startswith("Error"):
                    data_return = {"status": "ok", "user_deleted": user_id}, 200
                else:
                    data_return = {"status": "error", "reason": user}, 500
    except Exception as e:
        data_return = {"status": "error", "reason": str(e)}, 500

    return data_return

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True, port=5000)