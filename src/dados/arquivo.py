from src.dados.ioperacao_dados import IoperacaoDados
from typing import Tuple
from abc import abstractmethod
import os


class Arquivo(IoperacaoDados):
    def __init__(self):
        self._caminho_base = os.getcwd()

    @abstractmethod
    def salvar_dados(self, dados: Tuple):
        """Método para salvar dados na planilha

        Args:
            dados (Tuple): dados a serem salvos
        """
        pass

    @abstractmethod
    def atualizar_dados(self, dados: Tuple):
        """Método para atualizar dados na planilha

        Args:
            dados (Tuple): dados a serem salvos
        """
        pass
