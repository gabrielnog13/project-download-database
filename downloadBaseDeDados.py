import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import zipfile
import shutil

download_dir = os.path.expanduser("~/Downloads")

final_dir = os.path.expanduser("~/Desktop/downloadDeBases")

zip_file_name = "siconv.zip"

os.makedirs(final_dir, exist_ok=True)

options = webdriver.ChromeOptions()
prefs = {"download.default_directory": download_dir}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://repositorio.dados.gov.br/seges/detru/")
time.sleep(5)

download_link = driver.find_element(By.XPATH, '/html/body/pre/a[7]')
download_link.click()
time.sleep(1000)

driver.quit()


zip_path = os.path.join(download_dir, zip_file_name)

if os.path.exists(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(download_dir)
    for file_name in os.listdir(download_dir):
        file_path = os.path.join(download_dir, file_name)
        if os.path.isfile(file_path):
            shutil.move(zip_file_name, final_dir)
else:
    print("Arquivo .zip não encontrado!")

os.remove(zip_path)