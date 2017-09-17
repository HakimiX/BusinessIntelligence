import bs4
import requests
import csv
import os
import re
from tqdm import tqdm


def scrape(url):

    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content.decode('utf-8'), "html5lib")

    table = soup.find('table')
    table_body = table.find('tbody')

    a_tags = table_body.find_all('a')
    del a_tags[:5]

    a_tags = [a.text for a in a_tags]

    return a_tags


# Scrapes all data from a single page
def scrape_housing_data(url):

    data = []

    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content.decode('utf-8'), 'html5lib')

    table = soup.find('table')
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')

        # Decode address column
        a_tags = cols[0].find_all('a')
        line = re.sub(r'<br/>', '\n', str(a_tags[0]))
        _, line, _ = line.split('>')
        line, _ = line.split('<')
        # Split the two values
        street, town = line.split('\n')
        # Split the two values
        zip_code, city = town.split(' ', 1)
        int(zip_code)

        # Decode number of rooms
        no_rooms_str = cols[4].text.strip()
        # Exception handling
        try:
            no_rooms = int(no_rooms_str)
        except:
            no_rooms = None

        # Decode selling date and type
        size_in_sq_m_str = cols[6].text.strip()
        # Exception handling
        try:
            size_in_sq_m = int(size_in_sq_m_str)
        except:
            size_in_sq_m = None

        # Decode year of construction
        year_of_construction_str = cols[7].text.strip()
        # Exception handling
        try:
            year_of_construction = int(year_of_construction_str)
        except:
            year_of_construction = None

        # Decode price
        price_str = cols[1].text.strip()
        # Exception handling
        try:
            price = float(price_str.replace('.', ''))
        except:
            price = None

        # Decode sales date
        sale_date_str = cols[2].text.strip()
        sale_date = sale_date_str[:10]

        decoded_row = (street, city, zip_code, no_rooms,
                       size_in_sq_m, year_of_construction, price,
                       sale_date)
        data.append(decoded_row)

    return data


def save_data(base_url, urls):
    response = []
    for url in urls:
        u = os.path.join(base_url, url)
        response += scrape_housing_data(u)
    save_to_file = os.path.join(out_dir, os.path.basename(url).split('_')[0] + '.csv')
    save_to_csv(response, save_to_file)


# Saving scraped HTML data into CSV
def save_to_csv(data, path='./out/boliga.csv'):

    with open(path, 'w', encoding='utf-8') as output_file:
        output_writer = csv.writer(output_file)
        output_writer.writerow(['street', 'city', 'zipcode',
                                'no_rooms', 'size_in_sq_m',
                                'year_of_construction', 'price',
                                'sale_date_str'])

        for row in data:
            output_writer.writerow(row)


def run():

    base_url = 'http://138.197.184.35/boliga/'
    urls = scrape(base_url)
    temp_list = []
    count = 0

    for i in tqdm(urls, desc='saving'):
        _, number = i.split('_')
        number, _ = number.split('.')
        num = int(number)
        temp_val = count + 1
        if num == temp_val:
            temp_list.append(i)
            count += 1
        else:
            save_data(base_url, temp_list)
            temp_list = []
            count = 1
            temp_list.append(i)

    save_data(base_url, temp_list)


out_dir = './data/out'
if not os.path.exists(out_dir):
    os.mkdir(out_dir)
run()
