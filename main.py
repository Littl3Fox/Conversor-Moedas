import utils

def main():

    #Aqui e recebo do usuário a moeda de origem(ori) e destino(dest)

    ori = str(input("Digite a moeda de origem: "))
    dest = str(input("Digite a moeda de destino:"))

    #Coloco numa lista para análise
    moedas = [ori,dest]

    #Vejo se as moedas existem de fato
    try:
        for moeda in moedas:
            utils.confere_moedas(moeda)
    except ValueError as error:
        print(error)
        return
    
    #Recebo o valor a ser convertido
    valor = (float(input("Digite o valor a ser convertido: ")))

    #Verifico se o valor é válido
    try:
        utils.confere_valor(valor)
    except ValueError as error:
        print(error)
        return

    #Converto a moeda

    try:
        resultado = utils.converte_moedas(moedas,valor)
        #Mostra o resultado
        print(f"O valor de {valor} de {moedas[0]} equivale a {resultado} de {moedas[1]}")
    except Exception as error:
        print(error)
        return
    
    return 0


if __name__ == "__main__":
    main()
