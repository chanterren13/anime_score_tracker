import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

class mal():
    def __init__(self, driver):
        self.driver = driver
        self.source = 'MAL'

    def pull_data(self, week):
        self.driver.get('https://myanimelist.net/anime/season')

        animes = self.driver.find_element_by_css_selector('.seasonal-anime-list')
        animes = animes.find_elements(By.CSS_SELECTOR, '.seasonal-anime')
        total_scores = pd.DataFrame(columns=['name', 'source', 'week', 'score'])

        for anime in animes:
            name = anime.find_element(By.CSS_SELECTOR, '.link-title')
            score = anime.find_element(By.CSS_SELECTOR, '.score-label')
            #print(name.text +': '+score.text)
            anime_info = pd.DataFrame([[name.text, self.source, week, score.text]], columns=['name', 'source', 'week', 'score'])
            total_scores = total_scores.append(anime_info)

        total_scores = total_scores[total_scores.score != 'N/A']
        total_scores.sort_values(by='score', inplace=True, ascending=False)
        return total_scores[:10]


if __name__ == '__main__':
    myanilist = mal(webdriver.Chrome(executable_path='/mnt/c/webdrivers/chromedriver.exe'))
    animes = myanilist.pull_data(1)
    print(animes)
