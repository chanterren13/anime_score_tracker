from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome(executable_path='/mnt/c/webdrivers/chromedriver.exe')
driver.get('https://myanimelist.net/anime/season')

total_scores = pd.DataFrame(columns=['name', 'source', 'score'])

animes = driver.find_elements_by_css_selector('.seasonal-anime')
for anime in animes:
    name = anime.find_element(By.CSS_SELECTOR, '.link-title')
    score = anime.find_element(By.CSS_SELECTOR, '.score-label')
    print(name.text +': '+score.text)
    anime_info = pd.DataFrame([[name.text, 'MAL', score.text]], columns=['name', 'source', 'score'])
    total_scores = total_scores.append(anime_info)

total_scores = total_scores[total_scores.score != 'N/A']
total_scores.sort_values(by='score', inplace=True, ascending=False)
