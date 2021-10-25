from selenium import webdriver
import pandas as pd
import mal as mal
import anidb as anidb
import os.path

if os.path.isfile('scores/anime_scores.csv'):
    saved_scores = pd.read_csv('scores/anime_scores.csv')
    week = saved_scores['week'].iloc[saved_scores.shape[0]-1] + 1
else:
    saved_scores = pd.DataFrame(columns=['name', 'source', 'week', 'score'])
    week = 1

total_scores = pd.DataFrame(columns=['name', 'source', 'week', 'score'])

driver = webdriver.Chrome(executable_path='/mnt/c/webdrivers/chromedriver.exe')
adb = anidb.anidb(driver)
total_scores = total_scores.append(adb.pull_data(week), ignore_index=False)

myanilist = mal.mal(driver)
total_scores = total_scores.append(myanilist.pull_data(week), ignore_index=False)

print(total_scores)

pd.concat([saved_scores, total_scores], ignore_index=True).to_csv('scores/anime_scores.csv', index=False)
