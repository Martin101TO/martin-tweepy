# Author: Kevin Li
# Description: This program uses tweepy to scrape tweets and store in a csv file.
import tweepy
import csv

# Authentication with bearer token
client = tweepy.Client(bearer_token='INSERT BEARER TOKEN HERE')

# Replace with your own search query
query = 'water lang:en'

tweets = client.search_recent_tweets(query=query)

for tweet in tweets.data:
    print(tweet.text)
    print(tweet.id)
    if len(tweet.context_annotations) > 0:
        print(tweet.context_annotations)

#Creating a csv file
csvFile = open("data.csv", "a", newline="", encoding='utf-8')
csvWriter = csv.writer(csvFile)

csvWriter.writerow(['tweet_id','retweets', 'replys', 'likes','text'])

for tweet in tweets.data:
    tweet_id = tweet.id
    text = tweet.text
    
    retweets = tweet.public_metrics
    replys = tweet.public_metrics
    likes = tweet.public_metrics

    res = [tweet_id, retweets, replys, likes, text]

    csvWriter.writerow(res)



csvFile.close