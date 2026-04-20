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


    def __str__(self) -> str:
        prt_lst = self.__formatPlacarToPrint()
        index = 0
        print_str = ""
        for _ in range(3):
            print_str += f"{prt_lst[index]}   |   {prt_lst[index + 6]}   |   {prt_lst[index + 3]}\n"
            for _ in range(26):
                print_str += "-"
            print_str += "\n"
            index += 1
        print_str += f"       |   {prt_lst[-1]}   |\n"
        print_str += "       +----------+\n\n"

        return print_str

    # ---------------- CHECAGEM DE PONTUAÇÃO -----------------------

    def __checkSeq(valores:list[int]) -> bool:
        min = valores[0] - 1
        for valor in valores:
            if valor > min:
                return False
            else:
                min = valor
        return True

    def add(self, pos:int, valores:list[int]) -> None:
        match pos:
            case 8:
                self.__checkSeq(valores)

    def getScore(self):
        pass