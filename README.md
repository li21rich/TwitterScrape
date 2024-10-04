# SIMPLIFIED VERSION of Twitter Scrape
This repo  is the shortened, generalized, and more reusable version of the Twitter Scraping tool I developed for research analysis of the environmental action situation in the UK. Contact ![image](https://github.com/user-attachments/assets/404a3e78-4c65-40b6-baa7-aa77fa26a2c1) for the original full version.

# Usage
Simplified tool for scraping Twitter (also known as X) using Selenium webdriver.<br />
Logs in by provided username and password, and then goes to a provided search URL, giving the date, statistics, and contents of any number of tweets associated with the search.

## Requirements
After downloading, **install and add chromedriver**: https://chromedriver.chromium.org/downloads  \
You will need Selenium and Python. \
You will also need a Twitter account to run the bot on. \
To use the program, run main.py and provide the details described in the tips below.

## Tips
Running it will prompt for *username*, *password*, *minimum*, and *query*.\
&nbsp;&nbsp;*username* & *password*: These must be the credentials of **your twitter account**. It is recommended that you use a throwaway account.\
&nbsp;&nbsp;*minimum*: Minimum refers to the number of tweets you want to scrape. Enter an integer.\
&nbsp;&nbsp;*query*: The search page link. You can go to Twitter, enter a search query (or use advanced search), and copy the resulting page URL.
