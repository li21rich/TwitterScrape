from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time, os

class Twitterbot:
	def __init__(self, email, password):
		"""Constructor
		Arguments:
			email {string} -- registered twitter email
			password {string} -- password for the twitter account
		"""
		self.email = email
		self.password = password
		chrome_options = webdriver.ChromeOptions()
		#chrome_options.add_argument("--headless")  # Make headless if desired.
		path = os.getcwd()
		path_join = os.path.join(path, 'chromedriver\chromedriver.exe')
		chromedriver_path = r"FILE PATH" #Insert file path to chromedriver.exe here
		#print(path_join)

		self.bot = webdriver.Chrome(
			options=chrome_options,
			# executable_path=path_join,
		)

	def login(self, usernameString):
		#sign in with email and password
		bot = self.bot
		# fetches the login page
		#bot.get('https://twitter.com/login')
		bot.get('https://twitter.com/i/flow/login')

		time.sleep(3)

		email = bot.find_element("xpath", '//input[@autocomplete="username"]')
		# sends the email to the email input
		email.send_keys(self.email)

		email.send_keys(Keys.RETURN)
		time.sleep(3)
		"""
		file_path = "output.html"
		with open(file_path, "w", encoding="utf-8") as file:
			file.write(bot.page_source)
		"""
		try:
			print("Suspicious activity detected")
			username = bot.find_element("xpath", '//input[@autocomplete="on" and @name="text"]')
			# sends the email to the email input
			username.send_keys(usernameString)
			username.send_keys(Keys.RETURN)
			print("Username check bypassed")
		except Exception as e:
			print("No suspicious activity detected")
		time.sleep(3)
		password = bot.find_element("xpath", '//input[@autocomplete="current-password"]')
		# sends the password to the password input
		password.send_keys(self.password)
		# executes RETURN key action
		password.send_keys(Keys.RETURN)
		time.sleep(5)
		"""
		file_path = "finalOutput.html"
		with open(file_path, "w", encoding="utf-8") as file:
			file.write(bot.page_source)
		"""
	def scrape(self, desiredTweets):
		bot = self.bot
		bot.get("https://twitter.com/search?q=Just%20Stop%20Oil%20OR%20JustStopOil&src=typed_query") #paste your desired search URL here
		time.sleep(3)
		#set - avoid redundancy
		links = set();
		n = int(desiredTweets/7.333333)
		for _ in range(n):
			# javascript scroll
			bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
			time.sleep(5)
			# iterating links
			elems = bot.find_elements(
				"xpath", "//a[@role='link' and contains(@href, 'status') and not(contains(@href, 'analytics')) and not(contains(@href, 'photo')) and not(contains(@href, 'people'))]"
			)
			# print("elems:", elems)
			for elem in elems:
				href = elem.get_attribute('href')
				# print(f'href:{href}')
				links.add(href)
		# iterating through links
		count = 0
		for link in links:
			count +=1
			print(count, ">{!}------------------------")
			# open link
			bot.get(link)
			time.sleep(3)
			tweet_element = bot.find_element("xpath", '//div[@data-testid="tweetText"]')
			# Get tweet text
			tweet_text = tweet_element.text
			print(tweet_text)
		#  homepage
		bot.get('https://twitter.com/')
