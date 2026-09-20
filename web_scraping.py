from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

#need to add headers to respect wikis robot policies *sigh*
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

#print(soup)

#html of the table we are interested in 
#<table class="wikitable sortable sticky-header-multi sort-under jquery-tablesorter" 
#style="text-align:left;" id="mwMQ">

table = soup.find_all('table')[0]

'''
with open('op.txt', 'w') as f:
    print(table, file=f)
'''

titles = table.find_all('th')
table_titles = [_.text.strip() for _ in titles]
#print(table_titles)

df = pd.DataFrame(columns=table_titles)

col_data = table.find_all('tr')

for row in col_data[1:]:
    data = row.find_all('td')
    row_data = [_.text.strip() for _ in data]

    length = len(df)
    df.loc[length] = row_data

#print(df)

df.to_csv(r'C:/Users/Apala/Documents/Data_analysis/op.csv', index=False)