# TwitterScrape
Scrapes Twitter using Selenium webdriver.
Provides date, statistics, and contents of any number of tweets after a search query.

# Requirements
After downloading, install and add chromedriver: https://chromedriver.chromium.org/downloads.
You will need to have a twitter account to run the bot on. Run main.py and provide the details given.
Usages of time.sleep in twitterbot.py should be adjusted based on your internet speed -- if the loading time is slower, then the sleep times need to be longer. 

# Notes
This project was designed in Windows. Modifications may need to be made for Linux and others.  
Running it will prompt for email, username, password, headless, login_method, minimum, and query.
  Enabling headless by typing "yes" will make it so the bot window is hidden from your desktop. Leaving headless as disabled will allow you to watch the process live.
  Login method can be either by username or email. Username may be the quicker process but either should be fine. 
  Minimum refers to the number of tweets you want to scrape. Enter a whole number.
  Query refers to the link page to scrape. 
