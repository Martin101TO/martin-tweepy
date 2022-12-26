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
            [sg.Text('Enter queury text:'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]
        ]

# Creating the GUI window
window = sg.Window('Martin-tweepy', layout)

# Event Loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    elif event == 'Ok':
        token = scrape.auth(values[0])
        q = scrape.insert_query(values[1])
        
        data = scrape.tweet_scrape(token, q)
        scrape.tweets_csv(data)

        print("Done") 

window.close()