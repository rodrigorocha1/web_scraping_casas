from src.dados.ioperacao_dados import IoperacaoDados
from typing import Tuple
import os


class Arquivo(IoperacaoDados):
    def __init__(self):
        self._caminho_base = os.getcwd()

    def salvar_dados(self, dados: Tuple):
        pass

    def atualizar_dados(self, dados: Tuple):
        pass
