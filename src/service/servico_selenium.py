from typing import Iterator, Tuple
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchElementException,
    InvalidElementStateException,
    ElementNotInteractableException
)
from src.config.pacote_log import logger


class WebScrapingSelenium:

    def __init__(self, url: str):
        self.__url = url
        self.__servico = Service(ChromeDriverManager().install())

    def __clicar_cookie(self, navegador: WebDriver):
        """Método para clicar no cookie

        Args:
            navegador (WebDriver): Recebe o navegador
        """
        try:
            WebDriverWait(navegador, 10).until(EC.element_to_be_clickable(
                (By.ID, 'adopt-accept-all-button'))).click()
        except:
            pass

    def abrir_navegador(self) -> WebDriver:
        navegador = webdriver.Chrome(service=self.__servico)
        navegador.get(self.__url)
        navegador.maximize_window()
        self.__clicar_cookie(navegador=navegador)
        return navegador

    def extrair_dados(self, navegador: WebDriver) -> Iterator[Tuple[WebElement]]:
        """Método para extrair dados

        Args:
            navegador (WebDriver): Navegador

        Returns:
            _type_: Um iteravel

        Yields:
            Iterator[Tuple]: Um iteravel
        """
        try:

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
        except NoSuchElementException as msg:
            logger.error(f'Não encontrou elemento: {msg} ')
            exit(1)
        except ElementNotInteractableException:
            logger.error('Elemento não pode ser interagido')
            exit(1)
        except InvalidElementStateException:
            logger.error('Falha na operação de enviar teclas')
            exit(1)
        except Exception:
            logger.error('Falha Geral')
            exit(1)

    def executar_paginacao(self, navegador: WebDriver) -> bool:
        """Executar a páginação

        Args:
            navegador (WebDriver): navegdor

        Returns:
            bool: verdadeiro se o botão existe, falso caso contrário
        """
        try:
            navegador.find_element(
                By.XPATH,  '//*[@id="js-site-main"]/div[2]/div[1]/section/div[2]/div[2]/div/ul/li[9]/button').click()
            return True

        except Exception as e:
            return False

    def fechar_navegador(self, navegador: WebDriver):
        """Método para fechar o navegador

        Args:
            navegador (WebDriver): recebe o navegador
        """
        navegador.quit()
