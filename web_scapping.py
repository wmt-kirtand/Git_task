import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs

url = 'https://wmt-kirtand.github.io/Git_task/'

r = requests.get(url)

soup = bs(r.content, 'html.parser')

img_tags = soup.find_all('img')

png_images = [img['src'] for img in img_tags if img['src'].endswith('.png')]

for img_url in png_images:
    full_img_url = urljoin(url, img_url)
    img_data = requests.get(full_img_url).content
    img_name = full_img_url.split('/')[-1]
    with open(f'scraped_images/{img_name}', 'wb') as img_file:
        img_file.write(img_data)
    
    print(f'Saved: {img_name}')
