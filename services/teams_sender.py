import requests
from config import TEAMS_WEBHOOK_URL

def send_message(nome, categoria):
    msn = {
        "text": f"Olá {nome}, recebemos seu chamado: *{categoria}*. Em breve retornamos."
    }
    requests.post(TEAMS_WEBHOOK_URL, json=msn)