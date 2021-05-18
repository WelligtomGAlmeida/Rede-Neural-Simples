from src.Peso import Peso

class Neuronio:

    def __init__(self, padroes):
        self.padroes = padroes
        self.pesos = Peso()

    def calcularSomatorio(self, padrao):
        soma = (padrao.x1 * self.pesos.w1)
        soma = soma + (padrao.x2 * self.pesos.w2)
        soma = soma + (padrao.x3 * self.pesos.w3)

        return soma

    def funcaoLimiar(self, u):
        y = 0
        if u >= 0:
            y = 1
        elif u < 0:
            y = 0

        return y

    def corrigirPesos(self, padrao, y):
        deltaw = []
        n = 0.1
        e = padrao.d - y
        var = n * e

        deltaw.append(var * padrao.x1)
        deltaw.append(var * padrao.x2)
        deltaw.append(var * padrao.x3)

        self.pesos.w1 = self.pesos.w1 + deltaw[0]
        self.pesos.w2 = self.pesos.w2 + deltaw[1]
        self.pesos.w3 = self.pesos.w3 + deltaw[2]

    def calcularEpocas(self, nepoca):
        pesos2 = '\nOs pesos iniciais são: :\n   w1 = ' + str(self.pesos.w1) + '\n   w2 = ' + str(self.pesos.w2) + '\n   w3 = ' + str(self.pesos.w3)

        i = 0
        while i < nepoca:
            for padrao in self.padroes:
                y = self.funcaoLimiar(self.calcularSomatorio(padrao))
                self.corrigirPesos(padrao, y)

            i += 1

        return 'Neuronio Treinado.\n' + pesos2 + '\n\nOs pesos atuais são:\n   w1 = ' + str(self.pesos.w1) + '\n   w2 = ' + str(self.pesos.w2) + '\n   w3 = ' + str(self.pesos.w3)

    def teste(self,teste):
        y = self.funcaoLimiar(self.calcularSomatorio(teste))
        return 'O resultado foi: ' + str(y)