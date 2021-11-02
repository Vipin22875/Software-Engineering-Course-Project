#create student information form, store STAFF information in file
#and also display the information from the file
import datetime
from datetime import date

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
    fp.write(sphone)
    fp.write("\n")
    return
 
def validate(date_string):
	#date_string = '12-25-2018'
	format = "%Y-%m-d"
	try:
		datetime.datetime.strptime(date_string, format)
		print("This is the correct date string format.")
	except ValueError:
		print("This is the incorrect date string format. It should be YYYY-MM-DD")
        

	
	
while True:
	print("\n")
	print("1.Add new information")
	print("2.Display infomation from the file")
	print("3.TEST CASE CHECK ")
	print("4.Exit")
	print("\n")
	choice = int(input("Enter our choice : "))
	
	if(choice == 1):
		filename = input("Enter the name of the file: ")
		fp = open(filename,"a")
		
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
		
		fp.close()
		
	elif(choice == 2):
		filename2 = input("Enter the name of the file to read information: ")
		print("\n")
		try:
			fp2 = open(filename2,"r")
			print(fp2.read())
			print("\n")
			fp2.close()
		except FileNotFoundError:
			print("Oops there is no file named : ",filename2)
					
	elif(choice == 3):
		filename3 = input("Enter the name of the file where you stored the INFO: ")
		print("\n")
		print("-----------------")
		print("TEST CASE CHECK RESULT")
		fp3 = open(filename3,"r")
		line=fp3.read()
		#print(line)
		line =line.split(",")
		#print(len(line))
		if (line[0]).isnumeric() :
			print("OK")
		else:
			print("PLEASE CHECK THE ID ")
		if type(line[1])==str:
			print("OK")
		else:
			print("PLEASE CHECK THE NAME ")
		if (line[2]).isnumeric() :
			print("OK")
		else:
			print("PLEASE CHECK THE AGE ")
		if line[3]=="M" or line[3]=="F" :
			print("OK")
		else:
			print("PLEASE CHECK THE GENDER ")
		if validate(line[4]) :
			print("OK")
		else:
			print("PLEASE CHECK THE DATE ")
		if line[5]=="D" or line[5]=="N"  :
			print("OK")
		else:
			print("PLEASE CHECK THE DESIGNATION ")
		if (len(line[6])-1)==10 :
			print("OK")
		else:
			print("PLEASE CHECK THE NUMBER ")
		print("----------------")
		#print(line[7])
		fp3.close()
		
		
		
		
	elif(choice ==4):
		exit(1)
	else:	
		print("\nOops incorrect choice!")
		print("Try again\n")


		
