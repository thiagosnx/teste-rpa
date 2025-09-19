# IMDb Scraper com Selenium

Este projeto é um script em Python que usa **Selenium WebDriver** para acessar a lista dos filmes mais bem avaliados no IMDb, coletar informações (título, ano, duração, nota, classificação e sinopse) e salvar os resultados em um arquivo CSV. Ao final, o arquivo é movido automaticamente para a pasta `uploads`.

## Requisitos

* Python 3.8 ou superior
* Google Chrome instalado
* ChromeDriver compatível com a versão do seu navegador (colocado no PATH ou na mesma pasta do script)
* pip

## Estrutura básica

* `script.py` — arquivo com o script
* `requirements.txt` — arquivo com dependências
* `uploads/` — pasta onde o CSV final será movido

## Instalação (passo a passo)

1. (Opcional) criar e ativar um ambiente virtual:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

2. Instalar dependências:

```bash
pip install -r requirements.txt
```

## Como executar

No terminal, dentro da pasta do projeto, execute:

```bash
python script.py
```


## Saída

* O script gera o arquivo `filmes_imdb.csv` com os dados coletados.
* Em seguida o arquivo é movido para a pasta `uploads` (criada automaticamente, se não existir).

## Observações importantes

* Certifique-se de que o **ChromeDriver** esteja compatível com a versão do Google Chrome. Se não quiser adicionar ao PATH, coloque o executável `chromedriver` na mesma pasta do script.
* O script está configurado para coletar os **5 primeiros filmes** (linha `for f in filmes[:5]:`). Altere `5` para coletar mais ou menos filmes.
* Dependências usadas no script: `selenium`, `pandas`. O restante (`pathlib`, `time`, `shutil`) faz parte da biblioteca padrão do Python.

## Problemas comuns

* Erro de `ChromeDriver` não encontrado: verifique se o executável está no PATH ou na mesma pasta.
* Diferenças na estrutura do site (classes/IDs): o IMDb pode alterar classes, o que pode quebrar seletores por classe. Nesse caso, atualize os seletores no script.

