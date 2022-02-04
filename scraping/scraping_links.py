import os
import sys
from bs4 import BeautifulSoup

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from scraping.scraping_details import run_scrape_details_and_save_to_db
from scraping.base_scraping import load_page
from scraping.helpers import wait_for_xpath, click_btn_by_xpath

data_links = []


def load_page_data(driver):
    wait_for_xpath(driver, '/html/body/div/div/div/div[4]/div/div/button[4]')
    result = get_link_from_html(driver.page_source)
    for res in result:
        data_links.append(res)


def get_link_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all('div', class_='blueprint-thumbnail')
    links = []
    for div in divs:
        links.append("https://factorioprints.com" + str(div.find('a').get("href")))
    return links


def pagination(driver):
    click_btn_by_xpath(driver=driver, xpath='/html/body/div/div/div/div[4]/div/div/button[4]')
    return driver


def run_scrape_links(url):
    driver = load_page(url)
    for n in range(0, 10):
        load_page_data(driver)
        driver = pagination(driver)

    return data_links


if __name__ == '__main__':
    links = run_scrape_links("https://factorioprints.com/top")
    for link in links:
        run_scrape_details_and_save_to_db(link)
