import xml.etree.ElementTree as ET

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