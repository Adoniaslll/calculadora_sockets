import socket


HOST = "0.0.0.0"
PORTA = 5000


def calcular(mensagem):
    partes = mensagem.split("|")

    if len(partes) != 4 or partes[0] != "CALC":
        return "ERRO|Formato invalido"

    operacao = partes[1]

    try:
        numero1 = float(partes[2])
        numero2 = float(partes[3])
    except ValueError:
        return "ERRO|Os valores devem ser numeros"

    if operacao == "SOMAR":
        resultado = numero1 + numero2
    elif operacao == "SUBTRAIR":
        resultado = numero1 - numero2
    elif operacao == "MULTIPLICAR":
        resultado = numero1 * numero2
    elif operacao == "DIVIDIR":
        if numero2 == 0:
            return "ERRO|Nao e possivel dividir por zero"
        resultado = numero1 / numero2
    else:
        return "ERRO|Operacao desconhecida"

    return f"OK|{resultado:g}"


def iniciar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        servidor.bind((HOST, PORTA))
        servidor.listen()
        print(f"Servidor aguardando conexoes na porta {PORTA}...")

        while True:
            conexao, endereco = servidor.accept()

            with conexao:
                print(f"Cliente conectado: {endereco[0]}:{endereco[1]}")
                mensagens = conexao.makefile("r", encoding="utf-8")

                for linha in mensagens:
                    mensagem = linha.strip()
                    print("Recebido:", mensagem)

                    if mensagem == "SAIR":
                        resposta = "BYE|Conexao encerrada"
                        conexao.sendall((resposta + "\n").encode("utf-8"))
                        break

                    resposta = calcular(mensagem)
                    conexao.sendall((resposta + "\n").encode("utf-8"))
                    print("Enviado:", resposta)

                print("Cliente desconectado.")


if __name__ == "__main__":
    try:
        iniciar_servidor()
    except KeyboardInterrupt:
        print("\nServidor encerrado.")
    except OSError as erro:
        print("Erro ao iniciar o servidor:", erro)
