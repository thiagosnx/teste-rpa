from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time


driver = webdriver.Chrome()


driver.get("http://www.google.com.br/")
time.sleep(1)

driver.get("https://www.imdb.com/pt/chart/top/")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

botao_inicio = driver.find_element(By.CLASS_NAME, "ipc-scroll-to-top-button.sc-3e53ab1c-0.dOykdw.visible.ipc-chip.ipc-chip--on-base")
time.sleep(3)

botao_inicio.click()

filmes = driver.find_elements(By.CLASS_NAME, "ipc-metadata-list-summary-item")

resultados = []


for f in filmes:
    titulo = f.find_element(By.CLASS_NAME, "ipc-title__text.ipc-title__text--reduced").text

    spans = f.find_elements(By.CLASS_NAME, "sc-15ac7568-7.cCsint.cli-title-metadata-item")

    ano = spans[0].text
    duracao = spans[1].text
    classificacao = spans[2].text if len(spans) > 2 else 'N/I'


    resultados.append({
        "titulo": titulo,
        "ano": ano,
        "duracao":duracao,
        "classificacao":classificacao
    })


for r in resultados:
    print(r)

driver.quit()