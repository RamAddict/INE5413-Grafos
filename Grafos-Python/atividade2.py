from graph import *

def kosaraju(grafoN: Grafo):
    def inicializar():
        nonlocal tempo, visitados, fim, ancestral, inicio
        tempo = 0
        for n in grafoN.getNodes():
            visitados[n] = False
            inicio[n] = math.inf
            fim[n] = math.inf
            ancestral[n] = False

  
    def DFS(grafo: Grafo):
        nonlocal tempo, visitados, fim, ancestral, inicio
        sortedOp = sorted(fim.items(), key=lambda kv: kv[1], reverse = True)
        novoE = collections.OrderedDict(sortedOp)

        inicializar()
        for node in novoE.keys():
            if not visitados[node]:
                DFSVisit(grafo, node)
        return (visitados, inicio, ancestral, fim)
    
    def DFSVisit(grafo: Grafo, origem: Node):
        nonlocal tempo, inicio, fim, ancestral, visitados
        visitados[origem] = True
        tempo = tempo+1
        inicio[origem] = tempo
        for node in origem.getNeighbours():
            if not visitados[node]:
                ancestral[node] = origem
                DFSVisit(grafo, node)
        tempo = tempo + 1
        fim[origem] = tempo
    
    def printAncestors(nodo : Node, ancestrais: dict):
            for key,value in ancestrais.items():
                if value == nodo:
                    return ", {}{}".format(key.getLabel(), printAncestors(key, ancestrais))
            return ""
    
    inicio = dict()
    fim = dict()
    ancestral = dict()
    visitados = dict()
    tempo = 0
    inicializar()

    DFS(grafoN)
    ancestralT = DFS(transposeGraph(grafoN))[2]

    for item in ancestralT.items():
        if not item[1]:
            print("{}{}".format(item[0].getLabel(), printAncestors(item[0],ancestralT)))
            
def kahn(grafo):
    ordenados = []
    nodos_sem_entrada = []
    arestas_nVisitada = []
    for edge in grafo.getEdges():
        arestas_nVisitada.append(edge)

    def sem_entrada(nodo):
        for edge in arestas_nVisitada:
            if nodo == edge[1]:
                return False
        return True

    for node in grafo.getNodes():
        if sem_entrada(node):
            nodos_sem_entrada.append(node)

    while nodos_sem_entrada:
        n = nodos_sem_entrada.pop()
        ordenados.append(n.getLabel())
        for m in n.getNeighbours():
            arestas_nVisitada.remove((n,m))
            if sem_entrada(m):
                nodos_sem_entrada.append(m)

    print(ordenados) if arestas_nVisitada == [] else print("Grafo com ciclo")

def kruskal(grafo):
    Arvore = []
    setList = []
    for node in grafo.getNodes():
        S = set()
        S.add(node.getIndex() - 1)
        setList.append(S)

    sortedOp = sorted(grafo.getEdgeWeights().items(), key=lambda kv: kv[1])
    novoE = collections.OrderedDict(sortedOp)
    for key in novoE.keys():
        nodeIndex1 = key[0].getIndex() - 1
        nodeIndex2 = key[1].getIndex() - 1

        if setList[nodeIndex1].isdisjoint(setList[nodeIndex2]):
            Arvore.append((key[0], key[1]))
            union = setList[nodeIndex1].union(setList[nodeIndex2])
            setList[nodeIndex1] = union
            setList[nodeIndex2] = union

    somatorio = 0
    output = ""
    for edge in Arvore:
        somatorio += grafo.getEdgeWeight(edge)
        output += "{}-{}, ".format(edge[0].getLabel(),edge[1].getLabel())
    print(somatorio)
    print(output[:-2])

def main():
    g = Grafo()

    print ("INICIO KOSARAJU (CFC)")
    g.openFileNet()
    print("RESULTADO DO ALGORITMO:")
    kosaraju(g)
    print ('=============================')

    print ("INICIO KAHN (ORDENAÇÃO TOPOLÓGICA)")
    g.openFileNet()
    print("RESULTADO DO ALGORITMO:")
    kahn(g)
    print ('=============================')

    print ("INICIO KRUSKAL")
    g.openFileNet()
    print("RESULTADO DO ALGORITMO:")
    kruskal(g)
    print ('=============================')

main()
