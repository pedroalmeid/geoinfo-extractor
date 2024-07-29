import country_converter as coco
from deep_translator import GoogleTranslator

cc = coco.CountryConverter()

def getId(country_name):
    translated_country_name = GoogleTranslator(source='auto', target='english').translate(text=country_name)
    country_id = cc.convert(translated_country_name, to='ISO3')
    return country_id