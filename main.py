import twitterbot as tb

email = input("Enter bot twitter email: ")
username = input("Enter bot twitter username: ")
password = input("Enter bot twitter password: ")
headless = input("Enable headless? Enter \"yes\" if unsure or see the README.md file: ")
login_method = input("Enter \"username\" to log in with username or enter \"email\" to log in with email")
minimum = input("Enter minimum number of tweets to scrape: ")
query = input("Enter search URL to scrape ( i.e. https://twitter.com/search?q=Search%20Query%20OR%20SearchQuery&src=typed_query ): ")
try:
    bot = tb.Twitterbot(email, password, username, headless)
    if login_method.lower() == "username":
        bot.loginWithUsername()
    else:
        bot.loginWithEmail
except Exception as e:
    print("Invalid input. Please double check account credentials and ensure that you have inputted valid parameters")

bot.scrape(minimum, query)
