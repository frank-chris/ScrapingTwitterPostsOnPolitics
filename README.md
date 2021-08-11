# ScrapingTwitterPostsOnPolitics
Scraping Twitter posts on Indian politics. An assignment for CS 613 (Natural Language Processing) course at IIT Gandhinagar


## Assignment Statement

[File](https://drive.google.com/file/d/1mAlWNu8RjaaUHk1ZBU0jjvs78WLCW2r4/view)

## Twint

[GitHub](https://github.com/twintproject/twint)

When installing Twint, don't use the commands given on their README. They are broken. I found this from an issue (use this command to install Twint):

```sh
pip3 install --user --upgrade git+https://github.com/twintproject/twint.git#egg=twint
```
It works correctly.

But you'll have to add it to PATH to use the CLI version.

## Subtopics 

1. Pegasus snooping - Amey
2. Farmer agitation/protest - Amey
3. Bengal election 2021 - Amey
4. Farm laws - Amey
5. Education policy - Amey
6. Tamil Nadu election 2021 - Chris
7. Assam election 2021 - Chris
8. CAA protest - Chris
9. NRC protest - Chris
10. Kerala election 2021 - Chris
11. Union budget 2021 - Glint
12. Freedom of Religion Act - Glint
13. Lakshadweep protest - Glint
14. Union ministry reshuffle - Glint
(if we have any more ideas - Glint)

## Command used

```sh
twint -s SEARCH_PHRASE -o OUTPUT_FILE_NAME --csv --hashtags --stats --get-replies 
```

Example:
```sh
twint -s 'pegasus snooping' -o 'pegasus_snooping.csv' --csv --hashtags --stats --get-replies 
```

## Search phrases

(TBD)
