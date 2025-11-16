import time, random
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 


def increment_month(date_str):
	date = datetime.strptime(date_str, "%Y-%m-%d")
	year, month = date.year, date.month
	if month == 12:
		year += 1
		month = 1
	else:
		month += 1
	return datetime(year, month, 1).strftime("%Y-%m-%d")

def human_type(bot, element, text):
	actions = ActionChains(bot)
	actions.move_to_element(element).click().perform()
	for char in text:
		element.send_keys(char)
		time.sleep(random.uniform(0.02, 0.2))  # simulate human typing


class Twitterbot:
	def __init__(self, email, password, username, headless):
		self.email = email
		self.password = password
		self.username = username
		chrome_options = webdriver.ChromeOptions()
		if headless.lower() == "yes": chrome_options.add_argument("--headless")
		chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
		chrome_options.add_experimental_option("useAutomationExtension", False)
		self.bot = webdriver.Chrome(
			service=Service(ChromeDriverManager().install()),
			options=chrome_options
		)

	def login_with_email(self):
		bot = self.bot
		bot.get('https://twitter.com/i/flow/login')
		email_field = WebDriverWait(bot, 10).until(ec.visibility_of_element_located(('xpath', '//input[@autocomplete="username"]')))
		email_field.send_keys(self.email, Keys.RETURN)
		try:
			username_field = WebDriverWait(bot, 5).until(ec.presence_of_element_located(('xpath', '//input[@autocomplete="on" and @name="text"]')))
			username_field.send_keys(self.username, Keys.RETURN)
		except Exception as e:
			pass
		password_field = WebDriverWait(bot, 10).until(ec.presence_of_element_located(('xpath', '//input[@autocomplete="current-password"]')))
		password_field.send_keys(self.password, Keys.RETURN)
		time.sleep(1)

	def login_with_username(self): # old version
		bot = self.bot
		bot.get('https://twitter.com/i/flow/login')
		email_field = WebDriverWait(bot, 10).until(ec.presence_of_element_located(('xpath', '//input[@autocomplete="username"]')))
		actions = ActionChains(bot)
		actions.move_to_element(email_field).click().pause(0.5).send_keys("myemail@example.com").perform()
		email_field.send_keys(self.username, Keys.RETURN)
		password_field = WebDriverWait(bot, 10).until(ec.presence_of_element_located(('xpath', '//input[@autocomplete="current-password"]')))
		password_field.send_keys(self.password, Keys.RETURN)
		time.sleep(1)

	def login_with_username_like_human(self):
		bot = self.bot
		bot.get('https://twitter.com/i/flow/login')

		# Username/email field
		username_field = WebDriverWait(bot, 10).until(
			ec.presence_of_element_located(('xpath', '//input[@name="text"]'))
		)
		human_type(bot, username_field, self.username)
		username_field.send_keys(Keys.RETURN)

		# Password field
		password_field = WebDriverWait(bot, 10).until(
			ec.presence_of_element_located(('xpath', '//input[@name="password"]'))
		)
		human_type(bot, password_field, self.password)
		password_field.send_keys(Keys.RETURN)

		time.sleep(1)

	def scrape(self, mintweets, query):
		bot = self.bot
		bot.get(query)
		print("\nScanning:", query)
		WebDriverWait(bot, 10).until(ec.presence_of_element_located(('xpath', "//article[@data-testid='tweet']")))
		count = 0
		results = ""
		while count < int(mintweets):
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
		with open("output.txt", "w", encoding="utf-8") as file: file.write(results)
		return results

	def advanced_scrape(self, startingDate, endingDate, months, cap, in_query, sort):  # sorts by popular from start date to end date for each month
		bot = self.bot
		start_date = startingDate  # it might be a smart idea to modify this code to run by days instead of months, because advanced scrape tends to bias tweets posted at the end of every month.
		end_date = endingDate
		count = 0
		results = ""
		if sort.lower() == "yes":
			sort = "&f=top"  # sort by popular/trending
		else:
			sort = "&f=live"  # sort by latest/recent
		for i in range(int(months)): # i.e. 24 = scrape from each of the 24 months
			query = in_query + "20since%3A" + start_date + "%20until%3A" + end_date + "&src=typed_query" + sort
			bot.get(query)
			print("Scanning from", start_date, "to", end_date)
			try:
				WebDriverWait(bot, 10).until(ec.presence_of_element_located(('xpath', "//article[@data-testid='tweet']")))
				i = 0
				while i < int(cap):  # continue jumps to here. 50 is recommended value for cap. Higher values may cause errors if the amount of tweets in a month is exceeded by the cap.
					bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
					time.sleep(1)
					elements = WebDriverWait(bot, 10).until(ec.presence_of_all_elements_located(('xpath', "//article[@data-testid='tweet']")))
					for elem in elements:
						text = str(elem.find_element("xpath", ".//div[@data-testid='tweetText']").text)
						text = text.replace("\n\n", "\n").replace("\n\n", "\n")
						analytic = str(elem.find_element("xpath", ".//div[@role='group']").get_attribute('aria-label'))
						date = str(elem.find_element("xpath", ".//time").get_attribute('datetime'))
						date = date.split('T')[0]
						i += 1
						count += 1
						result = str(":::> #" + str(count) + ". " + analytic + " " + date + " <:::\n" + text)
						print(result)
						results += result + "\n"
						if not i < int(cap):
							break
				start_date = end_date
				end_date = increment_month(end_date)
			except Exception as e:
				print("It seems you've been rate limited. You left off scraping from", start_date, "to", end_date)
				print("No worries. The program will automatically continue your search in 15 minutes.")
				time.sleep(15 * 60)
				continue
		with open("output.txt", "w", encoding="utf-8") as file: file.write(results)
		return results
