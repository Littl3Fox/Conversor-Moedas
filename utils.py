import xml.etree.ElementTree as ET
import requests
#Confere se a moeda é válida e existe.

def confere_moedas(simbolo):

    #Carrego o arquivo .xml com os nomes das moedas e seus respectivos símbolos
    tree = ET.parse("moedas.xml")
    root = tree.getroot()

    #Dicionário vazio para colocar os símbolos e nomes das moedas
    moedas = {} 

    #Aqui eu vou passar por cada elemento do arquivo .xml com os nomes das moedas e seus respectivos símbolos
    #e coloca-las em um dicionário para, posteriormente, ver se a moeda digitada pelo usuário está
    #no dicionário.

    for child in root:

        #child.tag seria o simbolo da moeda(STR) e child.text seria o nome completo
        #A cada iteração eu atualizo o valor do dicionário com um simbolo e moeda diferente
        moedas[child.tag] = child.text 

    simbolo = simbolo.upper()

    if simbolo in moedas:
        return 0
    else:
        raise ValueError(f"Simbolo {simbolo} de moeda invalida")
    
#Confere se o valor passado é válido

def confere_valor(valor):

    if valor <= 0:
        raise ValueError("O valor digitado é inválido!")
    
#Converte as moedas
#Recebe uma lista moedas com a moeda de origem(moedas[0]) e moeda de destino(moeda[1])
#Recebe também o valor a ser convertido

def converte_moedas(moedas,valor):

    #Aqui eu faço uma requisição dos dados para a API
    resposta = requests.get(f"https://economia.awesomeapi.com.br/json/last/{moedas[0]}-{moedas[1]}")

    #Verifico se a requisição funcionou (200) e tive uma resposta favorável.
    if resposta.status_code == 200:
        #Aqui pego os dados da requisição.
        dados = resposta.json()

        #Pego o valor da moeda de destino 
        valor_dest = dados[moedas[0]+moedas[1]]['bid']

        #Retorno o valor convertido
        return valor * float(valor_dest) 
    else:

        raise ValueError("Requisição a API falhou")
