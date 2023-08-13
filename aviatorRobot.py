from time import sleep
import pandas as pd
from selenium import webdriver
from datetime import datetime as dt
from selenium.webdriver.chrome import service
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from configobj import ConfigObj


config  = ConfigObj('config.txt')
usuario = config['LOGIN']['usuario']
senha   = config['LOGIN']['senha']

'''
valor_entrada = config['PARAMETERS']['valor_entrada']
auto_retirar  = config['PARAMETERS']['auto_retirar']
usar_mg = config['MARTINGALE']['usar_martingale']
fator_mg = config['MARTINGALE']['fator_martingale']
niveis_mg = config['MARTINGALE']['niveis_martingale']
entrada_gale1 = int(valor_entrada) * float(fator_mg)
entrada_gale2 = float(entrada_gale1) * float(fator_mg)
entrada_gale3 = float(entrada_gale2) * float(fator_mg)
entrada_gale4 = float(entrada_gale3) * float(fator_mg)
'''


resultado_final = []
check_resultado_final = []

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.premierbet.co.mz/play-game/?gameId=193484')
sleep(5)

#login
user_path = "//body/div/div/main[@role='main']/div/div/div/div/div/article/div/div/div/form[@action='#']/div/input[1]"
driver.find_element(By.XPATH, user_path).send_keys(usuario)

password_path = "//main[@role='main']//div//div//div//div//div//article//div//div//div//form[@action='#']//div//div//input[@placeholder='Palavra-passe']"
driver.find_element(By.XPATH, password_path).send_keys(senha)

login_btn_path = "//main[@role='main']//button[@type='button'][normalize-space()='Iniciar sessão']"
driver.find_element(By.XPATH, login_btn_path).click()

#aviator game
while len(driver.find_elements(By.XPATH, "//iframe[@id='game_loader']")) == 0:
    sleep(0.1)
        
iframe_1_path = "//iframe[@id='game_loader']"
iframe_1 = driver.find_element(By.XPATH, iframe_1_path)
sleep(0.1)
driver.switch_to.frame(iframe_1)

iframe_2_path = "//iframe[@id='game-iframe']"
iframe_2 = driver.find_element(By.XPATH, iframe_2_path)
sleep(0.1)
driver.switch_to.frame(iframe_2)

while len(driver.find_elements(By.XPATH, "//iframe[@id='spribe-game']")) == 0:
    sleep(0.1)

iframe_3_path = "//iframe[@id='spribe-game']"
iframe_3 = driver.find_element(By.XPATH, iframe_3_path)
sleep(0.1)
driver.switch_to.frame(iframe_3)

print("Pegando ultimos resultados...")
while len(driver.find_elements(By.XPATH, "/html/body/app-root/app-game/div/div[1]/div[2]/div/div[1]/app-bets-widget/div/app-all-bets-tab/div/cdk-virtual-scroll-viewport")) == 0:
    sleep(0.1)

minutos = float(dt.now().strftime('%M.%S')[1:])

def resultado():
    global resultado_final
    
    resultado = driver.find_element(By.XPATH, "/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[1]/app-stats-widget/div/div[1]").text
    lista = []
    resultado_final = []
    
    lista = resultado.split()
    
    for x in range(len(lista[0:1])):
        numero = lista[x].translate(str.maketrans('','','x'))
        resultado_final.append(float(numero))
        
    return resultado_final  

while True:
    resultado()
    if resultado_final != check_resultado_final:
        check_resultado_final = resultado_final
        data = (dt.now().strftime('%m/%d/%Y %H.%M.%S'))
        print(resultado_final, data) 