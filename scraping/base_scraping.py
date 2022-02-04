from selenium import webdriver

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True


def load_page(url):
    driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())
    driver.get(url)
    return driver
