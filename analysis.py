# Author: Kevin Li
# Description: This program uses Text Blob to perform sentiment analysis on a given .csv file.
from textblob import TextBlob
import csv
import re

# Helper function to filter out emojis, taken from https://stackoverflow.com/a/58356570
def remove_emojis(data):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)

# Main function that performs the sentiment analysis, using sentiment from TextBlob, save_file is input file to be processed, writes result to out.csv
def analyze_file(save_file):
    # Opening files
    csvFile = open(save_file, 'r', encoding="utf8")
    csvOut = open("out.csv", 'w', encoding="utf8")
    csv_reader = csv.reader(csvFile)
    csv_writer = csv.writer(csvOut)
    
    line_count = 0

    # Processing each row of data in save_file
    for row in csv_reader: 
        statement = TextBlob(remove_emojis(row[4]))
        
        row.append(statement.sentiment.polarity)

        csv_writer.writerow(row)
        line_count += 1

    csvFile.close
    csvOut.close

# Main function, holds testcase
def main():
    analyze_file("data.csv")

main()