from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pathlib import Path
import time
import pandas as pd
import shutil

def get_filmes():

    driver = webdriver.Chrome()

    driver.get("http://www.google.com.br/")
    time.sleep(1)

    driver.get("https://www.imdb.com/pt/chart/top/")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    inico_btn = WebDriverWait(driver, 5).until(
                ec.visibility_of_element_located((By.CLASS_NAME, "ipc-scroll-to-top-button.sc-3e53ab1c-0.dOykdw.visible.ipc-chip.ipc-chip--on-base"))
            )


    inico_btn.click()


    filmes = driver.find_elements(By.CLASS_NAME, "ipc-metadata-list-summary-item")


    resultados = []

    actions = ActionChains(driver)


    for f in filmes:

        sinopse_btn = f.find_element(By.CLASS_NAME, "ipc-icon-button.li-info-icon.ipc-icon-button--base.ipc-icon-button--onAccent2")

        actions.move_to_element(sinopse_btn).perform()

        WebDriverWait(driver, 10).until(ec.element_to_be_clickable(sinopse_btn))

        sinopse_btn.click()

        sinopse = WebDriverWait(driver, 5).until(
                ec.visibility_of_element_located((By.CLASS_NAME, "sc-717a9add-2.jPYKsd"))
            )
        sinopse = sinopse.text

        fecha_sinopse_btn = driver.find_element(By.CLASS_NAME, "ipc-promptable-base__close") 
        fecha_sinopse_btn.click()

        time.sleep(0.5)
        
        WebDriverWait(driver, 20).until(
            ec.invisibility_of_element_located((By.CLASS_NAME, "sc-717a9add-2.jPYKsd"))
        )


        titulo = f.find_element(By.CLASS_NAME, "ipc-title__text.ipc-title__text--reduced").text

        nota = f.find_element(By.CLASS_NAME, "ipc-rating-star--rating").text

        spans = f.find_elements(By.CLASS_NAME, "sc-15ac7568-7.cCsint.cli-title-metadata-item")

        ano = spans[0].text
        duracao = spans[1].text
        classificacao = spans[2].text if len(spans) > 2 else 'N/I'


        resultados.append({
            "titulo": titulo,
            "ano": ano,
            "duracao": duracao,
            "nota": nota,
            "classificacao": classificacao,
            "sinopse": sinopse
        })

    df = pd.DataFrame(resultados)

    df.columns = df.columns.str.upper()

    file = "filmes_imdb.csv"

    df.to_csv(file, index=False, encoding='utf-8-sig', sep=';')

    driver.quit()

    move_file(file, "uploads")

def move_file(file, path):
    origem = Path(file)
    destino = Path(path)

    destino.mkdir(parents=True, exist_ok=True)

    destino = destino / origem.name

    shutil.move(origem, destino)

    return destino


get_filmes()