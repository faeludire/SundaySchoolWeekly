# Import our Twitter credentials from credentials.py
from credentials import *
import tweepy
import datetime
from time import sleep


def tweet_lesson(lesson_number):
    # Access and authorize our Twitter credentials from credentials.py
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # File path for the lessons
    file_path = 'Memory_verses/' + str(lesson_number) + '.txt'

    # Open the current lesson text file for reading
    lesson_file = open(file_path, 'r')
    file_lines = lesson_file.readlines()

    # Close file
    lesson_file.close()

    # Update status with lines read from file
    last_tweet = api.update_status("Sunday School Weekly Lesson\n"
                                   "Find out more at apostolicfaithweca.org\n"
                                   "#AFMSundaySchool."
                                   "\nThe Sunday School lesson for this week is:")
    # Create a loop to iterate over file lines
    for line in file_lines:
        # Add try ... except block to catch and output errors
        try:
            print(line)
            if line != '\n':
                last_tweet = api.update_status(line, last_tweet.id)
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
        sleep(5)


for i in range(95, 200, 1):
    print("Currently Tweeting Lesson Number = ", i, '\n')
    presentUpdateTime = datetime.datetime.now()
    presentWeekNumber = datetime.date(presentUpdateTime).isocalendar()[1]
    nextWeekNumber = datetime.date(presentUpdateTime).isocalendar()[1] + 1

    print('Present week number == ', presentWeekNumber)
    print('Next week number == ', nextWeekNumber)

    while presentWeekNumber < nextWeekNumber:
        presentUpdateTime = datetime.datetime.now()
        if presentUpdateTime.hour == 11 and presentUpdateTime.minute == 30 and presentUpdateTime.second == 0 and \
                        presentUpdateTime.microsecond == 0:
            tweet_lesson(i)
            print('I tweeted this lesson at ', datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'), 'Next Tweet will '
                                                                                                      'be tomorrow at '
                                                                                                      '11:00AM', '\n\n')
        presentWeekNumber = datetime.date(presentUpdateTime).isocalendar()[1]

