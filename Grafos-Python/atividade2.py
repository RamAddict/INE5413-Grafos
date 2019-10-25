from graph import *

tempo = 0

def transposeGraph(grafo: Grafo):
    new_edges = []
    new_weights = dict()
    
    for edge in grafo.getEdges():
        transposed_edge = (edge[1], edge[0])
        new_edges.append(transposed_edge)
        new_weights[transposed_edge] = grafo.getEdgeWeight(edge)

    transposed_graph = Grafo()
    transposed_graph.setEdges(new_edges)
    transposed_graph.setEdgeWeight(new_weights)
    transposed_graph.setNodes(grafo.getNodes())
    transposed_graph.setDirigido(grafo.getDirigido())
    transposed_graph.setPonderado(grafo.getPonderado())

    return transposed_graph

def kosaraju(grafo: Grafo):
    tempo = 0
    inicio = dict()
    finishing_times = None
    fim = dict()
    ancestral = dict()
    visitados = dict()
    pilha = list()
  

    def DFS(grafo):
        nonlocal tempo, visitados, fim, ancestral, inicio

        for n in grafo.getNodes():
            visitados[n] = False
            inicio[n] = math.inf
            fim[n] = math.inf
            ancestral[n] = False

        sortedOp = sorted(fim.items(), key=lambda kv: kv[1], reverse = True)
        novoE = collections.OrderedDict(sortedOp)
        
        for node in novoE.keys():
            if not visitados[node]:
                DFSVisit(grafo, node)
    
    def DFSVisit(grafo, origem: Node):
        nonlocal tempo, inicio, fim, ancestral, visitados, pilha
        visitados[origem] = True
        tempo = tempo+1
        inicio[origem] = tempo
        for node in origem.getNeighbours():
            if not visitados[node]:
                ancestral[node] = origem
                DFSVisit(grafo, node)
        pilha.insert(0, origem)
        tempo = tempo + 1
        fim[origem] = tempo
    
    def DFSPrint(grafo, origem: Node):
        nonlocal tempo, inicio, fim, ancestral, visitados
        visitados[origem] = True
        print(origem.getLabel(), end='')
        for node in origem.getNeighbours():
            if not visitados[node]:
                DFSPrint(grafo, node)

    for n in grafo.getNodes():
        visitados[n] = False
        inicio[n] = math.inf
        fim[n] = math.inf
        ancestral[n] = False

    tempo = 0
    grafoT = transposeGraph(grafo)

    for n in grafo.getNodes():
        visitados[n] = False
        inicio[n] = math.inf
        fim[n] = math.inf
        ancestral[n] = False
    
    print (pilha)

    while pilha:
        atual = pilha.pop(0)
        if not visitados[atual]:
            DFSPrint(grafoT, atual)
            print("\n")
    # out = ""
    # for node,value in ancestral.items():
    #     if(not value):
    #         out += "\n{}".format(node.getLabel())
    #         for node1, value1 in ancestral.items():
    #             if(value1 == node):
    #                 out += ", {}".format(node1.getLabel())
    #                 node = node1
    #                 value = value1
    
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
    S = []
    for node in grafo.getNodes():
        S.append([node.getIndex() - 1])

    sortedOp = sorted(grafo.getEdgeWeights().items(), key=lambda kv: kv[1])
    novoE = collections.OrderedDict(sortedOp)
    for key in novoE.keys():
        nodeIndex1 = key[0].getIndex() - 1
        nodeIndex2 = key[1].getIndex() - 1

        if not S[nodeIndex1] == S[nodeIndex2]:
            Arvore.append((key[0].getLabel(), key[1].getLabel()))
            x = S[nodeIndex1] + S[nodeIndex2]
            # print(x)
            for w in x:
                S[w] = x
                
    print(Arvore)

def main():
    g = Grafo()
    g.openFile()

    print ("INICIO KOSARAJU (CFC)")
    kosaraju(g)
    print ('=============================')

    print ("INICIO KAHN (ORDENAÇÃO TOPOLÓGICA)")
    kahn(g)
    print ('=============================')

    print ("INICIO KRUSKAL")
    kruskal(g)
    print ('=============================')

main()
