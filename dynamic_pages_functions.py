from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

# Initializing selenium browser for dynamic requests
options = Options()
options.add_argument('--headless=new')
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Return html after dynamic load waiting
def getPageFromDynamicWebsite(url):
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )
    page_source = driver.page_source

    return page_source


def getWorldBankData(country_name, url, bigNumbers):
    translated_country_name = GoogleTranslator(
        source='auto', target='english').translate(text=country_name)
    try:
        page = getPageFromDynamicWebsite(url)
    except:
        return 0

    soup = BeautifulSoup(page, 'html.parser')

    for row in soup.select('div.item'):
        columns = row.contents

        country = columns[0].text
        if (country == country_name or country == translated_country_name):
            if columns[2].text:
                if bigNumbers:
                    data = columns[2].text.replace(',', '').strip()
                else:
                    data = columns[2].text
                return float(data)
        
    return 0


def getFemalePopulation(country_name):
    return getWorldBankData(
        country_name=country_name,
        url='https://data.worldbank.org/indicator/SP.POP.TOTL.FE.IN',
        bigNumbers=True
    )


def getMalePopulation(country_name):
    return getWorldBankData(
        country_name=country_name,
        url='https://data.worldbank.org/indicator/SP.POP.TOTL.MA.IN',
        bigNumbers=True
    )


def getForestArea(country_name):
    return getWorldBankData(
        country_name=country_name,
        url='https://data.worldbank.org/indicator/AG.LND.FRST.ZS',
        bigNumbers=False
    )


def getGdp(country_name):
    return getWorldBankData(
        country_name=country_name,
        url='https://data.worldbank.org/indicator/NY.GDP.MKTP.CD',
        bigNumbers=True
    )


def getGdpPerCapita(country_name):
    return getWorldBankData(
        country_name=country_name,
        url='https://data.worldbank.org/indicator/NY.GDP.PCAP.CD',
        bigNumbers=True
    )


def getGini(country_name):
    return getWorldBankData(
        country_name=country_name,
        url='https://data.worldbank.org/indicator/SI.POV.GINI',
        bigNumbers=False
    )


def getLifeExpectancy(country_name):
    return getWorldBankData(
        country_name=country_name,
        url='https://data.worldbank.org/indicator/SP.DYN.LE00.IN',
        bigNumbers=False
    )


def getPopulationGrowthRate(country_name):
    return getWorldBankData(
        country_name=country_name,
        url='https://data.worldbank.org/indicator/SP.POP.GROW',
        bigNumbers=False
    )


def getRuralPopulation(country_name):
    return getWorldBankData(
        country_name=country_name,
        url='https://data.worldbank.org/indicator/SP.RUR.TOTL',
        bigNumbers=True
    )


def getTotalPopulation(country_name):
    return getWorldBankData(
        country_name=country_name,
        url='https://data.worldbank.org/indicator/SP.POP.TOTL',
        bigNumbers=True
    )