# TwitterScrape
Scrapes Twitter (also known as X) using Selenium webdriver.<br />
Logs in by provided username, email, and password, and then goes to a provided search URL, giving the date, statistics, and contents of any number of tweets associated with the search.

## Requirements
After downloading, **install and add chromedriver**: https://chromedriver.chromium.org/downloads.\
You will need Selenium and Python. \
You will also need a Twitter account to run the bot on. 
To use the program, run main.py and provide the details described in the tips below.\

## Tips
Running it will prompt for *email*, *username*, *password*, *minimum*, and *query*.\
&nbsp;&nbsp;*email*, *username*, *password*: These must be the credentials of **your twitter account**. It is recommended that you use a throwaway account.\
&nbsp;&nbsp;*minimum*: Minimum refers to the number of tweets you want to scrape. Enter a whole number.\
&nbsp;&nbsp;*query*: The search page link. You can go to Twitter, enter a search query (or use advanced search), and copy the resulting page URL.
