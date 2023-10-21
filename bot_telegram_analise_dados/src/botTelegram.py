from dotenv import dotenv_values # biblioteca para chamar variaveis do ambiente .env
import os # para acessar o valor dentro da variavel do amebinte .env
import requests

load_dotenv() # carregando variaveis de ambiente.

class bottelegram:
    def __init__(self): # Ser executada toda vez que eu instanciar um objeto do tipo bottelegram.
        TOKEN = os.getenv("API_KEY") # pegando a variavel do ambiente env
        self.url = f"https://api.telegram.org/bot{TOKEN}/" # variavel de objeto. A / é para evitar problemas na codificação, pra nao misturar com outras variaveis.

    def start(self):
        while True:
            print(self.get_message())
            
    def get_message(self): # o self é para conseguir acessar a URL dentro da classe.
        link_request = f"{self.url}getUpdates?timeout=1000"
        result = requests.get(link_request)
        return result