# Author: Kevin Li
# Description: This program uses tweepy to scrape tweets and store in a csv file.
import tweepy
import csv
import os
from dotenv import load_dotenv

# Setting up environmental variables
load_dotenv()
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

# Authentication with bearer token and setup for user query
def auth(user_token):
    return user_token

def insert_query(user_query):
    return user_query

# Builds the user query given the queried word, start time, and end time
def build_query(i_query, stime, etime):
    return i_query + 'start_time: ' + stime + ' end_time:' + etime

# Main function that pulls the tweets
def tweet_scrape(i_token, i_query):
    client = tweepy.Client(bearer_token=i_token)
    tweets = client.search_recent_tweets(query=i_query)

    for tweet in tweets.data:
        print(tweet.text)
        print(tweet.id)
        if len(tweet.context_annotations) > 0:
            print(tweet.context_annotations)
    
    return tweets

# Writes the tweets data to the csv file
def tweets_csv(tweets_response, save_file):
    #Creating a csv file
    csvFile = open(save_file, "a", newline="", encoding='utf-8')
    csvWriter = csv.writer(csvFile)

    csvWriter.writerow(['tweet_id','retweets', 'replys', 'likes','text', 'sentiment'])

    for tweet in tweets_response.data:
        tweet_id = tweet.id
        text = tweet.text
        
        retweets = tweet.public_metrics
        replys = tweet.public_metrics
        likes = tweet.public_metrics

        res = [tweet_id, retweets, replys, likes, text, '']

        csvWriter.writerow(res)

    csvFile.close

# Main function for testing functionality of the program
def main():
    tweet_data = tweet_scrape(BEARER_TOKEN, 'water')
    tweets_csv(tweet_data, 'data.csv')

main()