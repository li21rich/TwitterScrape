# TwitterScrape
Scrapes Twitter using Selenium webdriver.<br />
Logs in by provided username, email, and password, and then goes to a provided search URL, giving date, statistics, and contents of any number of tweets associated with the search.

## Requirements
After downloading, **install and add chromedriver**: https://chromedriver.chromium.org/downloads.<br />
You will need to have a twitter account to run the bot on. Run main.py and provide the details given.<br />
Usages of time.sleep in twitterbot.py should be adjusted based on your internet speed -- if the loading time is slower, then the sleep times need to be longer. <br />
This project was designed in Windows. Modifications may need to be made for Linux and others.  

## Tips
Running it will prompt for *email*, *username*, *password*, *headless*, *login_method*, *minimum*, and *query*.<br />
  >*email*, *username*, *password*: These must be the credentials of **your twitter account**. It is recommended that you create a burner account for this. <br />
  >*headless*: Enabling headless by typing "yes" will make it so the bot window is hidden from your desktop. Leaving headless as disabled will allow you to watch the process live.<br />
  >*login_method*: Login method can be either by username or email. Username may be the quicker process but either should be fine. <br />
  >*minimum*: Minimum refers to the number of tweets you want to scrape. Enter a whole number.
