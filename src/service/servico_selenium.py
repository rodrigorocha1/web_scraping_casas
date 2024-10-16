from typing import Iterator, Tuple
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import logging


logging.getLogger("example")
logging.basicConfig(format="%(levelname)s | %(asctime)s | %(message)s",
                    level=logging.INFO, filename='test.log', datefmt="%Y-%m-%dT%H:%M:%SZ",)


class WebScrapingSelenium:

    def __init__(self, url: str, tipo_imovel: str):
        self.__url = url
        self.__servico = Service(ChromeDriverManager().install())

    def __clicar_cookie(self, navegador: WebDriver):
        WebDriverWait(navegador, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="cookie-notifier-cta"]'))).click()

    def abrir_navegador(self) -> WebDriver:
        navegador = webdriver.Chrome(service=self.__servico)
        navegador.get(self.__url)
        navegador.maximize_window()
        self.__clicar_cookie(navegador=navegador)
        return navegador

    def extrair_dados(self, navegador: WebDriver) -> Iterator[Tuple]:

        urls = navegador.find_elements(
            By.CLASS_NAME, 'property-card__content-link')

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

        return zip(urls, nome_apartamentos, precos, enderecos_apartamentos, metragems, quartos, banheiros, garagens)

    def executar_paginacao(self, navegador: WebDriver) -> bool:
        try:
            navegador.find_element(
                By.XPATH,  '//*[@id="js-site-main"]/div[2]/div[1]/section/div[2]/div[2]/div/ul/li[9]/button').click()
            return True
        except ElementClickInterceptedException:
            return False
        except Exception as e:
            logging.critical(f"A critical message {e}")

    def fechar_navegador(self, navegador: WebDriver):
        navegador.quit()
