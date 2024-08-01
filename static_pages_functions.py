import re
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

# Wikipedia web scrap functions
def getCapitalPopulation(country_name):
    translated_country_name = GoogleTranslator(
        source='auto', target='english').translate(text=country_name)
    url = 'https://en.wikipedia.org/wiki/List_of_national_capitals_by_population'
    try:
        page = requests.get(url)
    except:
        return 0

    soup = BeautifulSoup(page.text, 'html.parser')

    for row in soup.select('table.wikitable tbody tr'):
        columns = row.find_all('td')

        if len(columns) < 3:
            continue

        country_column = columns[0]

        country = country_column.find('a').text.replace("*", '').strip()
        if country == country_name or country == translated_country_name:
            population = columns[2].get_text().replace(',', '')
            return int(population)

    return 0

def getUrbanizationRate(country_name):
    translated_country_name = GoogleTranslator(
        source='auto', target='english').translate(text=country_name)
    url = 'https://en.wikipedia.org/wiki/Urbanization_by_sovereign_state'
    try:
        page = requests.get(url)
    except:
        return 0

    soup = BeautifulSoup(page.text, 'html.parser')

    for row in soup.select('table.wikitable tbody tr'):
        columns = row.find_all('td')

        if len(columns) < 4:
            continue

        country_column = columns[0]

        country = country_column.find(
            'a').text if country_column.find('a') else False
        if country == country_name or country == translated_country_name:
            urbanization_rate = columns[3].get_text()
            return float(urbanization_rate)

    return 0

def getElectricityProd(country_name):
    translated_country_name = GoogleTranslator(
        source='auto', target='english').translate(text=country_name)
    url = 'https://en.wikipedia.org/wiki/List_of_countries_by_electricity_production'
    try:
        page = requests.get(url)
    except:
        return 0

    soup = BeautifulSoup(page.text, 'html.parser')

    for row in soup.select('table.wikitable tbody tr'):
        columns = row.find_all('td')

        if len(columns) < 2:
            continue

        country_column = columns[0]

        if country_column.find('a'):
            country = country_column.find('a').text
            if country == country_name or country == translated_country_name:
                electricity_prod = columns[1].get_text().replace(',', '')
                return float(electricity_prod)

    return 0

def getGoldProd(country_name):
    url = 'https://en.wikipedia.org/wiki/List_of_countries_by_gold_production'
    try:
        page = requests.get(url)
    except:
        return 0

    soup = BeautifulSoup(page.text, 'html.parser')

    for row in soup.select('table.wikitable tbody tr'):
        columns = row.find_all('td')

        if len(columns) < 3:
            continue

        country_column = columns[1]

        if country_column.find('a'):
            country = country_column.find('a').text
            if country == country_name:
                gold_prod = columns[2].get_text().replace(',', '')
                return int(gold_prod)

    return 0

def getHighestGeographicalPoint(country_name):
    portuguese_country_name = GoogleTranslator(
        source='auto', target='pt').translate(text=country_name)
    url = 'https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_ponto_mais_alto'
    try:
        page = requests.get(url)
    except:
        return 0

    soup = BeautifulSoup(page.text, 'html.parser')

    for row in soup.select('table.wikitable tbody tr'):
        columns = row.find_all('td')

        if len(columns) < 4:
            continue

        country_column = columns[1]

        if country_column.find('a'):
            for country in country_column.find_all('a'):
                if country.text == portuguese_country_name:
                    string = columns[3].get_text().replace(',', '.')
                    re_search = r'[\d]+[.,\d]+|[\d]*[.][\d]+|[\d]+'
                    numbers_in_string = re.findall(re_search, string)
                    points = [float(number) for number in numbers_in_string]
                    highest_point = max(points)
                    return highest_point

    return 0

def getImmigrantPercentage(country_name):
    translated_country_name = GoogleTranslator(
        source='auto', target='english').translate(text=country_name)
    url = 'https://en.wikipedia.org/wiki/List_of_sovereign_states_by_immigrant_and_emigrant_population'
    try:
        page = requests.get(url)
    except:
        return 0

    soup = BeautifulSoup(page.text, 'html.parser')

    for row in soup.select('table.wikitable tbody tr'):
        columns = row.find_all('td')

        if len(columns) < 3:
            continue

        country_column = columns[0]

        if country_column.find('a'):
            country = country_column.find('a').text
            if country == country_name or country == translated_country_name:
                immigrant_percentage = columns[2].get_text()
                return float(immigrant_percentage)

    return 0

def getIntentionalHomicideRate(country_name):
    translated_country_name = GoogleTranslator(
        source='auto', target='english').translate(text=country_name)
    url = 'https://en.wikipedia.org/wiki/List_of_countries_by_intentional_homicide_rate'
    try:
        page = requests.get(url)
    except:
        return 0

    soup = BeautifulSoup(page.text, 'html.parser')

    homicides_table = soup.find_all('table')[1]

    for row in homicides_table.select('tbody tr'):
        columns = row.find_all('td')

        if len(columns) < 2:
            continue

        country_column = columns[0]
        country = country_column.find('a').text.replace("*", '').strip()
        if country == country_name or country == translated_country_name:
            homicide_rate = columns[1].get_text()
            return float(homicide_rate)

    return 0

def getLiteracyRate(country_name):
    portuguese_country_name = GoogleTranslator(
        source='auto', target='pt').translate(text=country_name)
    url = 'https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_%C3%ADndice_de_alfabetiza%C3%A7%C3%A3o'
    try:
        page = requests.get(url)
    except:
        return 0

    soup = BeautifulSoup(page.text, 'html.parser')

    for row in soup.select('table.sortable.wikitable tbody tr'):
        columns = row.find_all('td')

        if len(columns) < 2:
            continue

        country_column = columns[0]

        if country_column.find('a'):
            country = country_column.find('a').text
            if country == portuguese_country_name:
                literacy_rate = columns[1].get_text()
                if literacy_rate == 'N/A':
                    return 0
                else:
                    return float(literacy_rate.replace(',', '.').replace('%', ''))

    return 0

def getNeighbours(country_name):
    translated_country_name = GoogleTranslator(
        source='auto', target='english').translate(text=country_name)
    url = 'https://en.wikipedia.org/wiki/List_of_countries_and_territories_by_number_of_land_borders'
    try:
        page = requests.get(url)
    except:
        return 0

    soup = BeautifulSoup(page.text, 'html.parser')

    for row in soup.select('table.wikitable tbody tr'):
        columns = row.find_all('td')

        if len(columns) < 5:    
            continue    

        country_column = columns[0]
        
        if country_column.find('a'):
            country = country_column.find('a').text
            if country == country_name or country == translated_country_name:
                neighbours = columns[4].get_text()
                return int(neighbours)

    return 0

def getPetroleumReserves(country_name):
    translated_country_name = GoogleTranslator(
        source='auto', target='english').translate(text=country_name)
    url = 'https://en.wikipedia.org/wiki/List_of_countries_by_proven_oil_reserves'
    try:
        page = requests.get(url)
    except:
        return 0

    soup = BeautifulSoup(page.text, 'html.parser')

    proven_reserves_table = soup.find_all('table')[1]

    for row in proven_reserves_table.select('tbody tr'):
        columns = row.find_all('td')

        if len(columns) < 1:
            continue

        country_column = row.find('th')
        country = country_column.find('a').text.replace("*", '').strip()

        if country == country_name or country == translated_country_name:
            petroleum_reserve = columns[0].get_text().replace(',','').replace('.00','')
            return float(petroleum_reserve)

    return 0

def getHdi(country_name):
    translated_country_name = GoogleTranslator(
        source='auto', target='english').translate(text=country_name)
    url = 'https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index'
    try:
        page = requests.get(url)
    except:
        return 0

    soup = BeautifulSoup(page.text, 'html.parser')

    hdi_table = soup.find_all('table')[1]

    for row in hdi_table.select('tbody tr'):
        columns = row.find_all('td')

        if len(columns) < 2:
            continue

        country_column = row.find('th')
        country = country_column.find('a').text

        if country == country_name or country == translated_country_name:
            if len(columns) > 2:
                hdi = columns[2].get_text()
            elif len(columns) == 2:
                upper_sibling_columns = row.find_previous_sibling('tr').find_all('td')
                hdi = upper_sibling_columns[2].get_text()
            return float(hdi)

    return 0

# CIA web scrap functions
def getCoastalDistance(country_name):
    translated_country_name = GoogleTranslator(
        source='auto', target='english').translate(text=country_name)
    url = 'https://www.cia.gov/the-world-factbook/field/coastline/'
    try:
        page = requests.get(url)
    except:
        return 0

    soup = BeautifulSoup(page.text, 'html.parser')

    countries = soup.select('.pb30')

    for country in countries:
        if country.h3:
            try:
                if country.h3.a.text == country_name:
                    coastal_distance = country.text.replace(country_name, '').replace('km', '').replace(',','').strip()
                elif country.h3.a.text == translated_country_name:
                    coastal_distance = country.text.replace(translated_country_name, '').replace('km', '').replace(',','').strip()
                return float(coastal_distance)
            except:
                return 0

    return 0

def getTotalArea(country_name):
    translated_country_name = GoogleTranslator(
        source='auto', target='english').translate(text=country_name)
    url = 'https://www.cia.gov/the-world-factbook/field/area/'
    try:
        page = requests.get(url)
    except:
        return 0

    soup = BeautifulSoup(page.text, 'html.parser')

    countries = soup.select('.pb30')

    for country in countries:
        if (country.h3 and (country.h3.a.text == country_name or country.h3.a.text == translated_country_name)):
            raw_areas_info = country.text
            start_pos = raw_areas_info.find(':') + 1
            final_pos = raw_areas_info.find('s')
            total_area = raw_areas_info[start_pos:final_pos].replace(',','').strip()
            try:
                return int(total_area)
            except:
                return 0
    return 0

def getLatAndLong(country_name):
    translated_country_name = GoogleTranslator(
        source='auto', target='english').translate(text=country_name)
    url = 'https://developers.google.com/public-data/docs/canonical/countries_csv'
    try:
        page = requests.get(url)
    except:
        return [0,0]

    soup = BeautifulSoup(page.text, 'html.parser')

    for row in soup.select('tr'):
        columns = row.find_all('td')

        if len(columns) < 4:    
            continue    

        country = columns[3].text
        
        if country == country_name or country == translated_country_name:
            latitude = float(columns[1].text)
            longitude = float(columns[2].text)
            return [latitude, longitude]

    return [0,0]

