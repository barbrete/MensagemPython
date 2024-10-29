import urllib.parse
import pandas as pd
from selenium import webdriver as  wd
from selenium.webdriver.common.keys import Keys
import time
import urllib

contatos_tecnicos = pd.read_excel("ContatosTecnicos.xlsx")

navegador = wd.Chrome()
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements('id','side')) < 1:
    time.sleep(1)
    
for i, mensagem in enumerate(contatos_tecnicos['mensagem']):
    pessoa = contatos_tecnicos.loc[i,"nome"]    
    numero = contatos_tecnicos.loc[i,"numero"]
    texto = urllib.parse.quote(f"Olá {pessoa}, tudo bem? {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements('id','side')) < 1:
        time.sleep(10) 
    navegador.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div/p/span').send_keys(Keys.ENTER)
    time.sleep(2) 
