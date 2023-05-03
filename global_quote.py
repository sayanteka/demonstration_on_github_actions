
import os
import requests
import pandas as pd


def dataframe():

    stock_symbol=['TATASTEEL','TATACOMM','YESBANK','IDFCFIRSTB']
    try:
       API_KEY = os.environ["API_KEY"]
       print(api_key)
    except KeyError:
        api_key = "Token not available!"
    #api_key=os.environ.get('API_KEY')
    data_dict={}
    d=pd.DataFrame()
    for stock in stock_symbol:
        url=url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}.BSE&outputsize=full&apikey={}'.format(stock, API_KEY)

        response = requests.get(url)
        
        data = response.json()["Global Quote"]
        for key, value in data.items():
            key = key.split(". ")[-1]
            data_dict[key] = [value]
        df=pd.DataFrame(data_dict)
        d=d.append(df,ignore_index=True)
    d.to_excel('df_final.xlsx')
dataframe()    

