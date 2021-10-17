from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

class anidb():
    def __init__(self, driver):
        self.driver = driver
        self.source = 'anidb'

    def pull_data(self, week):
        self.driver.get('https://anidb.net/anime/season')

        total_scores = pd.DataFrame(columns=['name', 'source', 'week', 'score'])

        animes = self.driver.find_elements_by_css_selector('.g_bubble .box')
        for anime in animes:
            name = anime.find_element(By.CSS_SELECTOR, '.name-colored').text
            try:
                average = anime.find_element(By.CSS_SELECTOR, '.average')
                score = average.find_element(By.CSS_SELECTOR, '.value').text
            except NoSuchElementException:
                score = 'N/A'
            #print(name + ': ' + score)
            anime_info = pd.DataFrame([[name, self.source, week, score]], columns=['name', 'source', 'week', 'score'])
            total_scores = total_scores.append(anime_info)

        total_scores = total_scores[total_scores.score != 'N/A']
        total_scores.sort_values(by='score', inplace=True, ascending=False)
        return total_scores[:10]

if __name__ == '__main__':
    ani = anidb(webdriver.Chrome(executable_path='/mnt/c/webdrivers/chromedriver.exe'))
    df = ani.pull_data(1)
    print(df)

