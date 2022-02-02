import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def get_usage():
    lines = open('useragents.txt').read().splitlines()
    usage = random.choice(lines)
    return usage


def wait_for_xpath(driver, xpath):
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

