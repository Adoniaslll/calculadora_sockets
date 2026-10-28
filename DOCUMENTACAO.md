# Documentacao Tecnica

## 1. Qual problema a aplicacao resolve?

A aplicacao permite realizar calculos em outro processo pela rede. O usuario escolhe uma operacao no cliente, e o servidor recebe os valores, faz o calculo e devolve o resultado. O projeto demonstra de forma simples a comunicacao entre processos usando sockets.

## 2. Quem sao os processos envolvidos na comunicacao?

Existem dois processos independentes:

- **Cliente:** recebe a opcao e os numeros digitados pelo usuario, monta a mensagem e a envia.
- **Servidor:** fica aguardando conexoes na porta 5000, interpreta a mensagem, executa o calculo e envia uma resposta.

## 3. Como ocorre a comunicacao entre cliente e servidor?

1. O servidor cria um socket TCP, associa esse socket a porta 5000 e aguarda conexoes.
2. O cliente abre uma conexao com o endereco IP e a porta do servidor.
3. O cliente envia uma mensagem do protocolo da aplicacao.
4. O servidor separa os campos, valida os dados e executa a operacao.
5. O servidor envia o resultado ou uma mensagem de erro.
6. A conexao continua aberta para novos calculos ate o cliente enviar `SAIR`.

## 4. Qual protocolo de transporte foi escolhido?

Foi escolhido o **TCP**.

## 5. Por que o TCP e adequado?

O TCP e adequado porque oferece comunicacao orientada a conexao, entrega confiavel e preservacao da ordem dos dados. Uma calculadora precisa receber todos os campos da operacao corretamente e associar cada resposta ao pedido correspondente.

A aplicacao tambem aproveita o TCP para manter a mesma conexao durante varios calculos.

## 6. Qual e o protocolo utilizado pela aplicacao?

Foi criado um protocolo textual simples. Cada mensagem ocupa uma linha e termina com `\n`. Os campos sao separados por `|`.

### Mensagens do cliente

```text
CALC|OPERACAO|NUMERO1|NUMERO2
SAIR
```

### Mensagens do servidor

```text
OK|RESULTADO
ERRO|DESCRICAO
BYE|DESCRICAO
```

Exemplo completo:

```text
Cliente -> Servidor: CALC|DIVIDIR|20|4
Servidor -> Cliente: OK|5
```

## 7. Quais mensagens podem ser trocadas?

| Mensagem | Finalidade |
|---|---|
| `CALC|SOMAR|A|B` | Somar A e B |
| `CALC|SUBTRAIR|A|B` | Subtrair B de A |
| `CALC|MULTIPLICAR|A|B` | Multiplicar A por B |
| `CALC|DIVIDIR|A|B` | Dividir A por B |
| `SAIR` | Encerrar a sessao do cliente |
| `OK|resultado` | Informar que o calculo funcionou |
| `ERRO|descricao` | Informar um dado ou comando invalido |
| `BYE|descricao` | Confirmar o encerramento da conexao |

## 8. O que aconteceria se UDP fosse utilizado?

Com UDP nao existiria uma conexao permanente. Cada operacao seria enviada em um datagrama independente. Uma mensagem poderia ser perdida, duplicada ou chegar fora de ordem. Para oferecer a mesma confiabilidade, a aplicacao teria que adicionar identificadores, confirmacoes de recebimento, tempo limite e retransmissao. Isso aumentaria o codigo sem trazer vantagem importante para esta calculadora.

## 9. Quais situacoes de erro podem ocorrer?

- servidor nao iniciado ou inacessivel;
- opcao inexistente no menu;
- mensagem em formato incorreto;
- valor que nao e numerico;
- divisao por zero;
- operacao desconhecida;
- conexao encerrada inesperadamente;
- porta 5000 ocupada por outro programa.

## 10. Como os erros sao tratados?

- O cliente mostra uma mensagem quando nao consegue se conectar.
- Opcoes invalidas sao recusadas antes do envio.
- O servidor verifica a quantidade e o tipo dos campos recebidos.
- A conversao dos numeros utiliza `try/except`.
- A divisao por zero e verificada antes do calculo.
- Erros de dados produzem uma resposta iniciada por `ERRO|` sem derrubar o servidor.
- Erros de socket sao capturados e exibidos de forma legivel.
- `Ctrl+C` encerra cliente ou servidor sem mostrar uma longa mensagem de excecao.

## Explicacao do codigo do servidor

### Constantes

`HOST = "0.0.0.0"` permite receber conexoes locais ou de outro computador. `PORTA = 5000` define a porta usada pelo projeto.

### Funcao `calcular`

Recebe uma linha do protocolo, divide os campos com `split("|")`, valida o formato e converte os numeros para `float`. Em seguida, usa `if/elif` para escolher a operacao. A funcao sempre devolve `OK|...` ou `ERRO|...`.

### Funcao `iniciar_servidor`

Cria o socket com IPv4 (`AF_INET`) e TCP (`SOCK_STREAM`). Depois usa `bind`, `listen` e `accept`. Cada linha recebida e processada, e `sendall` envia a resposta completa. Ao receber `SAIR`, encerra apenas a conexao daquele cliente e volta a aguardar outro.

## Explicacao do codigo do cliente

### Endereco do servidor

Sem argumento, o cliente usa `127.0.0.1`, que representa a propria maquina. Tambem e possivel informar outro IP na linha de comando.

### Menu e mensagens

O dicionario `OPERACOES` transforma a opcao numerica no nome usado pelo protocolo. O cliente monta a linha `CALC|OPERACAO|NUMERO1|NUMERO2`, usa `sendall` e le uma linha de resposta.

### Tratamento da resposta

A resposta e separada no primeiro `|`. Se comecar com `OK`, o cliente mostra o resultado. Caso contrario, mostra a descricao do erro.

## Limitacoes intencionais

O servidor atende um cliente por vez. Isso mantem o codigo curto e atende ao requisito minimo. Clientes simultaneos, autenticacao, banco de dados e logs aparecem no enunciado apenas como desafios extras.
