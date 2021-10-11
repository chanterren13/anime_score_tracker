from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/mnt/c/webdrivers/chromedriver.exe')
driver.get('https://myanimelist.net/anime/season')

animes = driver.find_elements_by_css_selector('.seasonal-anime')
animes = animes[:10]
for anime in animes:
    score = anime.find_element(By.CSS_SELECTOR, '.score-label')
    print(score.text)

