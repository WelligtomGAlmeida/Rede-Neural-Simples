from src.Padrao import Padrao
from src.Neuronio import Neuronio

class Main:

    if __name__ == '__main__':
        # Instanciando a lista de dados de entradas
        padroes = []

        # Populando a lista com os dados de entrada
        padroes.append(Padrao(-1, 0, 0, 0))
        padroes.append(Padrao(-1, 0, 1, 0))
        padroes.append(Padrao(-1, 1, 0, 0))
        padroes.append(Padrao(-1, 1, 1, 1))

        neuronio = Neuronio(padroes)
        print(neuronio.calcularEpocas(50))



        print('\n\nAgora, teste o Neuronio!')
        x2 = input('Digite a primeira entrada:')
        x3 = input('Digite a segunda entrada:')

        teste = Padrao(-1, int(x2), int(x3), 0)
        print(neuronio.teste(teste))