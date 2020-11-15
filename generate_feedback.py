from bs4 import BeautifulSoup
import os
import csv

with open('grades.csv', mode='w') as grades_file:
    writer = csv.writer(grades_file)
    writer.writerow(["Student Id", "Grade", "Feedback"])

    currentPath =os.getcwd()
    dirs = next(os.walk(currentPath))[1]

    hwPaths = []

    print("ًWorking on it ..." )

    homeWorkName ="Homework 2"
    for dir in dirs:
        hwPaths.append(dir + "/" +homeWorkName )
    

    feedbackFileName = "HW2.html"
    for hwPath in hwPaths:
        with open( hwPath + "/" + feedbackFileName) as fp:
            soup = BeautifulSoup(fp, 'html.parser')
    
        listOfIndexes = []
        i = 0;

        strippedStrings =soup.stripped_strings
        strippedStringsList= list(strippedStrings)
        for string in strippedStringsList:
            if(string == "Comments:"):
                listOfIndexes.append(i)
            i= i + 1

        feedback =""
        for index in listOfIndexes:
            feedback = feedback +  strippedStringsList[index + 1] + "\n"
        writer.writerow([hwPath[0:10],soup.h4.string,feedback])

print("Done ;) run 'open grades.csv' to see the files" )
