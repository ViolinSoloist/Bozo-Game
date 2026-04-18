from Placar import Placar

class Bozo:
    def __init__(self):
        self.NUM_JOGADAS = 10
        self.rodada = 1
    
    def main(self):
        seed = int(input("Digite a semente (zero para aleatório): "))
        pl = Placar()
        pl.print_placar()

        for _ in range(self.NUM_JOGADAS):
            print(f"****** Rodada {self.rodada}")
            print("Pressione ENTER para lançar os dados")
            input()

            # TO DO: USAR CLASSE ROLAR E ROLARDADOS PARA ROLAR E IMPRIMIR CONFIGURAÇÃO DOS DADOS


if __name__ == "__main__":
    Bozo().main()