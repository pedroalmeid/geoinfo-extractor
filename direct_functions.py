import country_converter as coco
from deep_translator import GoogleTranslator

cc = coco.CountryConverter()

def getId(country_name):
    translated_country_name = GoogleTranslator(source='auto', target='english').translate(text=country_name)
    country_id = cc.convert(translated_country_name, to='ISO3')
    return country_id

def getTtdiRank(country_name):
    translated_country_name = GoogleTranslator(source='auto', target='english').translate(text=country_name)

    rank = ['United States', 'Spain', 'Japan', 'France', 'Australia', 'Germany', 'United Kingdom', 'China', 'Italy', 'Switzerland', 'Canada', 'Portugal', 'Singapore', 'South Korea', 'Austria', 'Netherlands', 'Denmark', 'United Arab Emirates', 'Sweden', 'Finland', 'Greece', 'Indonesia', 'Belgium', 'Ireland', 'New Zealand', 'Brazil', 'Poland', 'Luxembourg', 'Turkiye', 'Cyprus', 'Chile', 'Iceland', 'Czech Republic', 'Malta', 'Malaysia', 'Estonia', 'Hungary', 'Mexico', 'India', 'Bulgaria', 'Saudi Arabia', 'Slovenia', 'Romania', 'Lithuania', 'Georgia', 'Croatia', 'Thailand', 'Israel', 'Argentina', 'Colombia', 'Costa Rica', 'Kazakhstan', 'Qatar', 'Slovakia', 'South Africa', 'Azerbaijan', 'Mauritius', 'Bahrain', 'Vietnam', 'Montenegro', 'Egypt', 'Peru', 'Panama', 'Dominican Republic', 'Latvia', 'Albania', 'Oman', 'Serbia', 'Philippines', 'Jordan', 'Uruguay', 'Armenia', 'Iran', 'Barbados', 'Botswana', 'Sri Lanka', 'Kenya', 'Uzbekistan', 'Lebanon', 'Ecuador', 'Tanzania', 'Morocco', 'Tunisia', 'Jamaica', 'Mongolia', 'Cambodia', 'North Macedonia', 'Moldova', 'Trinidad and Tobago', 'Bosnia and Herzegovina', 'Laos', 'Paraguay', 'Rwanda', 'Bolivia', 'Namibia', 'Kuwait', 'El Salvador', 'Algeria', 'Tajikistan', 'Guatemala', 'Pakistan', 'Kyrgyz Republic', 'Venezuela', 'Zambia', 'Nepal', 'Ghana', 'Senegal', 'Nicaragua', 'Bangladesh', 'Zimbabwe', 'Honduras', 'Nigeria', 'Benin', 'Ivory Coast', 'Malawi', 'Angola', 'Cameroon', 'Sierra Leone', 'Mali']

    position = 0

    if country_name in rank:
        position = rank.index(country_name) + 1
    elif translated_country_name in rank:
        position = rank.index(translated_country_name) + 1
    
    return position

