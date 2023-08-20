import pymysql

connection_string_host = '127.0.0.1'
connection_string_port = 3306
connection_string_user = 'sandbox_user'
connection_string_password = 'DefaultPassword123'
connection_string_schema = "mydb"

#region Getting data from table
def get_user(user_id):
	global connection_string_host
	global connection_string_port
	global connection_string_user
	global connection_string_password
	global connection_string_schema
	data_return = ""
	try:
		conn = pymysql.connect(host=connection_string_host, port=connection_string_port, user=connection_string_user, passwd=connection_string_password,db=connection_string_schema)
		conn.autocommit(True)
		cursor = conn.cursor()
		cursor.execute(f"SELECT * FROM {connection_string_schema}.users where id = {user_id}")
		for row in cursor:
			data_return = str(row[1])
		cursor.close()
		conn.close()
	except Exception as e:
		data_return = "Error | " + str(e)
	return data_return
#endregion

#region Inserting data into table
def add_user(user_name, user_id):
	global connection_string_host
	global connection_string_port
	global connection_string_user
	global connection_string_password
	global connection_string_schema
	data_return = ""
	try:
		print(1)
		user = get_user(user_id)
		if user != "":
			print(2)
			if not user.startswith("Error"):
				print(3)
				data_return = f"Error | Id {user_id} already in use."
			else:
				print(5)
				data_return = user  # If an exception comes from the previous action, it will be sent to the response
		else:
			print(6)
			conn = pymysql.connect(host=connection_string_host, port=connection_string_port, user=connection_string_user, passwd=connection_string_password,db=connection_string_schema)
			conn.autocommit(True)
			cursor = conn.cursor()
			cursor.execute(f"INSERT into {connection_string_schema}.users (name, id) VALUES ('{user_name}', {user_id})")
			data_return = get_user(user_id)
	except Exception as e:
		data_return = "Error | " + str(e)
	return data_return
#endregion

##region Deleting data from table
def delete_user(user_id):
	global connection_string_host
	global connection_string_port
	global connection_string_user
	global connection_string_password
	global connection_string_schema
	data_return = ""
	try:
		user = get_user(user_id)
		if user != "":
			if not user.startswith("Error"):
				conn = pymysql.connect(host=connection_string_host, port=connection_string_port,user=connection_string_user, passwd=connection_string_password,db=connection_string_schema)
				conn.autocommit(True)
				cursor = conn.cursor()
				cursor.execute(f"delete from {connection_string_schema}.users WHERE id = {user_id}")
				data_return = "User deleted"
			else:
				data_return = user  # If an exception comes from the previous action, it will be sent to the response
		else:
			data_return = f"Error | User Id {user_id} not found"
	except Exception as e:
		data_return = "Error | " + str(e)
	return data_return
#endregion

##region Updating data from table
def update_user(user_name, user_id):
	global connection_string_host
	global connection_string_port
	global connection_string_user
	global connection_string_password
	global connection_string_schema
	data_return = ""
	try:
		user = get_user(user_id)
		if user != "":
			if not user.startswith("Error"):
				conn = pymysql.connect(host=connection_string_host, port=connection_string_port,user=connection_string_user, passwd=connection_string_password,db=connection_string_schema)
				conn.autocommit(True)
				cursor = conn.cursor()
				cursor.execute(f"UPDATE {connection_string_schema}.users SET name = '{user_name}' WHERE id = {user_id}")
				data_return = get_user(user_id)
			else:
				data_return = user  # If an exception comes from the previous action, it will be sent to the response
		else:
			data_return = f"Error | User Id {user_id} not found"
	except Exception as e:
		data_return = "Error | " + str(e)
	return data_return
#endregion