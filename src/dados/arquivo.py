from src.dados.ioperacao_dados import IoperacaoDados
import os
import openpyxl


class Arquivo(IoperacaoDados):
    def __init__(self):
        self._caminho_base = os.getcwd()
