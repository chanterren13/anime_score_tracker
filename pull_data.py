from selenium import webdriver
import pandas as pd
import mal as mal
import anidb as anidb
import os.path

if os.path.isfile('scores/anime_scores.csv'):
    total_scores = pd.read_csv('scores/anime_scores.csv')
    week = total_scores['week'].iloc[total_scores.shape[0]-1] + 1
else:
    total_scores = pd.DataFrame(columns=['name', 'source', 'week', 'score'])
    week = 1

driver = webdriver.Chrome(executable_path='/mnt/c/webdrivers/chromedriver.exe')
adb = anidb.anidb(driver)
total_scores = total_scores.append(adb.pull_data(week), ignore_index=False)

myanilist = mal.mal(driver)
total_scores = total_scores.append(myanilist.pull_data(week), ignore_index=False)

print(total_scores)

total_scores.to_csv('scores/anime_scores.csv', index=False)
