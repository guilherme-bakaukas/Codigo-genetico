# Codigo-genetico
O problema a ser resolvido refere-se ao caixeiro viajante. O desafio basea-se em fazer uma viagem com a menor distância possível, na qual deve-se passar por todas as cidades listadas e retornar a cidade inicial **sem repetir as cidades**.
### Para isso usaremos um algoritmo genetico.
A ideia é criar uma população, isto é, um conjunto de indivíduos que representam possibilidades de caminhos para solucionar o desafio. A partir disso, devemos
selecionar "pais" dessa população, para criar "filhos com mutação", ou seja, com uma alteração no caminho. Feito isso, comparamos os dois indivíduos e mantemos na geração aquele mais apto a resolver o problema (aquele que contém a menor distância total). A partir disso surge o conceito de evolução, em que as gerações criadas tendem a gerar indivíduos melhores de modo a chegar em um padrão com a melhor disposição de caminhos.
