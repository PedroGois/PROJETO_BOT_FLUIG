from config import KEYWORDS

def classify(texto):
    texto = texto.lower()

    for palavra, categoria in KEYWORDS.items():
        if palavra in texto:
            return categoria

    return "Geral"