from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

class anidb():
    def __init__(self, driver):
        self.driver = driver

    def pull_data(self, week):
        self.driver.get('https://anidb.net/anime/season')
        animes = self.driver.find_elements_by_css_selector('.g_bubble .box')
        for anime in animes:
            name = anime.find_element(By.CSS_SELECTOR, '.name-colored')
            print(name)

if __name__ == '__main__':
    ani = anidb()
    ani.pull_data(1)

