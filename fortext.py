from time import sleep
import pandas as pd
import pytest
import time
import json
from selenium import webdriver
from datetime import datetime as dt
from selenium.webdriver.chrome import service
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from configobj import ConfigObj

#login
config  = ConfigObj('config.txt')
usuario = config['LOGIN']['usuario']
senha   = config['LOGIN']['senha']

#input parameters
valor_entrada = float(config['PARAMETERS']['valor_entrada'])
auto_retirar  = float(config['PARAMETERS']['auto_retirar'])

#martingale parameters
usar_mg = config['MARTINGALE']['usar_martingale']
fator_mg = config['MARTINGALE']['fator_martingale']
niveis_mg = config['MARTINGALE']['niveis_martingale']
entrada_gale1 = int(valor_entrada) * float(fator_mg)
entrada_gale2 = float(entrada_gale1) * float(fator_mg)
entrada_gale3 = float(entrada_gale2) * float(fator_mg)
entrada_gale4 = float(entrada_gale3) * float(fator_mg)
entrada_gale5 = float(entrada_gale4) * float(fator_mg)
entrada_gale6 = float(entrada_gale5) * float(fator_mg)
entrada_gale7 = float(entrada_gale6) * float(fator_mg)
entrada_gale8 = float(entrada_gale7) * float(fator_mg)
entrada_gale9 = float(entrada_gale8) * float(fator_mg)
entrada_gale10 = float(entrada_gale9) * float(fator_mg)

if config['MARTINGALE']['usar_martingale'] == 'SIM':
    martingale = int(config['MARTINGALE']['niveis_martingale'])
else:
    martingale = 0

resultado_final = []
check_resultado_final = []    
    
entrada = True
green = False
gale_1 = False
green_gale_1 = False
gale_2 = False
green_gale_2 = False
gale_3 = False
green_gale_3 = False
gale_4 = False
green_gale_4 = False
gale_5 = False
green_gale_5 = False
loss = False

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0"}

driver = webdriver.Chrome()
driver.get('https://888bets.co.mz/pt/games/detail/casino/demo/7787')
sleep(10)
'''
print('Actualizando site...')
#driver.refresh()
print('Iniciando Conexao...')
sleep(6)
botao_entrar_path = "//div[@class='logout-menu right']//a[@class='login-btn mr-right']"
driver.find_element(By.XPATH, botao_entrar_path).click()
sleep(4)
usuario_path = "//input[@placeholder='82 123 4567']"
driver.find_element(By.XPATH, usuario_path).send_keys(usuario)
sleep(0.1)
senha_path = "//input[@placeholder='Palavra-passe']"
driver.find_element(By.XPATH, senha_path).send_keys(senha)
sleep(0.1)
manter_path = "//label[@for='keepLogin']"
driver.find_element(By.XPATH, manter_path).click()
sleep(0.1)
login_path = "//button[@data-test='sign-in-modal-btn']"
driver.find_element(By.XPATH, login_path).click()
print('Botao de login clicado')
sleep(5)
'''
print('Acessando aviator...')
'''
aviator_path = "//a[@data-test='header-menu-button-aviator']"
driver.find_element(By.XPATH, aviator_path).click()
'''
while len(driver.find_elements(By.XPATH, "//iframe[@class='iframeDefaultSize']")) == 0:
    sleep(0.1)

iframe_path = "//iframe[@class='iframeDefaultSize']"
iframe = driver.find_element(By.XPATH, iframe_path)
sleep(5)
driver.switch_to.frame(iframe)

while len(driver.find_elements(By.XPATH,"/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[3]")) == 0:
    sleep(0.5)
    
#apostar lado A
auto_btn_path = ".navigation:nth-child(1) .tab:nth-child(3)"
driver.find_element(By.CSS_SELECTOR, auto_btn_path).click()
sleep(0.1)

auto_retirar_btn_path = ".second-row:nth-child(4) .input-switch"
driver.find_element(By.CSS_SELECTOR, auto_retirar_btn_path).click()
sleep(0.1)

valor_entrada_path = ".first-row:nth-child(2) .font-weight-bold"
driver.find_element(By.CSS_SELECTOR, valor_entrada_path).send_keys(u'\ue009' + u'\ue003')
driver.find_element(By.CSS_SELECTOR, valor_entrada_path).send_keys(valor_entrada)
sleep(0.1)

auto_retirar_path = ".ng-valid > .small .font-weight-bold"
driver.find_element(By.CSS_SELECTOR, auto_retirar_path).send_keys(u'\ue009' + u'\ue003')
driver.find_element(By.CSS_SELECTOR, auto_retirar_path).send_keys(auto_retirar)
sleep(0.1)

'''
#apostar lado B
auto_btn_path = ".navigation:nth-child(2) .tab:nth-child(3)"
driver.find_element(By.CSS_SELECTOR, auto_btn_path).click()
sleep(0.1)

auto_retirar_btn_path = ".second-row:nth-child(5) .input-switch"
driver.find_element(By.CSS_SELECTOR, auto_retirar_btn_path).click()
sleep(0.1)

valor_entrada_path = ".first-row:nth-child(3) .font-weight-bold"
driver.find_element(By.CSS_SELECTOR, valor_entrada_path).send_keys(u'\ue009' + u'\ue003')
driver.find_element(By.CSS_SELECTOR, valor_entrada_path).send_keys(valor_entrada)
sleep(0.1)

auto_retirar_path = ".ng-valid > .small .font-weight-bold"
driver.find_element(By.CSS_SELECTOR, auto_retirar_path).send_keys(u'\ue009' + u'\ue003')
driver.find_element(By.CSS_SELECTOR, auto_retirar_path).send_keys(auto_retirar)
sleep(2)
'''

print("Pegando ultimos resultados...")

while len(driver.find_elements(By.XPATH, "/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[1]/app-stats-widget/div/div[1]")) == 0:
    sleep(0.1)

minutos = float(dt.now().strftime('%M.%S')[1:])

def resultado():
    global resultado_final

    resultado = driver.find_element(By.XPATH, "/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[1]/app-stats-widget/div/div[1]").text

    lista = []
    resultado_final = []

    lista = resultado.split()

    for x in range(len(lista[0:5])):
        numero = lista[x].translate(str.maketrans('', '', 'x'))
        resultado_final.append(float(numero))

    return resultado_final
    sleep(0.5)
    
#botao apostar lado A  
apostar_path_1 = ".auto-game .d-flex"
#botao apostar lado A 
apostar_path_2 = ".first-row:nth-child(3) .label"


def estrategia(resultado):
    global entrada
    global green
    global gale_1
    global green_gale_1
    global gale_2
    global green_gale_2
    global gale_3
    global green_gale_3
    global gale_4
    global green_gale_4
    global gale_5
    global green_gale_5
    global gale_6
    global green_gale_6
    global gale_7
    global green_gale_7
    global gale_8
    global green_gale_8
    global gale_9
    global green_gale_9
    global green_gale_10
    global loss

    if resultado[0] < 5.0 and entrada == True:
        print(f"ENTRAR APOS VELA {resultado[0]}")
        driver.find_element(By.CSS_SELECTOR, apostar_path_1).click()
        entrada = False
        green = True
        gale_1 = True
        gale_2 = True
        gale_3 = True
        gale_4 = True
        gale_5 = True
    
    elif resultado[0] >= float(auto_retirar) and green == True:
        entrada = True
        green = False
        gale_1 = False
    
    elif resultado[0] < auto_retirar and gale_1 == True:
        valor_gale1_path = ".first-row:nth-child(2) .font-weight-bold"
        driver.find_element(By.CSS_SELECTOR, valor_gale1_path).send_keys(u'\ue009' + u'\ue003')
        driver.find_element(By.CSS_SELECTOR, valor_gale1_path).send_keys(entrada_gale1)
        driver.find_element(By.CSS_SELECTOR, apostar_path_1).click()
        print('Entrada no GALE 1')
        green = False
        gale_1 = False
        green_gale_1 = True

    elif resultado[0] >= auto_retirar and green_gale_1 == True:
        valor_entrada_path = ".first-row:nth-child(2) .font-weight-bold"
        driver.find_element(By.CSS_SELECTOR, valor_entrada_path).send_keys(u'\ue009' + u'\ue003')
        driver.find_element(By.CSS_SELECTOR, valor_entrada_path).send_keys(valor_entrada)
        entrada = True
        green = True
        green_gale_1 = False
        gale_2 = False
        #gale_3 = False
    
    elif resultado[0] < auto_retirar and gale_2 == True:
        valor_gale2_path = ".first-row:nth-child(2) .font-weight-bold"
        driver.find_element(By.CSS_SELECTOR, valor_gale2_path).send_keys(u'\ue009' + u'\ue003')
        driver.find_element(By.CSS_SELECTOR, valor_gale2_path).send_keys(entrada_gale2)
        driver.find_element(By.CSS_SELECTOR, apostar_path_1).click()
        print('Entrada no GALE 2')
        green_gale_2 = True
        gale_2 = False

    elif resultado[0] >= auto_retirar and green_gale_2 == True:
        valor_entrada_path = ".first-row:nth-child(2) .font-weight-bold"
        driver.find_element(By.CSS_SELECTOR, valor_entrada_path).send_keys(u'\ue009' + u'\ue003')
        driver.find_element(By.CSS_SELECTOR, valor_entrada_path).send_keys(valor_entrada)
        entrada = True
        green = True
        green_gale_2 = False
        gale_3 = False
    
    elif resultado[0] < auto_retirar and gale_3 == True:
        valor_gale2_path = ".first-row:nth-child(2) .font-weight-bold"
        driver.find_element(By.CSS_SELECTOR, valor_gale2_path).send_keys(u'\ue009' + u'\ue003')
        driver.find_element(By.CSS_SELECTOR, valor_gale2_path).send_keys(entrada_gale3)
        driver.find_element(By.CSS_SELECTOR, apostar_path_1).click()
        print('Entrada no GALE 3')
        green_gale_3 = True
        gale_3 = False
        
    elif resultado[0] >= auto_retirar and green_gale_3 == True:
        valor_entrada_path = ".first-row:nth-child(2) .font-weight-bold"
        driver.find_element(By.CSS_SELECTOR, valor_entrada_path).send_keys(u'\ue009' + u'\ue003')
        driver.find_element(By.CSS_SELECTOR, valor_entrada_path).send_keys(valor_entrada)
        entrada = True
        green = True
        green_gale_3 = False
        gale_3 = False
        gale_4 = False
        
    elif resultado[0] < auto_retirar and gale_4 == True:
        valor_gale2_path = ".first-row:nth-child(2) .font-weight-bold"
        driver.find_element(By.CSS_SELECTOR, valor_gale2_path).send_keys(u'\ue009' + u'\ue003')
        driver.find_element(By.CSS_SELECTOR, valor_gale2_path).send_keys(entrada_gale4)
        driver.find_element(By.CSS_SELECTOR, apostar_path_1).click()
        print('Entrada no GALE 4')
        green_gale_4 = True
        gale_4 = False
        
    elif resultado[0] >= auto_retirar and green_gale_4 == True:
        valor_entrada_path = ".first-row:nth-child(2) .font-weight-bold"
        driver.find_element(By.CSS_SELECTOR, valor_entrada_path).send_keys(u'\ue009' + u'\ue003')
        driver.find_element(By.CSS_SELECTOR, valor_entrada_path).send_keys(valor_entrada)
        entrada = True
        green = True
        green_gale_4 = False
        gale_3 = False
        gale_4 = False
        gale_5 = False
        
    elif resultado[0] < auto_retirar and gale_5 == True:
        valor_gale2_path = ".first-row:nth-child(2) .font-weight-bold"
        driver.find_element(By.CSS_SELECTOR, valor_gale2_path).send_keys(u'\ue009' + u'\ue003')
        driver.find_element(By.CSS_SELECTOR, valor_gale2_path).send_keys(entrada_gale5)
        driver.find_element(By.CSS_SELECTOR, apostar_path_1).click()
        print('Entrada no GALE 5')
        green_gale_5 = True
        gale_5 = False
        gale_4 = True
        
    elif resultado[0] >= auto_retirar and green_gale_5 == True:
        valor_entrada_path = ".first-row:nth-child(2) .font-weight-bold"
        driver.find_element(By.CSS_SELECTOR, valor_entrada_path).send_keys(u'\ue009' + u'\ue003')
        driver.find_element(By.CSS_SELECTOR, valor_entrada_path).send_keys(valor_entrada)
        entrada = True
        green = True
        green_gale_5 = False
        gale_3 = False
        gale_4 = False
        gale_5 = False
        
        
        
    elif resultado[0] < auto_retirar and gale_5 == True:
        valor_gale2_path = ".first-row:nth-child(2) .font-weight-bold"
        driver.find_element(By.CSS_SELECTOR, valor_gale2_path).send_keys(u'\ue009' + u'\ue003')
        driver.find_element(By.CSS_SELECTOR, valor_gale2_path).send_keys(entrada_gale5)
        driver.find_element(By.CSS_SELECTOR, apostar_path_1).click()
        print('Entrada no GALE 5')
        green_gale_5 = True
        gale_5 = False
        gale_4 = True
        
    elif resultado[0] >= auto_retirar and green_gale_5 == True:
        valor_entrada_path = ".first-row:nth-child(2) .font-weight-bold"
        driver.find_element(By.CSS_SELECTOR, valor_entrada_path).send_keys(u'\ue009' + u'\ue003')
        driver.find_element(By.CSS_SELECTOR, valor_entrada_path).send_keys(valor_entrada)
        entrada = True
        green = True
        green_gale_5 = False
        gale_3 = False
        gale_4 = False
        gale_5 = False
     
while True:
    resultado()
    if resultado_final != check_resultado_final:
        check_resultado_final = resultado_final
        estrategia(resultado_final)
        data = (dt.now().strftime('%m/%d/%Y %H.%M.%S'))
        print(resultado_final,data)