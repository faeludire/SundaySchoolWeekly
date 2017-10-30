# Import our Twitter credentials from credentials.py
from credentials import *
import tweepy
from time import sleep

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for i in range(151, 400):
    #File path for the lessons
    filepath = 'Memory_verses/'+str(i)+'.txt'

    #Open the current lesson text file for reading
    lesson_file = open(filepath, 'r')
    file_lines = lesson_file.readlines()

    #Close file
    lesson_file.close()

    #Create a loop to iterate over file lines
    for line in file_lines:
        # Add try ... except block to catch and output errors
        try:
            print(line)
            if line != '\n':
                api.update_status(line)
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
        sleep(10)
