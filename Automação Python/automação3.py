import pyautogui
import time

def espera(segundos=2):
    time.sleep(segundos)


def clique(x,y,delay=2):
    espera(delay)
    pyautogui.click(x = x, y = y)

def dois_clique(x,y,delay=2):
    espera(delay)
    pyautogui.doubleClick(x = x, y = y)

def abrir_site(nome_site, delay=2):
    espera(delay)
    pyautogui.write(nome_site)
    espera(delay)
    pyautogui.press('enter')
    espera(1)


#verifique os cursos do SENAC em taquaralto

clique(x=1811, y=8)
dois_clique(x=11, y=540)
abrir_site('https://www.to.senac.br/')
clique(x=1180, y=207)
clique(x=1259, y=371)