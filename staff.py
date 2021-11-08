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

# error = []
error = {}

def info(fp):
	for i in details:
		data = input("Enter "+ i + " :")

		# if (i == "Contact no" or i == "ID" or i == "DIV"):
		# 	while (len(data) != validLength[i] and len(data) != 0):
		# 		data = input("Enter valid "+ i + " :")
		fp.write(data + ",")
	fp.write("\n")
	return

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
					error.update({entry:'Valid Length Error ' + details[i] + " " + str(i)})

			if l == 'Salary':
				if check_salary(dataStaff[i]):
					entry = ("At entry "+str(count+1))
					error.update({entry:'Valid Salary Error ' + details[i] + " " + str(i)})

			if l == 'Gender':
				if dataStaff[i] == "M" or dataStaff[i] == "F":
					entry = ("At entry " + str(count+1))
					error.update({entry:"Vaccine Information Error " + str(i) })
					
		count +=1
	for i in error:
		print(i," : ",error[i])

	return error

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

def update_error(error,filename):
	fp = open_file(filename,'r')
	lines = fp.readlines()
	fp.close()
	error_lines = error.keys()
	error_value = [i for error[i] in error_lines]
	error_lines = [int(i[-1]) for i in error_lines]
	error_value = [int(i[-1]) for i in error_value]
	print(error_lines)
	fp = open_file(filename,'w')
	for j in error_lines:
		print(j)
		for i in range(len(lines)):
			if j-1 == i:
				info(fp)
				i = i + 1
			else:
				fp.write(lines[i])
	fp.close()
	pass

if __name__== "__main__":
	filename = 'staff.txt'
	while True:
		print(Style.RESET_ALL)
		print(" 1. Overview of all errors")
		print(" 2. Check for error line by line")
		choice = int(input("Enter: "))
		if choice == 1:
			error_dict = show_error(filename)
		elif choice == 2:
			check(filename)
		elif choice == 3:
				print(error_dict)
				update_error(error_dict,filename)
		else:
			print("Exit")
			break