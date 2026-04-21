class Placar:

    def __init__(self):
        self.MAX_PLACES = 10
        self.pontos_no_tabuleiro = [0 for x in range(self.MAX_PLACES)]
        # [#1, #2, #3, #4, #5, #6, #7, #8, #9, #10]
        self.posicao_ocupada = [False for y in range(self.MAX_PLACES)]

    def __str__(self):
        num = ""
        s = ""
        for i in range(3):
            num = f"{self.pontos_no_tabuleiro[i]:<4}" if self.posicao_ocupada[i] else f"({i+1}) "
            s +=   num + "   |   "
            num = f"{self.pontos_no_tabuleiro[i+6]:<4}" if self.posicao_ocupada[i+6] else f"({i+7}) "
            s +=   num + "   |   "
            num = f"{self.pontos_no_tabuleiro[i+3]:<4}" if self.posicao_ocupada[i+3] else f"({i+4}) "
            s+= num + "\n--------------------------\n"
	
        num = f"{self.pontos_no_tabuleiro[9]:<4}" if self.posicao_ocupada[9] else "(10)"
        s += "       |   " + num + "   |"
        s += "\n       +----------+\n"
        return s

    # ---------------- CHECAGEM DE PONTUAÇÃO -----------------------

    def __checkFull(self, valores:list[int]) -> bool:
        v = sorted(valores)

        trinca_primeiro = (v[0] == v[1] == v[2]) and (v[3] == v[4])
        par_primeiro = (v[0] == v[1]) and (v[2] == v[3] == v[4])

        return trinca_primeiro or par_primeiro

    def __checkSeq(self, valores:list[int]) -> bool:
        v = sorted(valores)
        return (v[0] == v[1] - 1) and (v[1] == v[2] - 1) and (v[2] == v[3] - 1) and (v[3] == v[4] - 1)

    def __checkQuadra(self, valores:list[int]) -> bool:
        v = sorted(valores)
        return v[0] == v[3] or v[1] == v[4]
    
    def __checkQuina(self, valores:list[int]) -> bool:
        v = sorted(valores)
        return v[0] == v[4]
    
    def __conta(self, n:int, valores:list[int]) -> int:
        qntd = valores.count(n)
        return qntd  * n

    def add(self, pos:int, valores:list[int]) -> None:
        if self.posicao_ocupada[pos - 1]:
            raise ValueError("Posição ocupada")
        
        pontos = 0
        match pos:
            case 1:
                pontos = self.__conta(1, valores)
            case 2:
                pontos = self.__conta(2, valores)
            case 3:
                pontos = self.__conta(3, valores)
            case 4:
                pontos = self.__conta(4, valores)
            case 5:
                pontos = self.__conta(5, valores)
            case 6:
                pontos = self.__conta(6, valores)
            case 7:
                if self.__checkFull(valores):
                    pontos = 15
            case 8:
                if self.__checkSeq(valores):
                    pontos = 20
            case 9:
                if self.__checkQuadra(valores):
                    pontos = 30
            case 10:
                if self.__checkQuina(valores):
                    pontos = 40
            case _:
                raise IndexError("Valor da posição ilegal")
        
        self.pontos_no_tabuleiro[pos - 1] = pontos
        self.posicao_ocupada[pos - 1] = True
    
    def getScore(self) -> int:
        total = 0
        i = 0
        for ponto in self.pontos_no_tabuleiro:
            if self.posicao_ocupada[i]:
                total += ponto
            i += 1
        return total