from abc import ABC, abstractmethod
from typing import Tuple


class IoperacaoDados(ABC):
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
