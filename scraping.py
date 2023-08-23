from bs4 import BeautifulSoup
import requests
import pandas as pd



def scrap_etenders(link='https://etenders.gov.in/eprocure/app'):
    link = requests.get('https://etenders.gov.in/eprocure/app').text
    soup = BeautifulSoup(link, 'html.parser')

    title_tender = []
    tender_id = []
    opening_date = []
    closing_date = []

    table = soup.find('table', {'class': "list_table"})
    table_row = table.find('tr', {'class': 'list_header'})
    count = 0
    for inside in table.find_all('tr', {'class': ['even', 'odd']}):
        count += 1
        title_tender.append(inside.find_all("td")[0].text)
        tender_id.append(inside.find_all("td")[1].text)
        opening_date.append(inside.find_all("td")[2].text)
        closing_date.append(inside.find_all("td")[3].text)

    #print(title_tender)
    #print(tender_id)
    #print(opening_date)
    #print(closing_date)
    df = pd.DataFrame({
        "Tender Title": title_tender,
        "Reference No": tender_id,
        "Closing Date": opening_date,
        "Bid Opening Date": closing_date
        })

    df.to_csv('Tender_Data.csv', index=False)
    print("Data extracted and saved in DATA.csv")



def cpppc_scraper(link='https://www.cpppc.org/en/PPPyd.jhtml'): #China Public Private Partnerships Center
    link_to_scrape = requests.get(link).text
    soup = BeautifulSoup(link_to_scrape, 'html.parser')
    title = []
    content = []
    ul_data = soup.find('ul', {'class': "new-content ppp-list"})
    for li_data in ul_data.find_all('li'):
        a = li_data.a.text
        title.append(a)
        for div_data in li_data.find_all('div'):
            b = div_data.text
            content.append(b)

    df =pd.DataFrame( {'titles': title, 'Content': content})
    df.to_csv('results.csv', index=False)
    print("Data extracted and saved in RESULTS.csv")


def wbg_screper(link='https://ieg.worldbankgroup.org/data'):
    link_to_scrape  = requests.get(link)
    soup = BeautifulSoup(link_to_scrape.text, 'html.parser')

    div_content = soup.find('div', {'class': 'views-field views-field-body'})

    for table_data in div_content.find_all('tr'):
        print(table_data.text, end='')
        print('====' * 10)

scrap_etenders()
cpppc_scraper()
