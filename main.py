import static_pages_functions 
import dynamic_pages_functions
import direct_functions

countries = [
    'China',
    'Venezuela',
    'África do Sul',
    'Morocco',
    "Côte D'Ivoire",
]

for country in countries:
    print(f'''{country}: OK capital: {static_pages_functions.getCapitalPopulation(country)},
    OK id: {direct_functions.getId(country)},
    OK urbanization_rate: {static_pages_functions.getUrbanizationRate(country)},
    OK electricity_prod: {static_pages_functions.getElectricityProd(country)},
    OK gold_prod: {static_pages_functions.getGoldProd(country)},
    OK highest_geographical_point: {static_pages_functions.getHighestGeographicalPoint(country)},
    OK immigrant_percentage: {static_pages_functions.getImmigrantPercentage(country)},
    OK intentional_homicide_rate: {static_pages_functions.getIntentionalHomicideRate(country)},
    OK literacy_rate: {static_pages_functions.getLiteracyRate(country)},
    OK neighbours: {static_pages_functions.getNeighbours(country)},
    OK petroleum_reserves: {static_pages_functions.getPetroleumReserves(country)},
    OK coastal_distance: {static_pages_functions.getCoastalDistance(country)}
    OK total_area: {static_pages_functions.getTotalArea(country)},
    female_population: {dynamic_pages_functions.getFemalePopulation(country)}
    ''')

'''
[] Criar uma lista com todos os países
[] Criar todas as funções de web scrap (para cada categoria)
[] Configurar as funções de web scrap para preencher a categoria
com valor 0 caso haja falha na obtenção da informação
[] Configurar as funções de web scrap para lidar com nomes 
traduzidos de países em casos específicos
[] Pensar em separar as funções de web scrap para sites estáticos e 
dinâmicos em arquivos diferentes (um usa selenium e outro não)
[] Para cada item da lista (cada país) montar o dicionário com todas
as categorias e respectivos valores extraídos pelas funções de web scrap
[] Realizar requisição de criação de país para a API REST para criar o país 
automaticamente no banco de dados
'''
