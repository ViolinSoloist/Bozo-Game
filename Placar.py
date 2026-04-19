class Placar:

    def __init__(self):
        self.MAX_PLACES = 10
        self.pontos_no_tabuleiro = [0 for x in range(self.MAX_PLACES)]
        # [#1, #2, #3, #4, #5, #6, #7, #8, #9, #10]
        self.posicao_ocupada = [False for y in range(self.MAX_PLACES)]

    def __formatPlacarToPrint(self) -> list[str]:
        lista = []
        index = 1

        for pos_ocupada in self.posicao_ocupada:
            if pos_ocupada == False:
                conteudo_str = f"({index})" if index == 10 else f"({index}) "
                lista.append(conteudo_str)
            else:
                lista.append(f" {self.pontos_no_tabuleiro[index-1]} ")
            index += 1

        return lista


    def printPlacar(self):
        prt_lst = self.__formatPlacarToPrint()
        index = 0
        for _ in range(3):
            print(f"{prt_lst[index]}   |   {prt_lst[index + 6]}   |   {prt_lst[index + 3]}")
            print("-" * 26)
            index += 1
        print(f"       |   {prt_lst[-1]}   |")
        print("       +----------+")
        print()