from src.dados.ioperacao_dados import IoperacaoDados
from src.dados.arquivo import Arquivo
from src.dados.arquivo_excel import ArquivoExcel
from src.service.servico_selenium import WebScrapingSelenium
from time import sleep


class WebScrapingPipeline:
    def __init__(self, operacao_dados: IoperacaoDados | Arquivo,  url: str, tipo_imovel: str):
        self.__tipo_imovel = tipo_imovel
        self.__url = url
        self.__operacao_dados = operacao_dados
        self.__servico_web_scraping = WebScrapingSelenium(url=self.__url)

    def rodar_web_scraping(self):
        navegador = self.__servico_web_scraping.abrir_navegador()
        flag_loop = True
        while flag_loop:

            sleep(4)
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
                    'tipo_imovel': self.__tipo_imovel
                }]
                if not self.__operacao_dados.verificar_arquivo():
                    self.__operacao_dados.salvar_dados(dados=dado)
                else:
                    self.__operacao_dados.atualizar_dados(dados=dado)

            flag_loop = self.__servico_web_scraping.executar_paginacao(
                navegador=navegador)
        self.__servico_web_scraping.fechar_navegador(navegador=navegador)


if __name__ == '__main__':
    tipo_imovel = 'apartamento'
    url = 'https://www.vivareal.com.br/venda/sp/ribeirao-preto/apartamento_residencial/#onde=,S%C3%A3o%20Paulo,Ribeir%C3%A3o%20Preto,,,,,city,BR%3ESao%20Paulo%3ENULL%3ERibeirao%20Preto,-21.169402,-47.811086,&itl_id=1000183&itl_name=vivareal_-_botao-cta_buscar_to_vivareal_resultado-pesquisa'
    wsp = WebScrapingPipeline(
        operacao_dados=ArquivoExcel(nome_aba=tipo_imovel, nome_arquivo='dados_imoveis.xlsx', nome_pasta_amarzenamento='pasta_excel'), tipo_imovel=tipo_imovel, url=url)
    wsp.rodar_web_scraping()
