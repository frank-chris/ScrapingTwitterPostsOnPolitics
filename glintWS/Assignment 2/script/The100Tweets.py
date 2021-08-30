import json
import twint
import os
import re

# Python3 program to count words
# in a given string
OUT = 0
IN = 1
 
# Returns number of words in string
def countWords(string):
    state = OUT
    wc = 0
 
    # Scan all characters one by one
    for i in range(len(string)):
 
        # If next character is a separator,
        # set the state as OUT
        if (string[i] == ' ' or string[i] == '\n' or
            string[i] == '\t'):
            state = OUT
 
        # If next character is not a word
        # separator and state is OUT, then
        # set the state as IN and increment
        # word count
        elif state == OUT:
            state = IN
            wc += 1
 
    # Return the number of words
    return wc
 

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

    itVariable = 0
    for dataPoint in data:
        if itVariable > 110:
            break

        if countWords(dataPoint["tweet"]) - (len(dataPoint["hashtags"]) + len(dataPoint["mentions"])) > 5 :
            print(dataPoint["id"],end="\t")
            print(re.sub(r'(\s)@\w*', r'\1', re.sub(r'(\s)#\w*', r'\1', dataPoint["tweet"])), end="\t")
            print(dataPoint["language"])
            itVariable = itVariable + 1

            
        
        # if itVariable == 0:
        # print(dataPoint.keys())
        #     print(dataPoint)
        
        # print("\n\nNext Tweet:")
        # print(dataPoint["tweet"])
        # print(dataPoint["mentions"])
        # print(dataPoint["hashtags"])
        # print(dataPoint["urls"])


        # print(len(dataPoint["hashtags"]),end="\t")
        # print(len(dataPoint["mentions"]),end="\t")
        # print(countWords(dataPoint["tweet"]),end="\t")
        # print(dataPoint["language"])

        # itVariable = itVariable + 1



        



    # for dataPoint in data:
    #     # print(dataPoint["hashtags"])
    #     y=dataPoint[jsonIndexToOutput]

    #     if mode == 2:
    #         for yy in y:
    #             if printIndividualItems == True :
    #                 print(yy)
    #             mySet.add(yy)
    #     if mode == 1:
    #         if printIndividualItems == True :
    #             print(y)
    #         mySet.add(y)
    # print(mySet)
    
main()
