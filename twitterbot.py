import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
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


class Twitterbot:
	def __init__(self, email, password, username, headless):
		self.email = email
		self.password = password
		self.username = username
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument("--headless") if headless.lower() == "yes" else None
		self.bot = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

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

	def login_with_username(self):
		bot = self.bot
		bot.get('https://twitter.com/i/flow/login')
		email_field = WebDriverWait(bot, 10).until(ec.presence_of_element_located(('xpath', '//input[@autocomplete="username"]')))
		email_field.send_keys(self.username, Keys.RETURN)
		password_field = WebDriverWait(bot, 10).until(ec.presence_of_element_located(('xpath', '//input[@autocomplete="current-password"]')))
		password_field.send_keys(self.password, Keys.RETURN)
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
