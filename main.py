import twitterbot as tb
import secrets, sys

twitter_user = input("Enter bot twitter username: ")
# gets credentials dictionary
credentials = secrets.get_credentials()
# creates bot using credentials
bot = tb.Twitterbot(credentials['email'], credentials['password'])
# log in process
try:
    bot.login(twitter_user)
except Exception as e:
    print(e)
# START SCRAPE
desiredTweets = 20
bot.scrape(desiredTweets)
