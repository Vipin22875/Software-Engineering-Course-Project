from os.path import exists
import os
from colorama import *
import colorama
import datetime
from datetime import date
from datetime import datetime

details = ['ID','Name', 'Age', 'Gender','Date of Joining', 'Designation', 'Phone','Salary']
detailsType = ['num','str','num','str','date','str','num','num']
validLength = { "Phone":10,"Salary":[999,9999999]}

error = {}
def open_file(filename,mode):
    if exists(filename):
        fp = open(filename,mode)
        return fp
    else:  
        print("File doesn't exist")
        error.update({'NoFile':"NotFound"})
        return None


def check_salary(salary):
	if int(salary) > validLength['Salary'][0] or int(salary) < validLength['Salary'][1]:
		return True
	else:
		return False

def validate(date_string):
    format = "%Y-%m-%d"
    try:
        res = bool(datetime.strptime(date_string, format))
    except ValueError:
        res = False
    return res

def show_error(filename):

	fp = open_file(filename,'r')

	lines = fp.readlines()
	# print(lines)
	#print(lines)
	count = 0
	for line in lines:
		#print(line)
		dataStaff = line.split(',')
		for i,l in enumerate(details):
			if l == 'Phone':
				if len(dataStaff[i]) != validLength[l]:
					entry = ("At entry "+str(count+1))
					error.update({entry:'Valid Length Error ' + details[i] + " "})

			if l == 'Salary':
				if check_salary(dataStaff[i]):
					entry = ("At entry "+str(count+1))
					error.update({entry:'Valid Salary Error ' + details[i] + " "})

			if l == 'Gender':
				if dataStaff[i] == "M" or dataStaff[i] == "F":
					entry = ("At entry " + str(count+1))
					error.update({entry:"Vaccine Information Error"})
					
		count +=1
	for i in error:
		print(i," : ",error[i])

	return

def check(filename):
	fp = open_file(filename,'r')
	lines = fp.readlines()
	# print(len(details))
	# print(len(detailsType))
	for line in lines:
		line = line.split(',')

		# print(details)
		# print(line)
		# print(len(line))
		print("******************")
		print("Checking validty of entries of Patient : ",line[0])
		for i,entry in enumerate(line):
			if detailsType[i] == 'str':
				entry = entry.strip('\n')
				if entry.isalpha():
					ok = 1
				else:
					ok = 0
			if detailsType[i] == 'num':
				if entry.isnumeric():
					ok = 1
				else:
					ok = 0

			if details[i] == 'Gender':
				if line[i] == "M" or line[i] == "F":
					ok = 1
				else:
					ok = 0
					
			if details[i] == 'Date of Joining':
				if validate(line[i]):
					ok = 1
				else :
					ok = 0		
			if details[i] == 'Destination':
				if line[i] == "D" or line[i] == "N":
					ok = 1
				else:
					ok = 0
			if details[i] == 'Salary':
				if check_salary(line[i]):
					ok = 1
				else:
					ok = 0
					
			if ok == 1:
				print("\033[0;32m")
				print("Passed : OK")
			else:
				print("\033[0;31m")
				print("Failed : PLEASE CHECK THE " +details[i].upper())
		if ok:
			print("\033[0;32m")
			print(colorama.Back.WHITE + "All clear"+Style.RESET_ALL)
		else:
			print("\033[0;31m")
			print(colorama.Back.WHITE + "Not clear"+Style.RESET_ALL)


if __name__== "__main__":
    filename = 'staff.txt'
    while True:
        print(Style.RESET_ALL)
        choice = int(input("Enter: "))
        if choice == 1:
            show_error(filename)
        elif choice == 2:
            check(filename)
        else:
            break