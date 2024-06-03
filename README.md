# Trabalho-Teoria-da-Computa-o
Primeiro trabalho de teoria da computação desenvolvido com a supervisão do professor Wellington Aparecido Della Mura, com o fim de aplicar os conceitos aprendidos em aula sobre automatos finitos, o qual prefiro não apresentar no dia designado.
## Automato em .json
```json
{
  "initial": 0,
  "final": [3],
  "transitions": [
    {"from": 0, "read": "a", "to": 1},
    {"from": 1, "read": "b", "to": 2},
    {"from": 2, "read": "c", "to": 3},
    {"from": 3, "read": "a", "to": 1}, 
    {"from": 3, "read": "b", "to": 0},
    {"from": 3, "read": "c", "to": 0}
  ]
}
```
### Arquivo de entrada CSV: 

```CSV
abc;1
aabc;1
ababc;1
abcd;1
aabcc;0
ab;0
cabc;1
abcabc;1
abccba;0
```
### Arquivo de saída gerado ao final da execução:
-
```CSV
abc;1;1;0.0
aabc;1;0;0.0
ababc;1;0;0.0
abcd;1;0;0.0
aabcc;0;0;0.0
ab;0;0;0.0
cabc;1;0;0.0
abcabc;1;1;0.0
abccba;0;0;0.0
```
### Funcionamento
#### Para compilar, não utilizamos IDE's ou interfaces digitais, executamos pelo CMD, entretanto, para acessar foi necessário incluir o caminho da pasta onde está incluso todos os arquivos. Com o seguinte comando:
```bash
 C:\Windows\system32>cd C:\Users\"seu usuario"\"local da pasta"\"pasta com automato e demais arquivos"
```
#### Após o caminho da pasta, é necessário incluir o comando para acessar o código pelo CMD:
```bash
python main.py arquivo_aut.aut arquivo_teste.in arquivo_saida.out
```
