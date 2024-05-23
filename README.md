# Projeto de Web Scraper em Python

## Descrição

Este projeto é um web scraper desenvolvido em Python para extrair informações de títulos e preços de livros de um site fictício de vendas de livros: http://books.toscrape.com/. O scraper navega por várias páginas do site, coleta os dados e os armazena em um arquivo CSV e em um banco de dados SQLite.

## Funcionalidades

> Extração de títulos e preços de livros.
> Navegação automática por múltiplas páginas.
> Armazenamento dos dados extraídos em um arquivo CSV.
> Armazenamento opcional em um banco de dados SQLite.

## Requisitos

* Python 3.x
* 'requests'
* 'beautifulsoup4'
* 'pandas'
* 'sqlite3' (padrão no Python)

# Instalação

1. Clone o repositório:

>* **git clone** https://github.com/4ndr4d3/web-scraper-python.git 
>* **cd** web-scraper-python

2. Crie um ambiente virtual (opcional, mas recomendado):

  >python -m venv venv

  >**source** venv/bin/activate  
   
  

3. Instale as dependências:

>**pip install -r requirements.txt**

# Uso

1. Execute o script principal para iniciar o scraping:

>python webscraper.py

2. Após a execução, os dados extraídos estarão disponíveis em **books.csv** e **books.db**.

# Estrutura do Projeto

nome-do-repositorio/
│
├── webscraper.py        
├── requirements.txt      
├── README.md            
├── books.csv             
└── books.db              


# Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias.

# Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo **LICENSE** para mais detalhes.