import pyautogui
import time

def espera(segundos=2):
    time.sleep(segundos)

def clique(x,y,delay=2):
    print(f"Clicando em ({x},{y}) após {delay}s")
    espera(delay)
    pyautogui.click(x = x, y = y)

def doiscliques(x,y,delay=2):
    print(f"Dando dois cliques em ({x},{y}) após {delay}s")
    espera(delay)
    pyautogui.doubleClick(x = x, y = y) 

def abrir_site(nome_site, delay=2):
    espera(delay)
    pyautogui.write(nome_site)
    espera(delay)
    pyautogui.press('enter') 
    espera(3)

def escrever_gmail(gmailescrever, delay=2):
    espera(delay)
    pyautogui.write(gmailescrever)
    espera(delay)
    pyautogui.press('enter') 

def atividade(atividadeescrever, delay=2):
    espera(delay)
    pyautogui.write(atividadeescrever)
    espera(delay)

# sequência
clique(x=1811, y=20)          
doiscliques(x=50, y=948)     
clique(1862,21)
abrir_site('https:gmail.com')
clique(x=97, y=193)
clique(x=1418, y=994)
clique(x=115, y=198)
clique(x=544, y=163) 
doiscliques(x=788, y=501)
doiscliques(x=507, y=163)
doiscliques(x=281, y=322)
clique(x=1265, y=470)
# doiscliques(278,216)
# doiscliques(325,165)
# doiscliques(334,192)
# clique(279,333)
# clique(782,501)
# clique(1301,480)
escrever_gmail('mateusgn@to.senac.br')
clique(1765,539)
atividade('atividade de automação')
clique(1294,1001)