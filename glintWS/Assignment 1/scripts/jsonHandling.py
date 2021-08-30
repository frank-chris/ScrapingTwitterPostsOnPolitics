import json
import twint
import os


def main():
    jasonHandling()

def jasonHandling():

    #input data file containing all the stuff
    dataFileName = "BengalElection2021.csv"
    # the dic index to output for each entry
    jsonIndexToOutput = "language"

    #set the mode = 1 or 2 (single data point vs a list)
    mode = 1  

    #some controlls
    printIndividualItems = False
    printUniqueItems = True

    # ************************************************************
    data = []
    mySet = set()
    with open (dataFileName) as f:
        for line in f:
            data.append(json.loads(line))

    for dataPoint in data:
        # print(dataPoint["hashtags"])
        y=dataPoint[jsonIndexToOutput]

        if mode == 2:
            for yy in y:
                if printIndividualItems == True :
                    print(yy)
                mySet.add(yy)
        if mode == 1:
            if printIndividualItems == True :
                print(y)
            mySet.add(y)
    print(mySet)
    
main()
