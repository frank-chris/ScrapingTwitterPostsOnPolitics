# ScrapingTwitterPostsOnPolitics
Scraping Twitter posts on Indian politics. An assignment for CS 613 (Natural Language Processing) course at IIT Gandhinagar


## Assignment Statement

[File](https://drive.google.com/file/d/1mAlWNu8RjaaUHk1ZBU0jjvs78WLCW2r4/view)

## Twint

[GitHub](https://github.com/twintproject/twint)     
[Wiki-Basic Usage](https://github.com/twintproject/twint/wiki/Basic-usage)

When installing Twint, don't use the commands given on their README. They are broken. I found this from an issue (use this command to install Twint):

```sh
pip3 install --user --upgrade git+https://github.com/twintproject/twint.git#egg=twint
```
It works correctly.

But you'll have to add it to PATH to use the CLI version.

## Subtopics 
   
First priority:   

1. Pegasus snooping - Amey
2. Farmer agitation/protest - Chris
3. Bengal election 2021 - Glint
4. Farm laws - Amey
  
Then:    
   
6. Education policy 
7. Tamil Nadu election 2021 
8. Assam election 2021 
9. CAA protest 
10. NRC protest 
11. Kerala election 2021 
12. Union budget 2021 
13. Freedom of Religion Act 
14. Lakshadweep protest 
15. Union ministry reshuffle 


## Command used

```sh
twint -s SEARCH_PHRASE -o OUTPUT_FILE_NAME --csv --hashtags --stats -ho 
```

Example:
```sh
twint -s 'pegasus snooping' -o 'pegasus_snooping.csv' --csv --hashtags --stats -ho
```

After this, we have to create and run a script on the generated csv files to get replies to these tweets. We also need to then remove duplicates and create 1 csv file per subtopic.

## Search phrases

| Sub topic                | List of `SEARCH_PHRASE`s |
|--------------------------|--------------------------|
| Pegasus snooping         |'pegasus snooping', |
| Farmer agitation         |'farmer agitation',|
| Bengal Election 2021     |'bengal election 2021',|
| Farm laws                |'farm laws',|
| Education policy         |'education policy',|
| Tamil Nadu Election 2021 |'tamil nadu election 2021',|
| Assam election 2021      |'assam election 2021',|
| CAA protest              |'CAA protest',|
| NRC protest              |'NRC protest',|
| Kerala election 2021     |'kerala election 2021',|
| Union budget 2021        |'union budget 2021',|
| Freedom of Religion Act  |'freedom of religion act',|
| Lakshadweep protest      |'lakshadweep protest',|
| Union Ministry Reshuffle |'union ministry reshuffle',|
