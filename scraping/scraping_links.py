import os
import sys
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from scraping.base_scraping import load_page
from scraping.helpers import wait_for_xpath


data_links = []


def load_page_data(driver):
    wait_for_xpath(driver, '/html/body/div/div/div/div[4]/div/div/button[4]')
    result = get_link_from_html(driver.page_source)
    for res in result:
        data_links.append(res)


def get_link_from_html(data):
    soup = BeautifulSoup(data, 'html.parser')
    divs = soup.find_all('div', class_='blueprint-thumbnail')
    links = []
    for div in divs:
        links.append("https://factorioprints.com" + str(div.find('a').get("href")))
    return links


def click_next_btn_by_xpath(driver):
    element = driver.find_element(By.XPATH, '/html/body/div/div/div/div[4]/div/div/button[4]')
    element.click()
    return driver


def pagination(driver):
    click_next_btn_by_xpath(driver)
    return driver


def main(url):
    driver = load_page(url)
    for n in range(0, 10):
        load_page_data(driver)
        driver = pagination(driver)

    return data_links


if __name__ == '__main__':
    links = main("https://factorioprints.com/top")
    print(links)
    print(len(links))
