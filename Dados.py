import random

class Dados:
    def __init__(self, lados=6, seed=None):
        self.lados = lados
        self.atual
        
        if seed is not None:
            random.seed(seed)
            self.fixed_seed = True
        else:
            self.fixed_seed = False

    def rolar(self) -> int:
        self.atual = random.randint(1, self.lados)
        return self.atual