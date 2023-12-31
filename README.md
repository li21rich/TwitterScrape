# TwitterScrape
Scrapes Twitter (also known as X) using Selenium webdriver.<br />
Logs in by provided username, email, and password, and then goes to a provided search URL, giving the date, statistics, and contents of any number of tweets associated with the search.

## Requirements
After downloading, **install and add chromedriver**: https://chromedriver.chromium.org/downloads.\
You will need to have Selenium and Python. \
You will also need to have a Twitter account to run the bot on. Run main.py and provide the details given.\
Usages of time.sleep in twitterbot.py should be adjusted based on your internet speed -- if the loading time is slower, then the sleep times need to be longer.\
This project was designed in Windows. Modifications may need to be made for Linux and others.  

## Tips
Running it will prompt for *email*, *username*, *password*, *headless*, *login_method*, *minimum*, and *query*.\
&nbsp;&nbsp;*email*, *username*, *password*: These must be the credentials of **your twitter account**. It is recommended that you use a new burner account.\
&nbsp;&nbsp;*headless*: Enabling headless by typing "yes" will make it so the bot window is hidden (runs faster). Leaving headless disabled will display the process live.\
&nbsp;&nbsp;*login_method*: Login method can be either by username or email. Username may be the quicker process but either should be fine.\
&nbsp;&nbsp;*minimum*: Minimum refers to the number of tweets you want to scrape. Enter a whole number.\
&nbsp;&nbsp;*query*: Link to search page. You can find one by going to Twitter, typing in the desired search query (or use advanced search), and copying the URL at the top of the page.
