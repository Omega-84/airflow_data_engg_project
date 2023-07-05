import requests
import sys
from bs4 import BeautifulSoup
import pandas as pd
import boto3
from io import StringIO

def car_etl():
    url = 'https://www.carpages.ca/used-cars/search/?fueltype_id%5B0%5D=3&fueltype_id%5B1%5D=7'
    page = requests.get(url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.text,'lxml')
        cols = ['Title','Description','KMs_driven','Color','Price','Link']
        df = pd.DataFrame(columns=cols)
        skipped = pd.DataFrame(columns=['Page','Posting_no'])
        count = 1
        while count<=15:
            post = soup.find_all('div',class_='media soft push-none rule')
            for i,j in enumerate(post):
                try:
                    ls = []
                    ls.append(j.find('div',class_='media__content').find('hgroup',class_='push-half--bottom').find('a').get('title').strip())
                    ls.append(j.find('div',class_='media__content').find('hgroup',class_='push-half--bottom').find('h5').text.strip())
                    ls.append("".join([i.text for i in j.find('div',class_='media__content').find_all('div',class_='grey l-column l-column--small-6 l-column--medium-4')[0].find_all('span',class_='number')]))
                    ls.append(j.find('div',class_='media__content').find_all('div',class_='grey l-column l-column--small-6 l-column--medium-4')[1].find('span').text.strip())
                    ls.append(j.find('div',class_='media__content').find('div',class_='l-column l-column--medium-4 push-none').find('strong').text.strip())
                    ls.append('https://www.carpages.ca' + j.find('a',class_='media__img media__img--thumb').get('href'))
                    df = pd.concat([df,pd.DataFrame([ls],columns=cols)])
                    # df = df.append(dict(zip(cols,ls)),ignore_index=True)
                except:
                    skipped = pd.concat([skipped,pd.DataFrame([])])
                    # skipped = skipped.append(dict(zip(['Page','Posting_no'],[count,i+1])),ignore_index=True)
                
            next_page = soup.find('a',{'title':'Next Page','class':'nextprev'})
            if next_page != None :
                url = "https://www.carpages.ca" + next_page.get('href')
            else:
                print("Pages ended")    
                break
            page = requests.get(url)
            soup = BeautifulSoup(page.text,'lxml')
            count += 1
    else:
        print("Cannot scrape this page. Kindly recheck the URL.")
    s3_client = boto3.client('s3')
    response = s3_client.list_buckets()
    dest = response['Buckets'][0]['Name']
    csv_buffer = StringIO()
    df.to_csv(csv_buffer,index=False)
    s3_resource = boto3.resource('s3')
    s3_resource.Object(dest, 'df.csv').put(Body=csv_buffer.getvalue())
