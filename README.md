# Bozó (Jogo de Dados 🎲) 

## Instruções para execução do programa

Execute o programa através do Makefile (no diretório raíz):
```
make run
```

Ou diretamente com o Python (certifique-se de estar no diretório correto):
```
python3 Bozo.py
```

## Sobre o jogo

O **Bozó** é um jogo clássico de dados, muito popular nos estados de Mato Grosso e Mato Grosso do Sul, que mescla perfeitamente a sorte com o raciocínio lógico e estratégico. 

Embora o mecanismo de rolar dados seja simples, os jogadores precisam planejar suas jogadas, criar estratégias e ponderar probabilidades para alcançar a maior pontuação possível. O jogo pode ser disputado individualmente, em duplas ou trios (suportando de 2 a 6 jogadores na vida real).

## 🛠️ Mecânica do Jogo

- **Material:** O jogo utiliza 5 dados tradicionais de 6 faces (D6) e um copo.
- **Lançamentos:** Em cada rodada, o jogador tem até **3 tentativas** de lançamento.
- **Estratégia:** Após o primeiro lançamento, o jogador pode escolher quais dados quer "travar" e quais quer rolar novamente nas tentativas seguintes, buscando formar a combinação mais valiosa.
- **Objetivo:** Preencher todas as posições do placar da melhor forma possível. Quem terminar com a maior somatória de pontos, vence.

## 📊 Placar e Pontuações

Existem 10 posições possíveis no placar que o jogador deve preencher ao longo do jogo. Cada combinação só pode ser usada uma vez por jogador:

| Posição | Nome | Regra para Pontuar | Pontuação |
| :---: | :--- | :--- | :--- |
| **1** | **Ás** | Soma de todos os dados com a face `1` | 1 a 5 |
| **2** | **Duque** | Soma de todos os dados com a face `2` | 2 a 10 |
| **3** | **Terno** | Soma de todos os dados com a face `3` | 3 a 15 |
| **4** | **Quadra** | Soma de todos os dados com a face `4` | 4 a 20 |
| **5** | **Quina** | Soma de todos os dados com a face `5` | 5 a 25 |
| **6** | **Sena** | Soma de todos os dados com a face `6` | 6 a 30 |
| **7** | **Fu (Full Hand)** | Uma Trinca + Um Par (Ex: `3, 3, 3, 5, 5`) | **20 pontos** fixos |
| **8** | **Seguida** | Uma sequência perfeita (Ex: `1, 2, 3, 4, 5` ou `2, 3, 4, 5, 6`) | **30 pontos** fixos |
| **9** | **Quadrada** | Quatro dados com a mesma face (Ex: `4, 4, 4, 4, 1`) | **40 pontos** fixos |
| **10** | **General** | Todos os cinco dados com a mesma face (Ex: `6, 6, 6, 6, 6`) | **50 pontos** fixos |

> **Nota:** A implementação deste repositório simula esta mesma dinâmica em um ambiente virtual de terminal, gerenciando as rolagens, validações e a impressão do placar automaticamente. Para mais informações sobre o jogo, visite a página da Wikipédia sobre ele: _https://pt.wikipedia.org/wiki/Boz%C3%B3_(jogo)_
