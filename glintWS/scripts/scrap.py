import twint

def main():
    scrap()

def scrap():
    #query to search
    searchQuery="BengalElection2021"
    #output file name
    tweetOutputFileName = "BengalElection2021.csv"
    #meta data file name
    searchIDResumeFile = "my_search_id_.txt"


    #++++++++++++++++++++++++++++++++++++++++++++++
    c = twint.Config()
    c.Search = searchQuery
    c.Output = tweetOutputFileName
    c.Limit = 10000
    c.Hide_output = True
    c.Resume = searchIDResumeFile
    c.Store_json = True
    c.Stats = True
    twint.run.Search(c)

main()