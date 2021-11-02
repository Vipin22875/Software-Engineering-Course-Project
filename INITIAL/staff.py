#create student information form, store student information in file
#and also display the information from the file

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

	
	
while True:
	print("\n")
	print("1.Add new information")
	print("2.Display infomation from the file")
	print("3.Exit")
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

		sdate = input("Enter date of joining: ")
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
		exit(1)
	else:
		print("\nOops incorrect choice!")
		print("Try again\n")
		
