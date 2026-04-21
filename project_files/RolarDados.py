from random import Random
from Dados import Dados

class RolaDados:
    # CONSTRUTOR
    def __init__(self, quantidade: int, seed: int = 0):
        self.dados = []
        
        # se tem seed específica, gerador usa a seed, se não, é "aleatório"
        if seed != 0:
            rd = Random()
            rd.seed(seed)
            
        # cria quantidade de dados @param quantidade
        for _ in range(quantidade):
            if seed == 0:
                self.dados.append(Dados()) # Dado aleatório
            else:
                # Se tem seed, criamos uma "sub-semente" aleatória para cada dado
                self.dados.append(Dados(6, rd.randint(1, 10000)))

    def rolar(self, quais=None) -> list[int]:
        # Rola todos os dados (Primeira jogada)
        if quais is None:
            return [dado.rolar() for dado in self.dados]

        # texto passado de argumento, tipo "1 4 5" (Troca de dados)
        elif isinstance(quais, str):
            # muda string para lista (split: ["1", "4", "5"]
            numeros_digitados = quais.split()
            # Cria lista booleana indicando flags de dados a serem mudados (inicializa como False)
            booleans = [False for _ in range(len(self.dados))]
            
            for num_str in numeros_digitados:
                if num_str.isdigit():
                    # subtração em 1 necessária por a lista de dados é 0-indexada
                    idx = int(num_str) - 1
                    if 0 <= idx < len(self.dados):
                        booleans[idx] = True
                        
            # chama a própria função mas dessa vez ela vai com quais sendo instancia de list (de booleans)
            return self.rolar(booleans)

        # lista (de booleans) passada de argumento
        elif isinstance(quais, list):
            valores_finais = []
            for i, deve_rolar in enumerate(quais):
                # Se for True, nós mandamos aquele dado específico rolar
                if i < len(self.dados) and deve_rolar:
                    self.dados[i].rolar()
                    
                # atualiza os valores dos dados (pros novos que foram rodados e os antigos colocados de novo mas sem mudar)
                valores_finais.append(self.dados[i].getLado())
            return valores_finais

    # impressao
    def __str__(self) -> str:
        # pega o texto de cada dado e corta as quebras de linha
        linhas_por_dado = [dado.toString().split('\n')[:-1] for dado in self.dados]

        resultado = ""
        
        # * -> desempacota a lista, zip -> junta as linhas na horizontal
        for linhas_horizontais in zip(*linhas_por_dado):
            # Junta os 5 dados com um espaço de "    " entre elas
            resultado += "    ".join(linhas_horizontais) + "\n"

        return resultado