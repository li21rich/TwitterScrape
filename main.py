import twitterbot as tb

#email = input("Enter bot twitter email: ")
email = "" #email login method can be used but is unneeded
username = input("Enter bot twitter username: ")
password = input("Enter bot twitter password: ")
headless = "no";
minimum = input("Enter minimum number of tweets to scrape: ")
query = input("Enter search URL to scrape ( i.e. https://twitter.com/search?q=Search%20Query%20OR%20SearchQuery&src=typed_query ): ")
try:
    bot = tb.Twitterbot(email, password, username, headless)
    bot.loginWithUsername()
    bot.scrape(minimum, query)
except Exception as e:
    print("Invalid input. Please double check account credentials and ensure that you have inputted valid parameters")
    print(e)

