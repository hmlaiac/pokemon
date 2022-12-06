import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
class Crawler:
    def __init__(self):
        self.df = None

    def download_9th_pokemon(self, link):
        response = requests.get(link)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Locate to <table> of webpage
        tables = soup.find_all("table")
        
        # Select the row in table
        trs = []
        for table in tables:
            trs.extend(table.find("tbody").find_all("tr"))
        
        # Convert the data to DataFrame
        columns = ["ORI_DEX", "DEX", "URL", "CNT_NAME"]
        df = pd.DataFrame(columns=columns)
        print(df.columns)
        for tr in trs:
            sels = tr.select("td")
            if sels and re.match(r'#[0-9]',sels[0].text):
                ORI_DEX = sels[0].text[1:-1]
                DEX = sels[1].text[1:-1]
                URL = sels[2].find("a").get('href')
                CNT_NAME = sels[3].text[0:-1]
                df = df.append(pd.Series(data={"ORI_DEX":ORI_DEX,
                                      "DEX":DEX,
                                      "URL":URL,
                                      "CNT_NAME":CNT_NAME}), ignore_index=True)
        self.df = df
                                      
        return df

    def to_csv(self, path):
        self.df.to_csv(path)
        