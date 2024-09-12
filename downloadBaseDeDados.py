import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import zipfile
import shutil

# configurações
# diretório para onde o arquivo .zip será baixado
download_dir = os.path.expanduser("~/Downloads")

# diretório para onde os arquivos descompactados serão movidos
final_dir = os.path.expanduser("~/Desktop/downloadDeBases")

# nome do arquivo .zip a ser baixado
zip_file_name = "siconv.zip"

# criar o diretório final se ele não existir
os.makedirs(final_dir, exist_ok=True)

# configurar o Selenium para usar o Chrome
options = webdriver.ChromeOptions()
prefs = {"download.default_directory": download_dir}
options.add_experimental_option("prefs", prefs)

# inicializar o WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) # inicialização do navegador google chrome

# navegar para a página com o link do arquivo .zip
driver.get("https://repositorio.dados.gov.br/seges/detru/") # o link do site onde tem o arquivo que deseja baixar

# tempo necessário para espe (pode ser necessário ajustar o tempo ou usar WebDriverWait)
time.sleep(5)

# encontrar e clicar no link de download (ajuste o seletor conforme necessário)
download_link = driver.find_element(By.XPATH, '/html/body/pre/a[7]') # aqui é passado o xpath do aquivo que será baixado
download_link.click()

# tempo de espera de conclusão do download (pode ser necessário ajustar o tempo ou implementar uma verificação de arquivo)
time.sleep(1000)

# fechar o navegador
driver.quit()

# caminho do arquivo .zip que foi baixado
zip_path = os.path.join(download_dir, zip_file_name)

# verificação se o arquivo .zip foi baixado e se foi no diretório certo
if os.path.exists(zip_path):
    # descompactar o arquivo .zip
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(download_dir)

    # mover os arquivos que foram descompactados para o diretório final
    for file_name in os.listdir(download_dir):
        file_path = os.path.join(download_dir, file_name)
        if os.path.isfile(file_path):
            shutil.move(zip_file_name, final_dir)
else:
    print("Arquivo .zip não encontrado!")

# limpar o diretório de download
    os.remove(zip_path)