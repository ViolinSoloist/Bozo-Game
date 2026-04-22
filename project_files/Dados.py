from random import Random

class Dados:
    def __init__(self, lados=6, seed=0):
        self.lados = lados
        self.atual = 0
        
        if seed == 0:
            self.gerador = Random() # Aleatório real
        else:
            self.gerador = Random(seed) # gerador com seed
            
        self.rolar()

    def rolar(self):
        self.atual = self.gerador.randint(1, self.lados)
    
    def getLado(self) -> int:
        return self.atual
    
    s_border = "+-----+\n"
    s010 = "|  *  |\n"
    s100 = "|*    |\n"
    s001 = "|    *|\n"
    s000 = "|     |\n"
    s101 = "|*   *|\n"
    s111 = "|* * *|\n"

    def toString(self) -> str:
        
        if self.lados != 6:
            return "Não há representação para esse dados"
        
        string_dice = self.s_border
        
        match self.getLado():
            case 1:
                string_dice += (self.s000 + self.s010 + self.s000)
            case 2:
                string_dice += (self.s100 + self.s000 + self.s001)
            case 3:
                string_dice += (self.s100 + self.s010 + self.s001)
            case 4:
                string_dice += (self.s101 + self.s000 + self.s101)
            case 5:
                string_dice += (self.s101 + self.s010 + self.s101)
            case 6:
                string_dice += (self.s111 + self.s000 + self.s111)
        
        string_dice += self.s_border

        return string_dice