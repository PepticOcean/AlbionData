import pandas as pd
import requests

def import_API(imonth = 1, iday = 1, iyear = 2000, fmonth = 12, fday = 31, fyear = 2999, server = 'west'):

    #Requisitando as informações por meio da api on-line
    url = f'https://{server}.albion-online-data.com/api/v2/stats/gold.json?date={imonth}-{iday}-{iyear}&end_date={fmonth}-{fday}-{fyear}'
    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data)
    df.to_csv('Gold.csv', index=False)
    
import_API()