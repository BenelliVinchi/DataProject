from bs4 import BeautifulSoup
import requests
import pandas as pd
html_text = requests.get("https://www.scrapethissite.com/pages/simple/").text
souped_html = BeautifulSoup(html_text,'lxml')
country_capital_list = souped_html.find_all('span', class_="country-capital")

for each_capital in country_capital_list:
    print(each_capital.text.strip())
countries = souped_html.find_all('h3')
df= pd.DataFrame({
    
    "countries":[each_country.text.strip() for each_country in countries],
    "capitals":[each_capital.text.strip() for each_capital in country_capital_list]})



print(df)