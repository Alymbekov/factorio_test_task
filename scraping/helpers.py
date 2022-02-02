import os
import random
import sys
from pathlib import Path
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


def init_bs4(html):
    return BeautifulSoup(html, 'html.parser')


def get_usage():
    lines = open('useragents.txt').read().splitlines()
    usage = random.choice(lines)
    return usage


def wait_for_xpath(driver, xpath):
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))


def click_btn_by_xpath(xpath, driver):
    element = driver.find_element(By.XPATH, xpath)
    element.click()
    return driver


def get_parent_directory():
    path = Path(os.path.abspath(__file__))
    directory = Path(path.parent.absolute()).parent
    return directory


def generate_file_name(file_name):
    return file_name.replace('/', '')


def download_and_save_image(driver, xpath):
    html = driver.page_source
    soup = init_bs4(html)
    src_img = soup.find('img').get('src')
    file_name = generate_file_name(src_img)
    fn = os.path.join(get_parent_directory()) + f'/media/images/{file_name}.png'
    with open(fn, 'wb') as file:
        file.write(driver.find_element(By.XPATH, xpath).screenshot_as_png)
    return fn
