from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome(executable_path='/mnt/c/webdrivers/chromedriver.exe')
driver.get('https://myanimelist.net/anime/season')

total_scores = pd.DataFrame(columns=['name', 'source', 'week', 'score'])
week = 1

animes = driver.find_element_by_css_selector('.seasonal-anime-list')
animes = animes.find_elements(By.CSS_SELECTOR, '.seasonal-anime')
for anime in animes:
    name = anime.find_element(By.CSS_SELECTOR, '.link-title')
    score = anime.find_element(By.CSS_SELECTOR, '.score-label')
    print(name.text +': '+score.text)
    anime_info = pd.DataFrame([[name.text, 'MAL', week, score.text]], columns=['name', 'source', 'week', 'score'])
    total_scores = total_scores.append(anime_info)

total_scores = total_scores[total_scores.score != 'N/A']
total_scores.sort_values(by='score', inplace=True, ascending=False)
