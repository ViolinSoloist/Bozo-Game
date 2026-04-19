import random
from Dados import Dados

class RolaDados:

    def __init__(self, quantidade: int, seed: int = 0):
        self.dados = []

        if seed != 0:
            random.seed(seed)

        for _ in range(quantidade):
            if seed == 0:
                self.dados.append(Dados(6))
            else:
                self.dados.append(Dados(6, random.randint(1, 100000)))

    """ def rolar(self, especificados=None) -> list[int]:
        if especificados == None:
            return [d.rolar() for d in self.dados]
        
        elif isinstance(especificados, str):
            numeros_digitados = especificados.split()
            booleans = [False for _ in range(len(self.dados))]

            for num_str in numeros_digitados:
                if num_str.isdigit():
                    idx = int(num_str) - 1
                    if """