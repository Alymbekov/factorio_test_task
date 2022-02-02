import asyncio
import os
import sys
from pyppeteer import launch
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from scraping import helpers

data_links = []


async def get_link_from_html(data):
    soup = BeautifulSoup(data, 'html.parser')
    links = soup.find_all('a')
    return links


async def click_next_btn_by_xpath(page):
    elements = await page.xpath('/html/body/div/div/div/div[4]/div/div/button[4]')
    return elements[0]


async def load_page(url):
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.setUserAgent(helpers.get_usage())
    await page.goto(url)
    return page


async def load_page_data(page):
    try:
        import random
        await page.waitForXPath('/html/body/div/div/div/div[4]/div/div/button[4]')
        await page.screenshot({'path': f'example{random.randint(666, 999)}.png'})
        data = await page.evaluate("""
            document.querySelector('*').outerHTML
        """)
        links = await get_link_from_html(data)
        data_links.append(links)
    except:
        pass


async def pagination(page):
    try:
        next_btn = await click_next_btn_by_xpath(page)
        await next_btn.click()
        await page.waitFor(5000)
        return page
    except Exception as e:
        raise ValueError("Пагинация не сработало")


async def main_func():
    url = "https://factorioprints.com/top"
    page = await load_page(url)
    for n in range(0, 10):
        await load_page_data(page)
        page = await pagination(page)
    await page.close()

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main_func())
except Exception as e:
    print(data_links)
finally:
    event_loop.close()
