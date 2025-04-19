O código Conversor-Moedas faz exatamente o que o nome propõe:

Converte uma moeda de origem(BRL,USD,JPY,etc) em uma moeda de destino(BRL,USD,JPY,etc)

✏️Nesse projeto eu faço:
1º Peço ao usuário pelo o símbolo da moeda a ser convertida
2º Peço ao usuário pelo símbolo da moeda de destino
3º Peço ao usuário o valor que ele deseja converter
4º Faço uma requisição para a API [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas) para obter dados atualizados do par de moedas Origem/Destino
5º Multiplico o valor obtido com a API pelo valor a ser convertido e apresento ao usuário

📔Exemplo de uso: 

Digite a moeda de origem: USD
Digite a moeda de destino: BRL
Digite o valor a ser convertido: 100

100 USD equivale a 510.32 BRL

😀Motivação para eu fazer esse projeto:

Faz um tempo que não programo absolutamente nada e queria voltar. 
Usei o CHATGPT para me ajudar nesse projeto, mas não com o código. Queria algumas dicas de como fazer mas sem ter a resposta de cara.
Dessa forma eu ainda teria que pesquisar como fazer e ver como as bibliotecas funcionam, de certa forma sem fazer Ctrl+C e Ctrl+V.

💻Tecnologias usadas:

Python 3.13
requests para acesso à API
xml.etree.ElementTree para leitura de XML
Visual Studio Code
Git/GitHub para versionamento
