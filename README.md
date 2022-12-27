# martin-tweepy
This repository uses the Twitter API and tweepy to scrape tweets and store related information in a csv file.

## Eventual Goal
Turn scripts into an executable application to make the process simpler for researchers.  
Must be able to search within a given date range and given query.  
Data stored should have geo tag data any hastags, and basic statistics on tweets. 
Perfrom sentiment analysis on the data pulled.  

## Script Descriptions
```
scrape.py
```
The main Twitter API interface, uses tweepy to pull basic tweet infromation given a query.
```
scrape_app.py
```
The main GUI, uses PySimpleGui to create a basic interface that allows the user to use scrape.py.

## Extra Resources
Project and work this is based off of: https://github.com/jfmalloy1/AcademicTwitter  
PySimpleGUI: https://www.pysimplegui.org/en/latest/readme/
