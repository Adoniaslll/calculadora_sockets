# Captura e Analise no Wireshark

A captura deve ser feita durante a execucao real do projeto. Assim, as imagens apresentadas serao evidencias verdadeiras produzidas no computador da equipe.

## Captura na mesma maquina

1. Abra o Wireshark.
2. Selecione a interface de loopback. No Windows com Npcap, ela normalmente aparece como **Adapter for loopback traffic capture**.
3. Inicie a captura.
4. Em um terminal, execute `python servidor.py`.
5. Em outro terminal, execute `python cliente.py`.
6. Realize pelo menos estes testes:
   - soma de 10 e 5;
   - divisao de 20 por 4;
   - divisao de 8 por 0;
   - encerramento com a opcao 0.
7. Pare a captura.
8. Use o filtro:

```text
tcp.port == 5000
```

## Captura entre dois computadores

Selecione a interface Wi-Fi ou Ethernet usada pelos computadores. Execute o servidor em um computador e o cliente no outro. O mesmo filtro `tcp.port == 5000` pode ser utilizado.

## Evidencias que devem ser salvas

Tire capturas de tela e coloque-as na apresentacao:

1. estabelecimento da conexao TCP, mostrando `SYN`, `SYN, ACK` e `ACK`;
2. pacote com dados da aplicacao;
3. opcao **Follow > TCP Stream**, exibindo as mensagens do protocolo;
4. encerramento da conexao, mostrando pacotes com `FIN` e `ACK`.

Salve tambem o arquivo da captura como `captura_calculadora.pcapng`.

## O que explicar

- O IP de origem identifica quem enviou o pacote.
- O IP de destino identifica quem recebeu.
- A porta do servidor e 5000.
- A porta do cliente e temporaria e escolhida pelo sistema operacional.
- TCP estabelece uma conexao antes de transportar os dados.
- As mensagens `CALC`, `OK`, `ERRO`, `SAIR` e `BYE` pertencem ao protocolo criado pela equipe.

## Resultado esperado no Follow TCP Stream

```text
CALC|SOMAR|10|5
OK|15
CALC|DIVIDIR|20|4
OK|5
CALC|DIVIDIR|8|0
ERRO|Nao e possivel dividir por zero
SAIR
BYE|Conexao encerrada
```

## Lista de verificacao

- [ ] Captura realizada enquanto cliente e servidor estavam funcionando
- [ ] Filtro `tcp.port == 5000` aplicado
- [ ] Handshake TCP identificado
- [ ] Mensagens da aplicacao identificadas
- [ ] Encerramento da conexao identificado
- [ ] Capturas de tela adicionadas a apresentacao
- [ ] Arquivo `.pcapng` salvo
