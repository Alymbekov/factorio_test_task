import os
import sys


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from database.operations import add_author, add_information
from scraping.base_scraping import load_page
from scraping.helpers import (
    wait_for_xpath, click_btn_by_xpath, download_and_save_image, init_bs4
)


def load_page_data(driver):
    wait_for_xpath(driver, '//*[@id="root"]')
    wait_for_xpath(driver, '//*[@id="root"]/div/div/div[2]/div[1]/div[1]')
    wait_for_xpath(driver, '//*[@id="root"]/div/div/div[2]/div[2]/div')
    author = get_author_from_html(driver.page_source)
    detail = get_detail_from_html(driver.page_source)
    blue_string = get_blueprint(driver)
    file_path = download_and_save_image(driver, '//*[@id="root"]/div/div/div[2]/div[1]/a/img')
    return (
        author, detail, blue_string, file_path
    )


def get_card(html, card_header):
    soup = init_bs4(html)
    cards = soup.find_all('div', 'card')
    for card in cards:
        if card.find('div', class_='card-header').get_text() == card_header:
            return card


def get_author_from_html(html):
    dict_ = {}
    card = get_card(html, card_header='Info')
    trs = card.find_all('tr')
    for tr in trs:
        td = tr.find_all('td')[1].get_text()
        text = tr.find('td').get_text().strip()
        if text == 'Author':
            dict_['Author'] = td
        elif text == 'Created':
            dict_['Created'] = td
        elif text == 'Last Updated':
            dict_['LastUpdated'] = td
        elif text == 'Favorites':
            dict_['Favorites'] = td
    return dict_


def get_detail_from_html(html):
    card = get_card(html, card_header='Details')
    text = card.find('div', class_='card-body').find('div').get_text()
    return text


def get_blueprint(driver):
    driver = click_btn_by_xpath(
        driver=driver, xpath='//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/button[2]')
    wait_for_xpath(driver, '//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div[2]')
    html = driver.page_source
    soup = init_bs4(html)
    blue_string = soup.find('div', class_='blueprintString').get_text()
    return blue_string


def run_scrape_details_and_save_to_db(url):
    driver = load_page(url)
    author, detail, blue_string, file_path = load_page_data(driver)
    author_obj = add_author(author)
    add_information(
        information=detail,
        blue_print_string=blue_string,
        file_path=file_path,
        author=author_obj
    )
