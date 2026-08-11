# custom downloads

import os 
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()

current_folder = os.getcwd()

my_pref = {
    "download.default_directory" : current_folder,  # Tell it exactly where to save

     "download.prompt_for_download" : False         # Tell it NOT to ask "Save As..."
}

chrome_options.add_experimental_option("prefs",my_pref)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://the-internet.herokuapp.com/download")

download_btn = driver.find_element(By.XPATH,"//a[contains(text(),'Notes')]")

download_btn.click()

time.sleep(2)
driver.quit()