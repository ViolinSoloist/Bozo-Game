import random
from Dados import Dados

class RolaDados:
    # 1. O CONSTRUTOR
    def __init__(self, quantidade: int, seed: int = 0):
        self.dados = []
        
        # Se uma semente geral foi passada, nós configuramos o gerador principal
        if seed != 0:
            random.seed(seed)
            
        # Criamos a quantidade de dados solicitada (no Bozó, serão 5)
        for _ in range(quantidade):
            if seed == 0:
                self.dados.append(Dados(6)) # Dado totalmente aleatório
            else:
                # Se tem seed, criamos uma "sub-semente" aleatória para cada dado
                self.dados.append(Dados(6, random.randint(1, 100000)))

    # 2. O MÉTODO ÚNICO DE ROLAGEM (Substitui os 3 do Java)
    def rolar(self, quais=None) -> list[int]:
        # CENÁRIO A: Não passou nada. Rola todos os dados! (Primeira jogada)
        if quais is None:
            return [d.rolar() for d in self.dados]

        # CENÁRIO B: Passou um texto tipo "1 4 5" (Troca de dados)
        elif isinstance(quais, str):
            # Transforma a string numa lista de textos: ["1", "4", "5"]
            numeros_digitados = quais.split()
            # Cria uma lista de Falsos do tamanho dos nossos dados
            booleans = [False for _ in range(len(self.dados))]
            
            for num_str in numeros_digitados:
                if num_str.isdigit():
                    # Subtraímos 1 porque o usuário digita 1 a 5, mas a lista vai de 0 a 4
                    idx = int(num_str) - 1
                    if 0 <= idx < len(self.dados):
                        booleans[idx] = True
                        
            # Agora que temos a lista de booleanos [True, False, False, True, True],
            # chamamos a nós mesmos para executar o Cenário C!
            return self.rolar(booleans)

        # CENÁRIO C: Passou a lista de booleanos (A rolagem real acontece aqui)
        elif isinstance(quais, list):
            valores_finais = []
            for i, deve_rolar in enumerate(quais):
                # Se for True, nós mandamos aquele dado específico rolar
                if i < len(self.dados) and deve_rolar:
                    self.dados[i].rolar()
                    
                # Guardamos o valor do dado (seja ele novo ou o antigo que foi mantido)
                valores_finais.append(self.dados[i].getLado())
            return valores_finais

    # 3. IMPRESSÃO LADO A LADO (O jeito Pythônico de fazer)
    def __str__(self) -> str:
        # Pegamos o texto de cada dado e "cortamos" nas quebras de linha (\n)
        # O [:-1] joga fora a última quebra de linha vazia para não dar erro
        linhas_por_dado = [d.toString().split('\n')[:-1] for d in self.dados]

        resultado = ""
        
        # O * (asterisco) desempacota a lista, e o zip junta as linhas na horizontal
        for linhas_horizontais in zip(*linhas_por_dado):
            # Junta as 5 fatias com um espaço de "    " entre elas
            resultado += "    ".join(linhas_horizontais) + "\n"

        return resultado