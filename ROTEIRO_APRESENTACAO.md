# Roteiro de Apresentacao - ate 10 minutos

## 1. Problema e solucao - 1 minuto

"Nosso projeto e uma calculadora em rede. O cliente recebe a operacao do usuario, envia os dados pela rede e o servidor realiza o calculo e devolve o resultado."

## 2. Arquitetura - 1 minuto

Mostrar `diagrama_arquitetura.svg` e explicar os dois processos, o endereco IP e a porta TCP 5000.

## 3. Escolha do TCP - 1 minuto

Explicar que os calculos exigem mensagens completas, confiaveis e na ordem correta. Com UDP seriam necessarios confirmacao, identificacao e reenvio.

## 4. Protocolo da aplicacao - 2 minutos

Mostrar estes exemplos:

```text
CALC|SOMAR|10|5
OK|15
CALC|DIVIDIR|8|0
ERRO|Nao e possivel dividir por zero
```

Explicar que cada mensagem termina com uma quebra de linha e usa `|` para separar os campos.

## 5. Demonstracao - 2 minutos

1. Iniciar `servidor.py`.
2. Iniciar `cliente.py`.
3. Demonstrar uma soma correta.
4. Demonstrar divisao por zero.
5. Encerrar pela opcao 0.

## 6. Wireshark - 2 minutos

Aplicar o filtro `tcp.port == 5000`, mostrar o handshake, usar **Follow TCP Stream** e apontar as mensagens do protocolo.

## 7. Conclusao - 1 minuto

"O projeto demonstrou comunicacao entre processos usando sockets TCP, protocolo proprio, tratamento de erros e analise do trafego de rede."

## Perguntas que cada integrante deve saber responder

- O que fazem `bind`, `listen`, `accept`, `connect` e `sendall`?
- Por que foi usado TCP?
- O que significa a porta 5000?
- Como o servidor identifica cada campo da mensagem?
- Como a divisao por zero e tratada?
- Qual e a diferenca entre o protocolo TCP e o protocolo criado pela aplicacao?
- O que mudaria se UDP fosse utilizado?
