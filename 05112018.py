import time
import json
import datetime
import os

def Activity():
	
	print (datetime.datetime.now())

	myfile = open("questionbank1.txt","r")
	
	abc = {}
	
	for data1 in myfile.read().split("\n"):
		print "Question:",data1
		Answer=raw_input("Ans:")
		abc[data1] = Answer

	return abc
	
def Menu():
	path = "/home/kustarddev/PythonPrograms/SRT/users.json"
	
	print("1.Type q to quit \n")
	print("2.Type w to Wait an hour and come back\n")
	print("3.Type qb to add question bank \n")	

	action = raw_input("action=").lower()

	if(action == "w"):
		while (True):
			time.sleep(2)
			foo = Activity()
			
			with open('Question_Answer_Set.json', 'a') as outfile:  
					json.dump(foo, outfile)
					outfile.write('\n\n')
			Menu()


	elif(action == "qb"):
		
		questions = []

		n = int(raw_input("Enter how many questions you want me to ask: "))
		for i in range(0, n):
			x = raw_input("Ques:")
			questions.append(x)
			s = questions
			
		# password = users.get(username)
			
		with open('users.json', 'a') as outfile:  
					json.dump(s, outfile)
					outfile.write('\n\n')

		
		# with open('/home/kustarddev/PythonPrograms/SRT/users.json', 'r') as fu:
		# 		users = json.load(fu)
		# 		users[Questions] = y  # or whatever
		# with open('/home/kustarddev/PythonPrograms/SRT/users.json', 'w') as fu:
		# 		json.dump(users, fu)

		print("Question bank has been created")


		return questions		

		

	elif(action == "q"):
		exit()
	else:
		print("Please Enter a Correct Command")
		action = raw_input("action> ").lower()


def login():
	
	path = "/home/kustarddev/PythonPrograms/SRT/users.json"
	
	tries = 0

	while tries < 3:
		username = raw_input("Enter your emailid as user name: ")
		password = raw_input("Enter your password: ")

		users = {}
		with open(path) as f:
			json_string = f.read()
			users = json.loads(json_string)
	
		for user in users:
		
			if user['username'] == username and user['password'] == password:
			
				print("Welcome to Self Reflection Tool")
			 	
		break
	# time.sleep(1)
		
	print("Welcome to Self Reflection Tool")
	print(datetime.datetime.now())

	Menu()


def register():
	while True:
		username = raw_input("Enter your emailid: ")
		Firstname = raw_input("Enter your Firstname: ")
		Lastname = raw_input("Enter your Lastname: ")
		if not len(username) > 0:
			print("Username can't be blank")
			continue
		else:
			break

	while True:
		password = raw_input("Enter your Password: ")
		ConfirmPassword = raw_input("Enter your ConfirmPassword: ")
		if not len(password) > 0:
			print("Password can't be blank")
			continue
		else:
			break
	print("Account has been created...")

	print("Please login to add your question bank")


	reg_data = {}
	reg_data["username"] = username

	reg_data["password"] = password
	reg_data["Firstname"] = Firstname
	reg_data["Lastname"] = Lastname
	reg_data["Questions"] = {"Que1": "What productivity?","Que2": "How much water you had?"}
	
	print("Default Questions are as follows: %s" % reg_data["Questions"])

	filename = 'users.json'
	entry = reg_data
	a = []
	feeds = {}
	if not os.path.isfile(filename):
		# entry = reg_data

		a.append(entry)
		with open(filename, mode='a') as f:
			f.write(json.dumps(a, indent=2))
	else:
		with open(filename) as feedsjson:
			feeds = json.load(feedsjson)
			feeds.append(entry)
			with open(filename, mode='w') as f:
				f.write(json.dumps(feeds, indent=2))
	

	
			
	# with open('users.json', 'a') as outfile:  
	# 		json.dump(reg_data, outfile)
	# 		outfile.write('\n\n')

	
	return reg_data	
	

# On start

print("Welcome to the system. Please register or login.")
print("Options: register | login | exit")
while True:
	option = raw_input("> ").lower()
	if (option == "login"):
		login()
	elif (option == "register"):
		register()
	elif (option == "exit"):
		exit()
	else:
		print("You have entered wrong option")

print("Thank you for using Self Reflection Tool...");