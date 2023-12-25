from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time, os

class Twitterbot:
	def __init__(self, email, password, username, headless):
		self.email = email
		self.password = password
		self.username = username

		chrome_options = webdriver.ChromeOptions()
		if headless.lower() == "yes":
			chrome_options.add_argument("--headless")

		self.bot = webdriver.Chrome(
			options=chrome_options,
		)

	def loginWithEmail(self):
		bot = self.bot
		bot.get('https://twitter.com/i/flow/login')
		time.sleep(3)

		email_field = bot.find_element("xpath", '//input[@autocomplete="username"]')
		email_field.send_keys(self.email)
		email_field.send_keys(Keys.RETURN)
		time.sleep(3)

		try:
			username_field = bot.find_element("xpath", '//input[@autocomplete="on" and @name="text"]')
			username_field.send_keys(self.username)
			username_field.send_keys(Keys.RETURN)
			time.sleep(1)
		except Exception as e:
			time.sleep(1)

		password_field = bot.find_element("xpath", '//input[@autocomplete="current-password"]')
		password_field.send_keys(self.password)
		password_field.send_keys(Keys.RETURN)
		time.sleep(5)

	def loginWithUsername(self):
		bot = self.bot
		bot.get('https://twitter.com/i/flow/login')
		time.sleep(3)

		email_field = bot.find_element("xpath", '//input[@autocomplete="username"]')
		email_field.send_keys(self.username)
		email_field.send_keys(Keys.RETURN)
		time.sleep(2)

		password_field = bot.find_element("xpath", '//input[@autocomplete="current-password"]')
		password_field.send_keys(self.password)
		password_field.send_keys(Keys.RETURN)
		time.sleep(5)

	def scrape(self, minTweets, query):
			bot = self.bot
			bot.get(query)
			print("Scanning:", query)
			time.sleep(4)
			count = 0
			results = ""
			while count < minTweets:
				bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
				time.sleep(1)
				elements = bot.find_elements("xpath", "//article[@data-testid='tweet']")
				for elem in elements:
					text = str(elem.find_element("xpath", ".//div[@data-testid='tweetText']").text)
					analytic = str(elem.find_element("xpath", ".//div[@role='group']").get_attribute('aria-label'))
					date = str(elem.find_element("xpath", ".//time").get_attribute('datetime'))
					count += 1
					result = str(":::> #" + str(count) + ". " + analytic + " " + date + " <:::\n" + text )
					print(result)
					results += result + "\n"
			bot.get("https://twitter.com/home")
			file_path = "output.html"
			with open(file_path, "w", encoding="utf-8") as file:
				file.write(results)
			return results
