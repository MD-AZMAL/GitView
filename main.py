from script import * # import User class
import requests

usr_name = input('Enter the User Name : ')

resp = requests.get('https://github.com/'+usr_name)

if resp.status_code != 200: # check if user account exists
	print("No such user") 
else:
	newusr = User(usr_name)
	newusr.user_details()
	newusr.user_repos() 
