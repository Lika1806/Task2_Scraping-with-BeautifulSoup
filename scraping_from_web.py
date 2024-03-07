from bs4 import BeautifulSoup
from my_requests import get_text
import pandas as pd

url  = 'https://webscraper.io/test-sites/e-commerce/allinone'

soup = BeautifulSoup(get_text(url), 'html')

items = soup.find_all('div', class_="card-body")
all_info = [None]*len(items)

for i,item in enumerate(items):
    name = item.find('a').text
    price = item.find('h4', class_='float-end price card-title pull-right').text
    
    pars = item.find_all('p')
    description = pars[0].text
    review_count = pars[1].text.split()[0]
    rating = pars[2]['data-rating']
    all_info[i] = [name, price, description, review_count, rating]

new_df = pd.DataFrame(all_info, columns = ['title', 'price', 'description', 'raview_count', 'rating'])
new_df.to_csv('top_item_list.txt',index=False)
