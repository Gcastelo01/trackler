import dotenv
from os import system

env = dotenv.dotenv_values("../.env")

def send_alert(assunto="Assunto do e-mail", texto="Corpo do e-mail"):
    """
    Envia um alerta com o assunto e o texto especificados nos parâmetros. Utiliza o sistema MUTT do linux. Exige configuração prévia.
    """
    # Escrevendo corpo do e-mail
    f = open("../temp/mailBody.txt", "w+")
    f.write(texto)
    f.close()

    # Enviando e-mail utilizando sistema mutt
    system(f"mutt -s 'teste' {env['EMAIL']} < teste.txt")
    system("rm ../temp/mailBody.txt")
