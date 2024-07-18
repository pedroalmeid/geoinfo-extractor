'''
Prováveis pacotes necessários:
import country_converter as coco
from deep_translator import (GoogleTranslator) 
from bs4 import BeautifulSoup
import requests as r'''


countries = ['Brazil']

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
