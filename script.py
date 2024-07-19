import country_converter as coco
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

def getCapitalPopulation(country_name):
    translated_country_name = GoogleTranslator(source='auto', target='english').translate(text=country_name)
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
    translated_country_name = GoogleTranslator(source='auto', target='english').translate(text=country_name)
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

        country = country_column.find('a').text.strip() if country_column.find('a') else False
        if country == country_name or country == translated_country_name:
            urbanization_rate = columns[3].get_text()
            return float(urbanization_rate)

    return 0

def getElectricityProd(country_name):
    translated_country_name = GoogleTranslator(source='auto', target='english').translate(text=country_name)
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
            country = country_column.find('a').text.strip()
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
            country = country_column.find('a').text.strip()
            if country == country_name:
                gold_prod = columns[2].get_text().replace(',', '')
                return int(gold_prod)

    return 0

countries = [
    'China', 
    'Iran',
    "Côte D'Ivoire",
    'United States'
]

for country in countries:
    print(f'''{country}: capital: {getCapitalPopulation(country)},
    urbanization_rate: {getUrbanizationRate(country)},
    electricity_prod: {getElectricityProd(country)},
    gold_prod: {getGoldProd(country)}
    ''')


'''
[] Criar uma lista com todos os países
[] Criar todas as funções de web scrap (para cada categoria)
[] Configurar as funções de web scrap para preencher a categoria
com valor 0 caso haja falha na obtenção da informação
[] Configurar as funções de web scrap para lidar com nomes 
traduzidos de países em casos específicos
[] Para cada item da lista (cada país) montar o dicionário com todas
as categorias e respectivos valores extraídos pelas funções de web scrap
[] Realizar requisição de criação de país para a API REST para criar o país 
automaticamente no banco de dados
'''
