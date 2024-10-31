#para esse código funcionar, é necessário ter o whatsapp instalado e os contatos salvos

import pandas as pd
import time
import pyautogui as pag

pag.alert('Favor não usar o mouse ou o teclado enquanto o código executa.')

pag.press('winleft')
time.sleep(1)

pag.write('whatsapp')
time.sleep(2)

pag.press('enter')
time.sleep(1)
contatos = pd.read_excel("Contatos.xlsx")

for i, mensagem in enumerate(contatos['mensagem']):
    pessoa = contatos.loc[i,"nome"]    
    numero = contatos.loc[i,"numero"]
    time.sleep(3)
    pag.hotkey('ctrl','f') 
    time.sleep(1)   
    pag.write(str(pessoa))
    time.sleep(2)
    pag.press('tab')
    pag.press('enter')
    time.sleep(1)
    pag.write(str(mensagem))
    pag.write(str(pessoa))
    pag.press('enter')
    time.sleep(3)

pag.alert('Código finalizado.')
