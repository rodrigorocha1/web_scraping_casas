from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get('https://www.vivareal.com.br/venda/sp/ribeirao-preto/apartamento_residencial/#onde=Brasil,S%C3%A3o%20Paulo,Ribeir%C3%A3o%20Preto,,,,,,BR%3ESao%20Paulo%3ENULL%3ERibeirao%20Preto,,,')
navegador.maximize_window()


nome_apartamentos = navegador.find_elements(
    By.CLASS_NAME, 'property-card__title')


nome_apartamentos = navegador.find_elements(
    By.CLASS_NAME, 'property-card__title')

precos = navegador.find_elements(
    By.CLASS_NAME, 'js-property-card__price-small')

enderecos_apartamentos = navegador.find_elements(
    By.CLASS_NAME, 'property-card__address')

metragems = navegador.find_elements(
    By.CLASS_NAME, 'js-property-card-detail-area')

quartos = navegador.find_elements(
    By.CLASS_NAME, 'js-property-detail-rooms')

banheiros = navegador.find_elements(
    By.CLASS_NAME, 'js-property-detail-bathroom')

garagens = navegador.find_elements(
    By.CLASS_NAME, 'js-property-detail-garages')

navegador.find_element(
    By.XPATH,  '//*[@id="js-site-main"]/div[2]/div[1]/section/div[2]/div[2]/div/ul/li[9]/button').click()
