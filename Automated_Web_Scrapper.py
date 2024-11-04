
from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
from datetime import datetime
import time


def automated_crypto_pull():
    url = 'https://coinmarketcap.com/currencies/bitcoin/'
    
    page = requests.get(url)
    
    soup = BeautifulSoup(page.text,'html')
    
    crypto_name = soup.find('span', class_ = 'sc-65e7f566-0 lsTl').text
    
    crypto_price = soup.find('span', {'data-test': 'text-cdp-price-display'}).text
    final_price = crypto_price.replace('$','')
    
    date_time = datetime.now()
    
    date_time = datetime.now()
    
    dict = {'Crypto Name':crypto_name,
            'Price':final_price,
           'TimeStamp':date_time}
    
    df = pd.DataFrame([dict])
    
    import os
    
    if os.path.exists(r'C:\Users\RS-2100\Desktop\Portfolio\Python\Crypto_Automated_Pull.csv'):
        df.to_csv(r'C:\Users\RS-2100\Desktop\Portfolio\Python\Crypto_Automated_Pull.csv',mode = 'a', header = False, index = False)
    else:
        df.to_csv(r'C:\Users\RS-2100\Desktop\Portfolio\Python\Crypto_Automated_Pull.csv')
    print(df)


while True:
    automated_crypto_pull()
    time.sleep(3600)