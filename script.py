from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time


driver = webdriver.Chrome()


driver.get("http://www.google.com.br/")
time.sleep(2)

driver.get("https://www.imdb.com/pt/chart/top/")

filmes = driver.find_elements(By.CLASS_NAME, "ipc-metadata-list-summary-item")

for f in filmes:
    print(f.text)

driver.quit()
