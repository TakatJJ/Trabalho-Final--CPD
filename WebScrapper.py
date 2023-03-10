
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import numpy as np
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
from pathlib import Path
import time


option = Options ()
option.headless = True
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = option)
cont = 1
class Players : #class that represent each player.
    name = 'default'
    ID = '0'
    endOfTable = 100
    def __init__(self,name,ID,endOfTable):
        print("Init was called")
        self.name = name
        self.ID = ID
        self.endOfTable = endOfTable
    


dictPlayers ={
    # 'Karpov' : ["Karpov", '20719', 148],
    # 'Magnus' : ["Magnus", '52948', 178],   DOES NOT WORK
    # 'Kasparov': ['Kasparov', '15940', 99],
    # 'Fischer' : ['Bobby Fischer', '19233', 45]
    'Karpov' : Players('Karpov', '20719', 148), # Dict to generalizate the function calling.
    'Magnus' : Players('Magnus', '52948', 178),
    'Kasparov': Players('Kasparov', '15940', 99),
    'Fischer' : Players('B.Fischer', '19233', 45)
}

def FindAllGames(name, ID,EOT):
    patch = Path('./'+ name +'.csv') # Certificates the file doens't get written once it already exists
    if patch.is_file():
        return
    else: 
        for cont in range (1,int(EOT)):
            driver.get('https://www.chessgames.com/perl/chess.pl?page=' + str(cont) + '&pid='+ ID +'')
            element = driver.find_element (By.XPATH,'/html/body/p[2]/table[1]/tbody/tr/td/table[2]')
            html_content = element.get_attribute('outerHTML')
            soup = BeautifulSoup(html_content, 'html.parser')
            table = soup.find(name = 'table')
            df_full = pd.read_html(str(table))
            df_full[0].to_csv( name+'.csv', sep=';', mode='a', header=False, index = False)
        
        # sorry for the shitty code, selenium and the structure of the site was messy and it was bugging quite a lot.

for player in dictPlayers:
    
    FindAllGames(dictPlayers[player].name,dictPlayers[player].ID, (dictPlayers[player].endOfTable)) # Get's all the names within the dictionary.


