# uma população seria uma matriz de modo que cada vetor indica um indivíduo
# cada individuo é um vetor de caminhos ex(3 cidades): [2,1,3]
# a matriz distâncias contém um vetor para cada cidade, na qual cada posição desse vetor indica a distância com uma cidade
# exemplo de 3 cidades:
# distâncias = [[0,10,30],[10,0,40],[30,40,0]]
# distância cidades 1 e 2: 10 // cidades 1 e 3: 30 // cidades 2 e 3: 40

#neste exemplo usaremos 10 cidades
import random
from random import randint
import matplotlib.pyplot as plt

distancias=[[0,54,38,33,70,34,26,56,38,52],[54,0,16,29,43,24,51,71,47,29],[38,16,0,40,28,75,52,20,53,71],[33,29,40,0,12,21,23,18,32,51]]
a=[70,43,28,12,0,16,63,54,63,43]
distancias.append(a)
a=[34,24,75,21,16,0,30,29,51,39]
distancias.append(a)
a=[26,51,52,23,63,30,0,27,66,45]
distancias.append(a)
a=[56,71,20,18,54,29,27,0,64,19]
distancias.append(a)
a=[38,47,53,32,63,51,66,64,0,28]
distancias.append(a)
a=[52,29,71,51,43,39,45,19,28,0]
distancias.append(a)

#essa função retorna a distância total do caminho do indivíduo
def fitness(individuo, distancias):
    sum=0
    for i in range(len(individuo)-1):
        var = distancias[individuo[i]-1][individuo[i+1]-1]
        #esse -1 é necessário pois a matriz tem posiçoes [0][0] que simbolizam d entre [1][1]
        sum += var
    #volta a cidade inicial
    sum += distancias[individuo[len(individuo)-1]-1][individuo[0]-1]
    return (sum)

# função de criação de uma população com indivíduos aleatórios
# cada indivíduo contém um vetor de caminho possível
def criacao_populacao(popsize,num_cities):
    population=[]
    for i in range(popsize):
        individuo=[]
        count=0
        while(count<num_cities):
            num=randint(1,num_cities)
            if (num not in individuo):
                individuo.append(num)
                count=count+1
        population.append(individuo)
    return (population)

# essa função gera uma nova geração com mutação (troca de posição com dois elementos do vetor)
# exemplo: [1,2,3,4,5,6,7,8,9,10] ==== [1,7,3,4,5,6,2,8,9,10]

def new_generation(population, popsize):

    num_filho=50 #numero de filhos por geração
    children=[]

    for i in range(num_filho):
        # selecionamos um pai aleatorio
        pos_pai=randint(0,popsize-1)
        pai=population[pos_pai]
        new=[]
        for elemento in pai:
            new.append(elemento)

        #escolher duas posições do filho para trocar(mutação)
        pos1=randint(0,num_cities-1)
        pos2=pos1

        #verifica que pos1 !=pos2 para haver mutação de fato
        while(pos2==pos1):
            pos2=randint(0,num_cities-1)

        #realizamos o cross_over(mutação pela troca de posições)
        aux=new[pos1]
        new[pos1]=new[pos2]
        new[pos2]=aux

        #adicionamos o indivíduo a nova geração children
        children.append(new)

    #analisa se haverá uma troca de individuos na geração, comparamos um pai com um filho
    #prevalece na geração aquele com menor fitness (menor distância)
    for i in range(len(children)):
        fit_children=fitness(children[i],distancias)
        pos_aleatorio=randint(0,popsize-1)
        fit_aleatorio=fitness(population[pos_aleatorio],distancias)# comparação dos fitness
        if (fit_children<fit_aleatorio):#ideia do menor fitness ser o melhor

            population[pos_aleatorio]=children[i]

    return (population)

#lista controle foi criada apenas para facilitar a visualização dos dados
lista_controle=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
popsize=100
num_cities=10
population=criacao_populacao(popsize,num_cities)
generations=1500
x=[]
y=[]

for i in range(generations):

    population=new_generation(population,popsize)
    soma=0
    vetor_fit=[]
    x.append(i)

    for individuo in population:
        vetor_fit.append(fitness(individuo,distancias))
        soma += fitness(individuo,distancias)
    media=soma/len(population)#impressão da media para analise de mudança

    y.append(media)

    if ((i/100) in lista_controle):
        print("Geração ", i)
        print("Menor distância da geração",min(vetor_fit))
        print("Indivíduo com menor distância",population[vetor_fit.index(min(vetor_fit))])
        print("Média das distâncias da população: ", media)
        print("----------------------------------------------------------------------------")

#plotamos gráfico de evolução das gerações
plt.xlabel("gerações")
plt.ylabel("media distâncias")

plt.plot(x,y)
plt.show()
