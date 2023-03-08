
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import numpy as np
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
import time


option = Options ()
option.headless = True
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = option)
cont = 1


for cont in range (1,147):
    driver.get('https://www.chessgames.com/perl/chess.pl?page=' + str(cont) + '&pid=20719')
    element = driver.find_element (By.XPATH,'/html/body/p[2]/table[1]/tbody/tr/td/table[2]')
    html_content = element.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find(name = 'table')
    df_full = pd.read_html(str(table))
    df_full[0].to_csv('new.csv', sep=';', mode='a', header=False, index = False)
    
    # sorry for the shitty code, selenium and the structure of the site was messy and it was bugging quite a lot.




