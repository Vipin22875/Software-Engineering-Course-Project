#create student information form, store STAFF information in file
#and also display the information from the file
import datetime
from datetime import date
from datetime import datetime

def id(sid):
	fp.write(sid + ",")
	return


def name(sname):
	fp.write(sname + ",")
	return

def age(sage):
	fp.write(sage + ",")
	return

def gender(sgender):
	fp.write(sgender + ",")
	return
	
def date(sdate):
	fp.write(sdate + ",")
	return
	
def designation(sdesignation):
	fp.write(sdesignation + ",")
	return

def phone(sphone):
    fp.write(sphone + ",")
    # fp.write("\n")
    return

def salary(ssalary):
	fp.write(ssalary + ",")
	return

def empty(sempty):
	fp.write(" ")
	fp.write("\n")
	return
 
'''def validate(date_string):
	#date_string = '12-25-2018'
	format = "%Y-%m-d"
	try:
		datetime.datetime.strptime(date_string, format)
		print("This is the correct date string format.")
	except ValueError:
		print("This is the incorrect date string format. It should be YYYY-MM-DD")'''
		     
def validate(date_string):
	format = "%Y-%m-%d"
	try:
		res = bool(datetime.strptime(date_string, format))
	except ValueError:
		res = False
	return res
	
	
while True:
	print("\n")
	print("1.Add new information")
	print("2.Display infomation from the file")
	print("3.TEST CASE CHECK ")
	print("4.Exit")
	print("\n")
	choice = int(input("Enter our choice : "))
	
	if(choice == 1):
		# filename = input("Enter the name of the file: ")
		fp = open("staff.csv","a")
		
		sid = input("Enter staff id: ")
		id(sid)
				
		sname = input("Enter Name: ")
		name(sname)

		sage = input("Enter Age: ")
		age(sage)

		sgender = input("Enter Gender(M/F): ")
		gender(sgender)

		sdate = input("Enter date of joining (YYYY-MM-DD): ")
		date(sdate)

		sdesignation = input("Enter designation(D/N): ")
		designation(sdesignation)

		sphone = input("Enter phone no: ")
		phone(sphone)

		ssalary = input("Enter the salary: ")
		salary(ssalary)
		
		sempty = input("Press something")
		empty(sempty)

		fp.close()
		
	elif(choice == 2):
		# filename2 = input("Enter the name of the file to read information: ")
		print("\n")
		try:
			fp2 = open("staff.csv","r")
			print(fp2.read())
			print("\n")
			fp2.close()
		except FileNotFoundError:
			print("Oops there is no file named : ","staff.csv")
					
	elif(choice == 3):
		# filename3 = input("Enter the name of the file where you stored the INFO: ")
		print("\n")
		print("-----------------")
		print("TEST CASE CHECK RESULT")
		fp3 = open("staff.csv","r")
		lines=fp3.readlines()
		print(lines)
		# a1 = 1
		#print(line)
		for line in lines:
			print(line)
			line = line.split(",")
			print(line)
			# print(a1)
			#print(len(line))
			if (line[0]).isnumeric() :
				print("\033[0;32m")
				print("Passed : OK")
				a1 = -1
			else:
				print("\033[0;31m")
				print("Failed : PLEASE CHECK THE ID ")
				a1 = 0
			if type(line[1])==str:
				print("\033[0;32m")
				print("Passed : OK")
				a2 = -1
			else:
				print("\033[0;31m")
				print("Failed : PLEASE CHECK THE NAME ")
				a2 = 1
			"""
			for i in line[2]:
				if (ord(i)>47) and (ord(i)<58):
					ok = 0
				else:
					ok = 1
			if ok == 0:
				print("\033[0;32m")
				print("Passed : OK")
				a3 = -1
			"""
			if (line[2]).isnumeric():
				print("\033[0;32m")
				print("Passed : OK")
				a3 = -1
			else:
				print("\033[0;31m")
				print("Failed : PLEASE CHECK THE AGE ")
				a3 = 2
			if line[3]=="M" or line[3]=="F" :
				print("\033[0;32m")
				print("Passed : OK")
				a4 = -1
			else:
				print("\033[0;31m")
				print("Failed : PLEASE CHECK THE GENDER ")
				a4 = 3
			# print(line[4])
			if validate(line[4]) :
				print("\033[0;32m")
				print("Passed : OK")
				a5 = -1
			else:
				print("\033[0;31m")
				print("Failed : PLEASE CHECK THE DATE ")
				a5 = 4
			if line[5]=="D" or line[5]=="N":
				print("\033[0;32m")
				print("Passed : OK")
				a6 = -1
			else:
				print("\033[0;31m")
				print("Failed : PLEASE CHECK THE DESIGNATION ")
				a6 = 5
			if (len(line[6]))==10 :
				print("\033[0;32m")
				print("Passed : OK")
				a7 = -1
			else:
				print("\033[0;31m")
				print("Failed : PLEASE CHECK THE NUMBER ")
				a7 = 6
			if line[7].isnumeric() :
				print("\033[0;32m")
				print("Passed : OK")
				a8 = -1
			else:
				print("\033[0;31m")
				print("Failed : PLEASE CHECK THE SALARY ")
				a8 = 7
			print("----------------")

			print("\033[0;37m")
			#updating code
			if a1 == -1:
				pass
			else:
				id = input("Enter the ID again : ")
				line[a1] = id
			if a2 == -1:
				pass
			else:
				name = input("Enter the name again : ")
				line[a2] = name
			if a3 == -1:
				pass
			else:
				age = input("Enter the age again : ")
				line[a3] = age
				print(line[a3])
				# break
			if a4 == -1:
				pass
			else:
				gender = input("Enter the gender again : ")
				line[a4] = gender
			if a5 == -1:
				pass
			else:
				date = input("Enter the joining date again : ")
				line[a5] = date
			if a6 == -1:
				pass
			else:
				designation = input("Enter the designation again : ")
				line[a6] = designation
			if a7 == -1:
				pass
			else:
				phone = input("Enter the phone no. again : ")
				line[a7] = phone
			if a8 == -1:
				pass
			else:
				salary = input("Enter the salary again : ")
				line[a8] = salary
			#print(line[7])
			print("\033[0;37m")
			# a1 += 1
		fp3.close()
		
		
		
		
	elif(choice ==4):
		exit(1)
	else:	
		print("\nOops incorrect choice!")
		print("Try again\n")


		
