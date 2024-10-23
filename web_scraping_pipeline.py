from src.dados.ioperacao_dados import IoperacaoDados
from src.dados.arquivo import Arquivo
from src.dados.arquivo_excel import ArquivoExcel
from src.service.servico_selenium import WebScrapingSelenium
import os
from time import sleep
from datetime import datetime
from src.config.pacote_log import logger


class WebScrapingPipeline:
    def __init__(self, operacao_dados: IoperacaoDados | Arquivo,  url: str, tipo_imovel: str):
        self.__tipo_imovel = tipo_imovel
        self.__url = url
        self.__operacao_dados = operacao_dados
        self.__servico_web_scraping = WebScrapingSelenium(url=self.__url)

    def rodar_web_scraping(self):
        logger.info('Abrindo navegador')
        navegador = self.__servico_web_scraping.abrir_navegador()

        flag_loop = True
        i = 224
        while flag_loop:

            sleep(4)
            logger.info('Obter dados e Salvando dados')
            for dados in self.__servico_web_scraping.extrair_dados(navegador=navegador):
                dado = [{
                    'url': dados[0].get_attribute('href'),
                    'nome_apartamentos': dados[1].text,
                    'precos': dados[2].text,
                    'enderecos_apartamentos': dados[3].text,
                    'metragems': dados[4].text,
                    'quartos': dados[5].text,
                    'banheiros': dados[6].text,
                    'garagens': dados[7].text,
                    'tipo_imovel': self.__tipo_imovel,
                    'pagina': i,
                    'data_hora_coleta': datetime.now().strftime("%d-%m-%Y %H:%M:%S")

                }]

                if not self.__operacao_dados.verificar_arquivo():
                    self.__operacao_dados.salvar_dados(dados=dado)
                else:
                    self.__operacao_dados.atualizar_dados(dados=dado)

            flag_loop = self.__servico_web_scraping.executar_paginacao(
                navegador=navegador)
            i += 1
        self.__servico_web_scraping.fechar_navegador(navegador=navegador)
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':

    tipos_dados = [
        # ('apartamento', 'https://www.vivareal.com.br/venda/sp/ribeirao-preto/apartamento_residencial/?pagina=273#onde=Brasil,S%C3%A3o%20Paulo,Ribeir%C3%A3o%20Preto,,,,,,BR%3ESao%20Paulo%3ENULL%3ERibeirao%20Preto,,,'),
        ('casa', 'https://www.vivareal.com.br/venda/sp/ribeirao-preto/casa_residencial/?pagina=224#onde=Brasil,S%C3%A3o%20Paulo,Ribeir%C3%A3o%20Preto,,,,,,BR%3ESao%20Paulo%3ENULL%3ERibeirao%20Preto,,,')
    ]

    for dados in tipos_dados:

        tipo_imovel = dados[0]
        url = dados[1]
        logger.info(f'Obtendo dados {tipo_imovel}')
        wsp = WebScrapingPipeline(
            operacao_dados=ArquivoExcel(nome_aba=tipo_imovel, nome_arquivo=f'dados_imoveis.xlsx', nome_pasta_amarzenamento='pasta_excel'), tipo_imovel=tipo_imovel, url=url)
        wsp.rodar_web_scraping()
