

def name(pname):
	fp.write(pname + ",")
	return

def age(page):
	fp.write(page + ",")
	return

def gender(pgender):
	fp.write(pgender + ",")
	return
	
def phone(pphone):
	fp.write(pphone + ",")
	return
	
def bloodgroup(pbloodgroup):
	fp.write(pbloodgroup + ",")
	return

def sugar(psugar):
	fp.write(psugar + ",")
	return

def bloodpressure(pbloodpressure):
	fp.write(pbloodpressure + ",")
	return

def vaccine(pvaccine):
	fp.write(pvaccine + ",")
	return

def vaccinename(pvaccinename):
	fp.write(pvaccinename)
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
		
		pname = input("Enter patient name: ") 
		name(pname)
		
		page = input("Enter age: ")
		age(page)

		pgender = input("Enter gender(M/F): ")
		gender(pgender)

		pphone = input("Enter phone no: ")
		phone(pphone)

		pbloodgroup = input("Enter blood group(A/B/AB/O): ")
		bloodgroup(pbloodgroup)

		psugar = input("Enter sugar(Y/N): ")
		sugar(psugar)

		pbloodpressure = input("Enter bloodpressure: ")
		bloodpressure(pbloodpressure)

		pvaccine = input("Enter vaccine(0/1/2): ")
		vaccine(pvaccine)

		pvaccinename = input("Enter vaccine name: ")
		vaccinename(pvaccinename)
		
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
		
