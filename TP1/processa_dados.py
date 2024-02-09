def calcular_distribuicao_escalao_etario(idades):
    distribuicao = {'0-5': 0, '6-10': 0, '11-15': 0, '16-20': 0, '21-25': 0, '26-30': 0, '31-35': 0, '36-40': 0}

    for idade in idades:
        for chave, valor in distribuicao.items():
            limite_inferior, limite_superior = map(int, chave.split('-'))
            if limite_inferior <= idade <= limite_superior:
                distribuicao[chave] += 1

    return distribuicao


def parse(linhas):
    modalidades = set()
    aptos = 0
    idades = []

    for linha in linhas[1:]: 
        campos = linha.strip().split(',')
        modalidade = campos[8]
        idade = int(campos[5])
        aptidao = campos[11]

        modalidades.add(modalidade)

        if aptidao:
            aptos_count += 1

        idades.append(idade)

    modalidades_ordenadas = sorted(list(modalidades))
    total_atletas = len(linhas) - 1
    percentagem_aptos = (aptos / total_atletas) * 100
    percentagem_inaptos = 100 - percentagem_aptos
    distribuicao_escalao_etario = calcular_distribuicao_escalao_etario(idades)

    return modalidades_ordenadas, percentagem_aptos, percentagem_inaptos, distribuicao_escalao_etario

def main():
    with open('seu_dataset.csv', 'r') as arquivo:
        linhas = arquivo.readlines()

    modalidades_ordenadas, percentagem_aptos, percentagem_inaptos, distribuicao_escalao_etario = parse(linhas)

    while True:
        print("\nMenu:")
        print("1. Lista ordenada alfabeticamente das modalidades desportivas")
        print("2. Percentagem de atletas aptos e inaptos")
        print("3. Distribuição de atletas por escalão etário")
        print("4. Sair")

        opcao = input("Escolha uma opção (1-4): ")

        if opcao == '1':
            print("Lista ordenada alfabeticamente das modalidades desportivas:", modalidades_ordenadas)
        elif opcao == '2':
            print("Percentagem de atletas aptos:", percentagem_aptos)
            print("Percentagem de atletas inaptos:", percentagem_inaptos)
        elif opcao == '3':
            print("Distribuição de atletas por escalão etário:", distribuicao_escalao_etario)
        elif opcao == '4':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
