import os
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from tkinter import Tk, Label, Text, Button
from threading import Thread

# Dados de login
usuario = "seu_user"
senha = "seu_password"

# Mensagens padrão
mensagens_padrao = [
    "Oi, tudo bem?",
    "Olá, como vai?",
    "E aí, tudo tranquilo?",
    "Oi, espero que esteja bem!",
    "Olá, tenha um ótimo dia!",
    "Oi, você tem algum plano para hoje?"
]

# Função para iniciar a automação
def iniciar_automacao():
    # Obtém os links dos perfis da entrada de texto
    perfis = entrada_perfis.get("1.0", "end-1c").splitlines()

    # Define o diretório para armazenar os dados do Chrome
    chrome_data_dir = os.path.join(os.getenv('APPDATA'), 'instamilio')

    # Configuração do ChromeDriver com opções
    options = Options()
    options.add_argument(f"--user-data-dir={chrome_data_dir}")
    driver = webdriver.Chrome("chromedriver.exe", options=options)

    # Abre o Instagram e realiza o login automaticamente
    driver.get("https://www.instagram.com/")
    sleep(2)
    driver.find_element_by_name("username").send_keys(usuario)
    driver.find_element_by_name("password").send_keys(senha)
    driver.find_element_by_xpath("//button[contains(., 'Entrar')]").click()
    sleep(5)

    # Percorre os perfis e envia as mensagens
    for perfil_link in perfis:
        # Escolhe uma variação de mensagem aleatória
        mensagem_variada = random.choice(mensagens_padrao)

        # Abre o perfil
        driver.get(perfil_link)
        sleep(3)

        # Clica no botão de mensagem
        message_button = driver.find_element_by_css_selector("button[type='button'][aria-label='Enviar mensagem']")
        message_button.click()
        sleep(2)

        # Digita a mensagem e envia
        message_input = driver.find_element_by_css_selector("textarea[placeholder='Mensagem...']")
        message_input.send_keys(mensagem_variada)
        message_input.send_keys(Keys.ENTER)
        sleep(2)

        print("Mensagem enviada para o perfil:", perfil_link)
        print("Mensagem utilizada:", mensagem_variada)

        # Espera 4 minutos antes de enviar a próxima mensagem
        sleep(240)

    
# Função para iniciar a automação em uma thread separada
def iniciar_automacao_thread():
    thread = Thread(target=iniciar_automacao)
    thread.start()

# Cria a janela principal
janela = Tk()
janela.title("Automação de Prospecção")
janela.geometry("400x300")

# Rótulo para a entrada de texto dos perfis
label_perfis = Label(janela, text="Cole os links dos perfis abaixo:")
label_perfis.pack()

# Entrada de texto para os perfis
entrada_perfis = Text(janela, height=10, width=40)
entrada_perfis.pack()

# Botão para iniciar a automação
botao_iniciar = Button(janela, text="Iniciar Automação", command=iniciar_automacao_thread)
botao_iniciar.pack()

# Inicia a execução da interface gráfica
janela.mainloop()
