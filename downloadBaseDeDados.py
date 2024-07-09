import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import zipfile
import shutil

# Configurações
download_dir = "/path/to/downloads"  # Diretório para onde o arquivo .zip será baixado
final_dir = "/path/to/desktop/downloadDeBases"  # Diretório para onde os arquivos descompactados serão movidos
zip_file_name = "siconv.zip"  # Nome do arquivo .zip a ser baixado

# Configurar o Selenium para usar o Chrome
options = webdriver.ChromeOptions()
prefs = {"download.default_directory": download_dir}
options.add_experimental_option("prefs", prefs)

# Inicializar o WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) #inicializa o navegador google chrome

# Navegar para a página com o link do arquivo .zip
driver.get("https://repositorio.dados.gov.br/seges/detru/") #aqui é passado o link do site onde tem o arquivo que você quer baixar

# Esperar a página carregar completamente (pode ser necessário ajustar o tempo ou usar WebDriverWait)
time.sleep(5)

# Encontrar e clicar no link de download (ajuste o seletor conforme necessário)
download_link = driver.find_element(By.XPATH, '/html/body/pre/a[7]') #aqui é passado o xpath do aquivo que será baixado
download_link.click()

# Esperar o download completar (pode ser necessário ajustar o tempo ou implementar uma verificação de arquivo)
time.sleep(1000)

# Fechar o navegador
driver.quit()

# Caminho completo do arquivo .zip baixado
zip_path = os.path.join(download_dir, zip_file_name)

# Verificar se o arquivo .zip foi baixado
if os.path.exists(zip_path):
    # Descompactar o arquivo .zip
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(download_dir)

    # Mover os arquivos descompactados para o diretório final
    for file_name in os.listdir(download_dir):
        file_path = os.path.join(download_dir, file_name)
        if os.path.isfile(file_path):
            shutil.move(file_path, final_dir)
else:
    print("Arquivo .zip não encontrado!")

# Limpar o diretório de download (opcional mas é recomendável que seja feito)
os.remove(zip_path)