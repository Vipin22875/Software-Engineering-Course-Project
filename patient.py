from os.path import exists
import os

details = ['Name', 'Age', 'Gender','Phone', 'Bloodgroup', 'Sugar','BloodPressure','Vaccine','VaccineName']
validLength = { "Phone":10,"Vaccine":1}

error = {}
def menu():
    filename = 'patient.txt'
    if exists(filename):
        fp = open(filename,'r')
        # print("fg")
        # print(fp)
        # print(filename)
    else:  
        print("File doesn't exist")
        error.update({'NoFile':"NotFound"})
        return

    lines = fp.readlines()
    # print(lines)
    count = 0
    for line in lines:
        dataStudent = line.split(',')
        for i,l in enumerate(details):
            if l == 'Phone' or l == 'Vaccine':
                if len(dataStudent[i]) != validLength[l]:
                    entry = ("At entry "+str(count))
                    error.update({entry:'Valid Length Error ' + details[i] + " "})
            if l == 'Vaccine' and dataStudent[i] == '0':
                if dataStudent[i+1] != "NA":
                    entry = ("At entry " + str(count))
                    error.update({entry:"Vaccine Information Error"})
        count +=1

    for i in error:
        print(i," : ",error[i])

if __name__== "__main__":
    menu()