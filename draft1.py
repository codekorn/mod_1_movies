import requests
import pandas as pd


def bom_db(year):
    url = 'https://www.boxofficemojo.com/yearly/chart/?view2=worldwide&yr=' + str(year)+'&p=.htm'
    r = pd.read_html(requests.get(url).content)
    test_df = r[1]
    df = test_df.iloc[:,0:8]

    df.columns = ['Rank', 'Title', 'Studio', 'Worldwide Gross', 'Domestic Gross',
                   'Domestic %','Overseas Gross' ,'Overseas %']

    df['Year'] = year
    df.drop([0,1,2], inplace=True)
    df.reset_index(inplace=True)
    df.drop(columns=['index', 'Rank'], inplace=True)
    return df
