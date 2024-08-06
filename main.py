import direct_functions
import dynamic_pages_functions
import static_pages_functions

from pprint import pprint
import requests

countries = [
]

for country in countries:
    country_dictionary = {
        "id": direct_functions.getId(country),
        "name": country,
        "flag": "Flag URL",
        "capital_population": static_pages_functions.getCapitalPopulation(country),
        "coastal_distance": static_pages_functions.getCoastalDistance(country),
        "electricity_prod": static_pages_functions.getElectricityProd(country),
        "female_population": dynamic_pages_functions.getFemalePopulation(country),
        "forest_area": dynamic_pages_functions.getForestArea(country),
        "gdp": dynamic_pages_functions.getGdp(country),
        "gdp_per_capita": dynamic_pages_functions.getGdpPerCapita(country),
        "gini": dynamic_pages_functions.getGini(country),
        "gold_prod": static_pages_functions.getGoldProd(country),
        "hdi": static_pages_functions.getHdi(country),
        "highest_geographical_point": static_pages_functions.getHighestGeographicalPoint(country),
        "immigrant_percentage": static_pages_functions.getImmigrantPercentage(country),
        "intentional_homicide_rate": static_pages_functions.getIntentionalHomicideRate(country),
        "lat": static_pages_functions.getLatAndLong(country)[0],
        "life_expectancy": dynamic_pages_functions.getLifeExpectancy(country),
        "literacy_rate": static_pages_functions.getLiteracyRate(country),
        "long": static_pages_functions.getLatAndLong(country)[1],
        "male_population": dynamic_pages_functions.getMalePopulation(country),
        "neighbours": static_pages_functions.getNeighbours(country),
        "petroleum_reserves": static_pages_functions.getPetroleumReserves(country),
        "population_growth_rate": dynamic_pages_functions.getPopulationGrowthRate(country),
        "rural_population": dynamic_pages_functions.getRuralPopulation(country),
        "total_area": static_pages_functions.getTotalArea(country),
        "total_population": dynamic_pages_functions.getTotalPopulation(country),
        "ttdi_rank": direct_functions.getTtdiRank(country),
        "urbanization_rate": static_pages_functions.getUrbanizationRate(country)
    }

    pprint(country_dictionary)

    api_url = "http://localhost:4100/countries"
    response = requests.post(api_url, json=country_dictionary)

    if response.status_code == 201:
        print(f"{country} was created successfully on the database")
