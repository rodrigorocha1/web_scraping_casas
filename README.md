# Web Scraping do Site Viva Real

## 1 – Introdução

Este projeto tem como objetivo construir um web scraping usando Scrapy para extrair informações do site [Viva Real](https://www.vivareal.com.br/) e salvá-las em um arquivo `.xlsx`. A aplicação coleta os seguintes dados:

- **URL**: Link do anúncio.
- **Nome do apartamento**: Título do anúncio.
- **Preços**: Valor do imóvel.
- **Endereço**: Localização do imóvel.
- **Metragem**: Área do imóvel em metros quadrados.
- **Quartos**: Número de quartos disponíveis.
- **Banheiros**: Número de banheiros disponíveis.
- **Garagens**: Vagas de garagem.
- **Tipo de Imóvel**: Ex.: Apartamento, Casa, etc.
- **Data e Hora da Coleta**: Data e hora de quando os dados foram coletados.

Essas informações são salvas em um arquivo `.xlsx`, com as colunas organizadas conforme descrito acima.

## 2 – Diagrama de Classe

O diagrama de classe do projeto, ilustrado abaixo, organiza as classes e destaca a flexibilidade do sistema. 

> **Nota**: O diagrama facilita a reutilização de código e permite que o método de armazenamento dos dados possa ser alterado facilmente, por exemplo, de um arquivo Excel para um banco de dados, sem necessidade de alterações na classe principal.


![Diagrama de classe](https://static.wixstatic.com/media/123393_2defcd68894c40588a50dcaadc512c5a~mv2.png/v1/fill/w_740,h_557,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/123393_2defcd68894c40588a50dcaadc512c5a~mv2.png)


## 6 – Demonstração
[Link para a Demonstração](https://youtu.be/mcVH0QNHtVY)
