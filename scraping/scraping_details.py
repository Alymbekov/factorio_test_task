import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from scraping.helpers import wait_for_xpath


def load_page_data(driver):
    wait_for_xpath(driver, '//*[@id="root"]')
