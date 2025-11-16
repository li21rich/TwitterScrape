# TwitterScrape 

Uses Twitter's advanced search function to scrape tweets on Twitter/X using Selenium webdriver. 
Automatically logs in via username and password, and then goes to a provided search URL, giving the date, statistics, and contents of any number of tweets associated with the search.
> This repo is the rough, shortened version of the scraper I developed for my sentiment analysis research of environmental movements in the UK. Contact richardhli81 at gmail dot com for the original version with sentiment analysis and data visualization in 3D.

> UPDATE: Twitter now detects ChromeDriver. You will need to swap in [undetected-chromedriver](https://pypi.org/project/undetected-chromedriver/) instead of ChromeDriver.

## Getting Started

Make sure that you have a Twitter account to run the bot on. Getting twitter verification may help reduce rate limiting if it is worth the investment.
1. Set up environment
```
python -m venv .venv 
```
2. Activate environment
on Windows:
```
.\.venv\Scripts\Activate
```
or on macOS/Linux:
```
source .venv/bin/activate 
```
3. Dependencies
```
pip install -r requirements.txt
pip install --upgrade selenium requests webdriver-manager
python -m webdriver_manager.chrome
```
4. Run
```
python main.py
```
At minimum, you will be prompted for email, username, password, log-in method, headless, scraping method, query, and number of tweets.
  email, username, & password: These must be the credentials of your twitter account. It is recommended that you use a throwaway account.
  log-in method: Provides two methods to log-in. If one doesn't work, just try the other.
  headless: Keeps browser open or hidden while scraping.
  scraping method: Use the regular version unless you need to scrape by month. The advanced scrape-by-month version will also prompt you for dates.
  query: The search page link. You can go to Twitter, enter a search query (or use advanced search), and copy the resulting page URL.
  number of tweets: An approximation of how many tweets you want to scrape.

Once scraping is complete you will also have the option to filter out duplicates and short tweets.

> Twitter frequently changes its login flow, so you may need to update the code,
> Searching can take multiple hours depending on the size of the search. The results will be written to output.txt.
> You can extend the scraper to capture additional interaction statistics if needed.

## Lazy Demo Run
This will demonstrate how the bot scrapes for a search of tweets including "Just Stop Oil" related keywords
```
(your bot's email)
(your bot's username)
(your bot's password)
Press enter 5 times (uses the default inputs)
Once the bot finishes running, press enter 2 more times.
```