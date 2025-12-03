import time
from services.fluig_api import get_chamados
from services.classifier import classify
from services.teams_sender import send_message
from services.database import init_db, ja_enviado, marcar_como_enviado
from config import CHECK_INTERVAL_SECONDS

def main():
    print("BOT iniciado...")

    init_db()

    while True:
        chamados = get_chamados()

        for c in chamados:
            id_chamado = c.get("documentid")
            nome = c.get("solicitante")
            descricao = c.get("descricao")

            if ja_enviado(id_chamado):
                continue

            categoria = classify(descricao)
            send_message(nome, categoria)
            marcar_como_enviado(id_chamado)

            print(f"Mensagem enviada para {nome} | Categoria: {categoria}")

        time.sleep(CHECK_INTERVAL_SECONDS)

if __name__ == "__main__":
    main()
