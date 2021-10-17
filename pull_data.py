from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import mal as mal
import anidb as anidb

driver = webdriver.Chrome(executable_path='/mnt/c/webdrivers/chromedriver.exe')
adb = anidb.anidb(driver)
myanilist = mal.mal(driver)

total_scores = pd.concat([myanilist.pull_data(1), adb.pull_data(1)], ignore_index=False)

print(total_scores)

