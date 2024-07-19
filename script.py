import country_converter as coco
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator


def getCapitalPopulation(countryName):
    url = 'https://en.wikipedia.org/wiki/List_of_national_capitals_by_population'
    page = requests.get(url).text

    soup = BeautifulSoup(page, 'html.parser')

    for item in soup.select('table.wikitable tbody tr td a'):
        name = item.text.replace("*",'').strip() if '*' in item.text else item.text.strip()
        next_td = item.parent.find_next_sibling('td')
        previous_td = item.parent.find_previous_sibling('td')

        if (countryName == name) and ((countryName not in previous_td.get_text()) if previous_td else True):
            population = next_td.find_next_sibling('td').get_text()
            population = int(population.replace(',', '')) if (',' in population) else int(population)
            return population

    return 0

countries = [
    'Equatorial Guinea',
    'Guinea',
    'Guinea Bissau',
    'Papua New Guinea',
]

for country in countries:
    print(getCapitalPopulation(country))


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
