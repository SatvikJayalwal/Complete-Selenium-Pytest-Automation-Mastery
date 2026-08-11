# ChromeOptions, disabling extensions, User-Agents


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()

# When Chrome opens, it sometimes tries to load extensions (like ad-blockers or password managers)
# These can accidentally click things or change a webpage, ruining your automated script. We want 
# to tell Chrome: "Open up, but do not load any extensions."
chrome_options.add_argument("--disable-extensions")

chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com")
driver.get("https://www.whatismybrowser.com/detect/what-is-my-user-agent/")

driver.quit()



