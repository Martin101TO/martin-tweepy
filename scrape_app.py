# Author: Kevin Li
# Description: 
import tweepy
import csv
import scrape
import PySimpleGUI as sg


# Setting up GUI
sg.theme('light grey 2')

# Creating the window layout
layout = [  [sg.Text('Enter bearer token for API authentication: '), sg.InputText()],
            [sg.Text('Enter file csv file name to save to:'), sg.InputText()],
            [sg.Text('Enter query text:'), sg.InputText()],
            [sg.Text('Enter start time frame (YYYY-MM-DD):'), sg.InputText()],
            [sg.Text('Enter end time frame (YYYY-MM-DD):'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]
        ]         

# Creating the GUI window
window = sg.Window('Martin-tweepy', layout)

# Event Loop
while True:
    event, values = window.read()
    # values stores the input [bearer token, csv file, query, start time, end time]

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    elif event == 'Ok':
        token = scrape.auth(values[0])
        
        q = scrape.insert_query(values[2])
        # Following line replaces previous if user has access to time fram queries through Twitter API
        # q = scrape.build_query(values[2], values[3], values[4])
        
        data = scrape.tweet_scrape(token, q)
        scrape.tweets_csv(data, values[1])

        print("Done") 

window.close()