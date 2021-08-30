import json
import twint
import os


def main():
    findReplies()

def findReplies():
    #find replies for tweets in this file
    dataFileName = "BengalElection2021.csv"

    #store tweets that needs to be filtered for conversation in this file
    tempDataFileName = "./temp.csv"

    #store the reply tweets in this file..careful this appends the file
    replyFileName ="BengalElection2021Replies.csv"

    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    data = []
    replies = []
    replyFile = open(replyFileName,"a")
    with open (dataFileName) as f:
        for line in f:
            data.append(json.loads(line))
    for dataPoint in data:
        if dataPoint["replies_count"] > 0 :
            print(dataPoint["replies_count"])
            print(dataPoint["username"])
            userName=dataPoint["username"]
            #getting the data associated with each user
            c = twint.Config()
            query="to:@"+userName
            print(query)
            c.Search = query
            c.Output = "temp.csv"
            c.Limit = 1000
            c.Hide_output = True
            c.Store_json = True
            c.Stats = True
            c.Since = dataPoint["date"]
            twint.run.Search(c)
            #hopefully have all the tweets to this guy
            
            tempData = []
            with open (tempDataFileName) as f:
                for line in f:
                    tempData.append(json.loads(line))
            
            #now let's find all the replies.
            for tempDataPoint in tempData:
                if tempDataPoint["conversation_id"] == dataPoint["conversation_id"]:
                    replies.append(tempDataPoint)
                    replyFile.write(json.dumps(tempDataPoint))
                    replyFile.write("\n")
                    print(tempDataPoint)                    
            #lets get ride of the temp file
            os.remove(tempDataFileName)
    replyFile.close()

main()
