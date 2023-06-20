import os
import shutil


def sort_by_type(path):
    files = os.listdir(path) #get list of files in the directory 
    for file in files: #for function that walks over every file 
        filename, extension = os.path.splitext(file)
        extension  = extension[1:]

        if os.path.isdir(path+'/'+extension): #check if there is already directory for that extension 
            shutil.move(path+'/'+file, path+'/'+extension+'/'+file) #if yes moves this file into that directory
        else:
            os.makedirs(path+'/'+extension) #if not, creates directory 
            print(f"{extension} directory has been created")#Print the name of the new directory
            shutil.move(path+'/'+file, path+'/'+extension+'/'+file) #after making the new directory moves the file to that directory 

path = input("Enter Path: ") #Ask user for path 
sort_by_type(path)
