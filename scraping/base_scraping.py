from selenium import webdriver

from webdriver_manager.firefox import GeckoDriverManager


def load_page(url):
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get(url)
    return driver
