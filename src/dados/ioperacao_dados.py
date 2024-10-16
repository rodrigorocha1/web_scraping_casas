from abc import ABC, abstractmethod
from typing import Tuple


class IoperacaoDados(ABC):
    @abstractmethod
    def salvar_dados(self, dados: Tuple):
        pass

    @abstractmethod
    def atualizar_dados(self, dados: Tuple):
        pass
