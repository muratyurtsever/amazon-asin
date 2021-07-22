from requests_html import HTMLSession
import pandas as pd

linkburayagelecek = 'https://www.amazon.com/s?k=Cigar+Humidor+Humidifiers&ref=nb_sb_noss'

url = linkburayagelecek

s = HTMLSession()
r = s.get(url)
r.html.render(sleep=1)
items = r.html.find('div[data-asin]')

asins = []

for item in items:
    if item.attrs['data-asin'] != '':
        asins.append(item.attrs['data-asin'])

products = []

for asin in asins:
    url = f'https://www.amazon.com/dp/{asin}'
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=0.3)

    title = r.html.find('#productTitle', first=True).full_text.strip()
    
    rating = r.html.find('span.a-icon-alt', first=True).full_text
 

    product = {
        'title': title,
    
        'rating': rating,
        
        }

    products.append(product)


    print( asin )

df = pd.DataFrame(products)
df.to_csv('ssd.csv', index=False)