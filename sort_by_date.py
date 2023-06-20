import os
import shutil
from datetime import datetime



def sort_by_date(path):
    files = os.listdir(path) #List the files in the directory
    for file in files: #Walk over the files in the directory
        source = os.path.join(path, file)
        if os.path.isfile(source):  # Check if there is a directory with that name already
            timestamp = os.path.getmtime(source) #Get the Last date of modification
            modified_date = datetime.fromtimestamp(timestamp) #Convert the timestamp into object named datetime
            year = str(modified_date.year)# Takes the year from the datetime object
            month = modified_date.strftime("%B") # Takes the month from the datetime object

            year_directory = os.path.join(path, year) #Create the destination directory path for the year
            if not os.path.exists(year_directory): #Checks if there is a directory for that year already
                os.makedirs(year_directory) #If there is not already directory for this year, creates one
                print(f"{year_directory} directory has been created")#Print the name of the new directory
        
        #Again, same pattern but for months

            month_directory = os.path.join(year_directory, month) 
            if not os.path.exists(month_directory):
                os.makedirs(month_directory)
                print(f"{month_directory} directory has been created")

            destination = os.path.join(month_directory, file) #Create final destoination path for the file
            shutil.move(source, destination) #Move that file to that destionation 
        
path = input("Enter Path: ") #Ask user for path
sort_by_date(path)