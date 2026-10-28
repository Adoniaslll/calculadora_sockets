# Testes Realizados

Os testes abaixo foram executados com cliente e servidor em processos separados usando Python 3.

| Teste | Mensagem enviada | Resposta recebida | Resultado |
|---|---|---|---|
| Soma | `CALC|SOMAR|10|5` | `OK|15` | Passou |
| Subtracao | `CALC|SUBTRAIR|9|4` | `OK|5` | Passou |
| Multiplicacao | `CALC|MULTIPLICAR|3|7` | `OK|21` | Passou |
| Divisao | `CALC|DIVIDIR|20|4` | `OK|5` | Passou |
| Divisao por zero | `CALC|DIVIDIR|8|0` | `ERRO|Nao e possivel dividir por zero` | Passou |
| Valor invalido | `CALC|SOMAR|abc|2` | `ERRO|Os valores devem ser numeros` | Passou |
| Formato invalido | `TEXTO` | `ERRO|Formato invalido` | Passou |
| Operacao desconhecida | `CALC|POTENCIA|2|3` | `ERRO|Operacao desconhecida` | Passou |
| Encerramento | `SAIR` | `BYE|Conexao encerrada` | Passou |

Os arquivos tambem foram compilados com `python -m py_compile servidor.py cliente.py`, sem erros de sintaxe.
