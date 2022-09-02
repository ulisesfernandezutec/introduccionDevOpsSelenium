from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from time import sleep, time

def Error():
    print('Prueba NO superada')

if __name__ == '__main__':
    
    username = 'root'
    password = 'password'

    driver = webdriver.Chrome("./chromedriver")
    driver.get("http://127.0.0.1:8111/")

    driver.find_element(By.NAME,"user").send_keys(username)
    driver.find_element(By.NAME, "pass").send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="login"]/div[3]/div/input').click()

    driver.implicitly_wait(10)
    driver.get("http://127.0.0.1:8111/")
    
    driver.find_element(By.XPATH, '//*[@id="TitleBox--_index_html------Q3JlYWNpw7NuIHLDoXBpZGEgZGUgdGlja2V0---0"]/div/form/div[1]/div[1]/div[2]/input').send_keys('Prueba Ulises')
    driver.find_element(By.XPATH, '//*[@id="TitleBox--_index_html------Q3JlYWNpw7NuIHLDoXBpZGEgZGUgdGlja2V0---0"]/div/form/div[1]/div[5]/div[2]/textarea').send_keys('Texto de Prueba Ulises')
    driver.find_element(By.XPATH, '//*[@id="TitleBox--_index_html------Q3JlYWNpw7NuIHLDoXBpZGEgZGUgdGlja2V0---0"]/div/form/div[2]/div/div/div[2]/input').click()

    wait = WebDriverWait(driver, 10)
    h1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="body"]/h1')))

    if h1.text == 'Posible falsificación de petición en sitios cruzados (CSRF)':
        print('Prueba superada')
    else: 
        Error()
   
    driver.close()


