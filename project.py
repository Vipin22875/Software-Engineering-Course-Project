from os.path import exists
import os
from colorama import *
import colorama

details = ['Name', 'Age', 'Gender','Phone', 'Bloodgroup', 'Sugar','BloodPressure','Vaccine','VaccineName']
detailsType = ['str','num','str','num','str','str','num','num','str']
validLength = { "Phone":10,"Vaccine":1}

error = {}
def open_file(filename,mode):
    if exists(filename):
        fp = open(filename,mode)
        return fp
    else:  
        print("File doesn't exist")
        error.update({'NoFile':"NotFound"})
        return None

def show_error(filename):

    fp = open_file(filename,'r')

    lines = fp.readlines()
    # print(lines)
    #print(lines)
    count = 0
    for line in lines:
        #print(line)
        dataStudent = line.split(',')
        for i,l in enumerate(details):
            if l == 'Phone' or l == 'Vaccine':
                if len(dataStudent[i]) != validLength[l]:
                    entry = ("At entry "+str(count+1))
                    error.update({entry:'Valid Length Error ' + details[i] + " "})
            
            if l == 'Vaccine' and dataStudent[i] == '0':
                if dataStudent[i+1] != "NA":
                    entry = ("At entry " + str(count+1))
                    error.update({entry:"Vaccine Information Error"})
        count +=1

    for i in error:
        print(i," : ",error[i])

def check(filename):
    fp = open_file(filename,'r')
    lines = fp.readlines()
    # print(len(details))
    # print(len(detailsType))
    for line in lines:
        line = line.split(',')
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

            if details[i] == 'Vaccine' and line[i] == '0':
                if line[i+1] == "NA":
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

        
    pass

def update_error(error,filename):
	fp = open_file(filename,'r')
	lines = fp.readlines()
	fp.close()
	lines = error.keys()
	fp = open_file(filename,'w')
	for i,line in enumerate(lines):
		fp.write(line)
	pass

if __name__== "__main__":
    filename = 'patient.txt'
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
            try:
                print(error_dict)
                update_error(error_dict,filename)
            except:
                print("First Find errors")
        else:
            print("Exit")
            break