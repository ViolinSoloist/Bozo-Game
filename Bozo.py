from Placar import Placar
from RolarDados import RolaDados


class Bozo:
    def __init__(self):
        self.NUM_JOGADAS = 10
        self.QNTD_DADOS = 5
        self.rodada = 1

    def __printarDados__(self, rd):
        print("1          2          3          4          5")
        print(rd)    
    
    def main(self):
        seed = int(input("Digite a semente (zero para aleatório): "))
        pl = Placar()
        pl.printPlacar()
        rd = RolaDados(self.QNTD_DADOS) if seed == 0 else RolaDados(self.QNTD_DADOS, seed)
        
        for _ in range(self.NUM_JOGADAS):
            print(f"****** Rodada {self.rodada}")
            print("Pressione ENTER para lançar os dados")
            input()

            # primeira tentativa:
            rd.rolar()
            self.__printarDados__(rd)

            # segunda tentativa
            muda = input("Digite os números dos dados que quiser TROCAR. Separados por espaços.\n")
            rd.rolar(muda)
            self.__printarDados__(rd)

            #terceira tentativa
            muda = input("Digite os números dos dados que quiser TROCAR. Separados por espaços.\n")
            valores = rd.rolar(muda)
            self.__printarDados__(rd)

            print("\n\n")
            pl.printPlacar()

            # incremento de rodada
            self.rodada += 1

            
            


if __name__ == "__main__":
    Bozo().main()