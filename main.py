# Copyright (c) 2024, Richard Li, United States. All rights reserved
# Email: lilrichardh@gmail.com

import sys
import resultsfilter
import twitterbot as tb


# USER INPUT:

# account credentials
email = input("1. Enter bot twitter email: ") 
username = input("2. Enter bot twitter username: ")
password = input("3. Enter bot twitter password: ")

login_method = input("4. Enter \"yes\" to log in with email or \"no\" to log in with username [Default: yes]: ")  # This is largely insignificant unless one login method does not work while the other does.
headless = input("5. Enter \"yes\" to hide scraping browser window while scraping (headless) or \"no\" to keep it open [Default: no]: ") # Headless runs faster. Non-headless is helpful for testing.
advanced = input("6. Enter \"yes\" for scraping-by-month or \"no\" for simple scrape [Default: no]: ")  #  Monthly scraping is useful for observational research studies. You can modify the code in twitterbot.py to suit your needs.

# This chunk of text is just so you can paste in a URL to scrape:
print("\n7. Now to generate a search query:\n\nGo to twitter.com and type your search query into the search bar.\nYou may use quotation marks to look for exact phrases, OR/AND operands to condition your search, hashtags, and other search operators to make your search precise. For example, entering")
print("   #juststopoil OR \"Just Stop Oil\" OR \"JustStopOil\"   ")
print("into Twitter's search bar will produce a search for tweets containing the hashtag for juststopoil, or the exact phrase \"Just Stop Oil\", or the exact phrase \"JustStopOil\"")
print("You may also append search operators like \"since:2022-02-14\" or \"lang:en\" to further narrow your search. For more examples of search syntax, see https://developer.x.com/en/docs/x-api/v1/rules-and-filtering/search-operators")
print("ALTERNATIVELY, simply go to twitter.com/search-advanced and enter your search terms there, which will help you produce the search you need")
if advanced.lower() == "yes":
    print("Since you have advanced scraping enabled, do not include any search operators (i.e. \"since:YYYY-MM-DD\" or \"until:YYYY-MM-DD\" related to date in your search query/URL. This will be handled automatically.")
else:
    print("If you want to sort by recent/latest tweets instead of popular/trending, append \"&f=live\" to the end of your search query URL.")
query = input("Once you have entered your search, input the resulting URL you would like to search (i.e. \"https://twitter.com/search?q=%23juststopoil%20OR%20%22Just%20Stop%20Oil%22%20OR%20%22JustStopOil%22%20since%3A2022-02-14&src=typed_query&f=top&lang=en\" is available as a default demo input): ")
if query == "":
    query = "https://twitter.com/search?q=%23juststopoil%20OR%20%22Just%20Stop%20Oil%22%20OR%20%22JustStopOil%22%20since%3A2022-02-14&src=typed_query&f=top&lang=en";  # The search URL defaults to this for DEMO testing.
    if advanced.lower() == "yes":
        query = "https://twitter.com/search?q=%23juststopoil%20OR%20%22Just%20Stop%20Oil%22%20OR%20%22JustStopOil%22"

start_date = 0  # used for advanced scrape
end_date = 0  # used for advanced scrape
months = 0  # used for advanced scrape
cap = 0  # used for advanced scrape
if advanced.lower() == "yes":
    start_date = input("\n8. Now enter the start date to scrape from, YYYY-MM-DD (i.e. 2022-02-14): ")
    end_date = tb.increment_month(start_date)
    months = input("9. Up to how many months would you like to scrape for? ")
    cap = input("10. How many tweets at maximum per month? Default value is 50: ")  # Pressing enter defaults to 50. Higher values allow for greater sample sizes, but if the value is greater than the amount of tweets posted in the world in a given month, you potentially may face issues.
    if cap == "":
        cap = 50
    sort = input("11. Enter \"yes\" to scrape tweets in order of trending/popularity (sort by top). Enter \"no\" to sort by recency instead: ")  # Pressing enter defaults to no. Sorting by top can be helpful for a sample size biased toward popular tweets. Sorting by recency can be helpful for a more representative sample.
    if sort == "":
        sort = "no"
else:
    minimum = input("\n8. Enter minimum number of tweets to scrape: ")  # Pressing enter defaults to 10. Program will attempt to scrape at least this many tweets, if not more.
    if minimum == "":
        minimum = 10


# LOGGING IN:

try:
    bot = tb.Twitterbot(email, password, username, headless)
    if login_method.lower() == "yes":
        bot.login_with_email
    else:
        bot.login_with_username_like_human()
except Exception as e:
    print("Invalid input. Please double check account credentials and ensure that you have inputted valid parameters.")
    print(e)
    sys.exit()


# SCRAPING:

rawScrape = None
print("\nScraping... ...")
if advanced.lower() == "yes":
    rawScrape = bot.advanced_scrape(start_date, end_date, months, cap, query, sort)
else:
    rawScrape = bot.scrape(minimum, query)

do_dupes = input("\n\nDone scraping. Filter out duplicate tweets? Enter \"yes\" or \"no\": ")
do_filter = input("Filter out tweets that are too short? Enter \"yes\" or \"no\": ")
if do_dupes.lower() == "yes":
    dictionary_output = resultsfilter.remove_duplicates(rawScrape)
else:
    dictionary_output = resultsfilter.remove_none(rawScrape)
if do_filter.lower() == "yes":
    filter_limit = int(input("How many alphabetical characters is too short, in other words, what is the minimum length of a tweet? "))
    try:
        dictionary_output = resultsfilter.remove_shorts(dictionary_output, filter_limit)
    except Exception as e:
        print("Invalid input. Will default to no filtering.")

# Prints the filtered dictionary version of what "bot.scrape" or "bot.advanced_scrape" returns.
print("\nFiltered dictionary representation of scrape:\n", dictionary_output)  
print("\n\nDone. Your final results are in output.txt")

