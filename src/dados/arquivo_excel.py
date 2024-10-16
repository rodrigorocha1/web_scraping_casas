from typing import Dict, Union
from src.dados.arquivo import Arquivo
from openpyxl import Workbook, load_workbook, worksheet


class ArquivoExcel(Arquivo):
    def __init__(self, nome_aba: str):
        self.__planilha = Workbook()
        self.__nome_aba = nome_aba
        super().__init__()

    def __criar_cabecalho(self, dados: Dict[str, Union[str, int]], aba: worksheet):
        cabecalhos = list(dados.keys())
        aba.append(cabecalhos)

        return cabecalhos

    def salvar_dados(self, dados: Dict[str, Union[str, int]]):
        aba = self.__planilha.active
        aba.title = self.__nome_aba

        cabecalhos = self.__criar_cabecalho(dados=dados, aba=aba)
        for linha in dados:

            valores = [linha[coluna] for coluna in cabecalhos]
            aba.append(valores)
        self.__planilha.save(self._caminho_arquivo)
        self.__planilha.close()

    def atualizar_dados(self, dados: Dict[str, Union[str, int]]):
        workbook = load_workbook(self._caminho_arquivo)
        if self.__nome_aba not in workbook.sheetnames:
            planilha = workbook.create_sheet(self.__nome_aba)
            cabecalhos = self.__criar_cabecalho(dados=dados, aba=planilha)
            for linha in dados:
                valores = [linha[coluna] for coluna in cabecalhos]
                planilha.append(valores)
        else:
            planilha = workbook[self.__nome_aba]
            ultima_lina = planilha.max_row + 1
            for _, valor in enumerate(dados, start=ultima_lina):
                planilha.append(list(valor.values()))

            ultima_lina = planilha.max_row

        workbook.save(self._caminho_arquivo)
        workbook.close()

    def verificar_arquivo(self):
        return os.path.exists(self._caminho_arquivo)
