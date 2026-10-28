import socket
import sys


HOST = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
PORTA = 5000

OPERACOES = {
    "1": "SOMAR",
    "2": "SUBTRAIR",
    "3": "MULTIPLICAR",
    "4": "DIVIDIR",
}


def mostrar_menu():
    print("\n1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")


def iniciar_cliente():
    with socket.create_connection((HOST, PORTA), timeout=10) as cliente:
        cliente.settimeout(None)
        respostas = cliente.makefile("r", encoding="utf-8")
        print(f"Conectado ao servidor {HOST}:{PORTA}")

        while True:
            mostrar_menu()
            escolha = input("Escolha uma opcao: ").strip()

            if escolha == "0":
                cliente.sendall(b"SAIR\n")
                print(respostas.readline().strip())
                break

            if escolha not in OPERACOES:
                print("Opcao invalida.")
                continue

            numero1 = input("Primeiro numero: ").strip()
            numero2 = input("Segundo numero: ").strip()
            mensagem = f"CALC|{OPERACOES[escolha]}|{numero1}|{numero2}\n"
            cliente.sendall(mensagem.encode("utf-8"))

            resposta = respostas.readline().strip()
            if not resposta:
                print("O servidor encerrou a conexao.")
                break

            tipo, texto = resposta.split("|", 1)
            if tipo == "OK":
                print("Resultado:", texto)
            else:
                print("Erro:", texto)


if __name__ == "__main__":
    try:
        iniciar_cliente()
    except ConnectionRefusedError:
        print("Nao foi possivel conectar. Inicie o servidor primeiro.")
    except (socket.timeout, OSError) as erro:
        print("Erro de conexao:", erro)
    except KeyboardInterrupt:
        print("\nCliente encerrado.")
