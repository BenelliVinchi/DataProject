from bs4 import BeautifulSoup
import requests
import pandas as pd
html_text = requests.get("https://www.scrapethissite.com/pages/simple/").text
souped_html = BeautifulSoup(html_text, 'lxml')
countries = souped_html.find_all('h3')
country_capital_list = souped_html.find_all('span', class_="country-capital")
population_list = souped_html.find_all('span', class_="country-population")
area_km2_list = souped_html.find_all('span', class_="country-area")

country_data = []

for country, capital, population, area_km2 in zip(countries, country_capital_list, population_list, area_km2_list):
    country_data.append({
        "country": country.text.strip(),
        "capital": capital.text.strip(),
        "population": population.text.strip(),
        "area_km2": area_km2.text.strip()
    })

df = pd.DataFrame(country_data)
print(df)
