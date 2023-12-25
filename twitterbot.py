import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class Twitterbot:
	def __init__(self, email, password, username, headless):
		self.email = email
		self.password = password
		self.username = username
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument("--headless") if headless.lower() == "yes" else None
		self.bot = webdriver.Chrome(options=chrome_options,)

	def login_with_email(self):
		bot = self.bot
		bot.get('https://twitter.com/i/flow/login')
		email_field = WebDriverWait(bot, 10).until(ec.visibility_of_element_located(('xpath', '//input[@autocomplete="username"]')))
		email_field.send_keys(self.email, Keys.RETURN)
		try:
			username_field = WebDriverWait(bot, 10).until(ec.presence_of_element_located(('xpath', '//input[@autocomplete="on" and @name="text"]')))
			username_field.send_keys(self.username, Keys.RETURN)
		except Exception as e:
			pass
		password_field = WebDriverWait(bot, 10).until(ec.presence_of_element_located(('xpath', '//input[@autocomplete="current-password"]')))
		password_field.send_keys(self.password, Keys.RETURN)
		time.sleep(1)

	def login_with_username(self):
		bot = self.bot
		bot.get('https://twitter.com/i/flow/login')
		email_field = WebDriverWait(bot, 10).until(ec.presence_of_element_located(('xpath', '//input[@autocomplete="username"]')))
		email_field.send_keys(self.username, Keys.RETURN)
		password_field = WebDriverWait(bot, 10).until(ec.presence_of_element_located(('xpath', '//input[@autocomplete="current-password"]')))
		password_field.send_keys(self.password, Keys.RETURN)
		time.sleep(1)

	def scrape(self, minTweets, query):
		bot = self.bot
		bot.get(query)
		print("Scanning:", query)
		WebDriverWait(bot, 10).until(ec.presence_of_element_located(('xpath', "//article[@data-testid='tweet']")))
		count = 0
		results = ""
		while count < minTweets:
			bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
			time.sleep(1)
			elements = WebDriverWait(bot, 10).until(ec.presence_of_all_elements_located(('xpath', "//article[@data-testid='tweet']")))
			for elem in elements:
				text = str(elem.find_element("xpath", ".//div[@data-testid='tweetText']").text)
				analytic = str(elem.find_element("xpath", ".//div[@role='group']").get_attribute('aria-label'))
				date = str(elem.find_element("xpath", ".//time").get_attribute('datetime'))
				count += 1
				result = str(":::> #" + str(count) + ". " + analytic + " " + date + " <:::\n" + text)
				print(result)
				results += result + "\n"
		with open("output.html", "w", encoding="utf-8") as file: file.write(results)
		return results
