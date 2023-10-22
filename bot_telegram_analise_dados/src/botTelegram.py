from dotenv import load_dotenv # biblioteca para chamar variaveis do ambiente .env
import os # para acessar o valor dentro da variavel do amebinte .env
import requests
import json

load_dotenv() # carregando variaveis de ambiente.

class bottelegram:
    def __init__(self): # Ser executada toda vez que eu instanciar um objeto do tipo bottelegram.
        TOKEN = os.getenv("API_KEY") # pegando a variavel do ambiente env
        self.url = f"https://api.telegram.org/bot{TOKEN}/" # variavel de objeto. A / é para evitar problemas na codificação, pra nao misturar com outras variaveis.

    def start(self):
        print("Inicializando bot...")
        update_id = None
        while True:
            update = self.get_message(update_id)
            messages = update['result']
            if messages:
                for message in messages:
                    try:
                        update_id = message['update_id']
                        chat_id = message['message']['from']['id']
                        message_text = message['message']['text']
                        resposta_bot = self.criar_resposta(message_text)
                        self.enviar_resposta(chat_id, resposta_bot)
                    except:
                        pass
            
    def get_message(self, update_id): # o self é para conseguir acessar a URL dentro da classe.
        link_request = f"{self.url}getUpdates?timeout=1000"
        if update_id:
            link_request = f"{self.url}getUpdates?timeout=1000&offset={update_id + 1}"
        result = requests.get(link_request)
        return json.loads(result.content)

    def criar_resposta(self):
        return "Opa meu patrão!"

    def enviar_resposta(self, chat_id, resposta):
        link_to_send = f"{self.url}sendMessage?chat_id={chat_id}&text={resposta}"
        requests.get(link_to_send)
        return