import math
import collections
import heapq
import os
import random

class Node():
    def __init__(self, label, index):
        self.label = label
        self.index = index
        self.neighbours = set()

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return (self.label and self.index) == (other.label and other.index)
        else:
            return NotImplemented

    def __hash__(self):
        return hash((self.label, self.index))

    def __str__(self):
        vizinhos = ""
        retorno = "Nodo_%d(%s), nodos adjacentes:\n" % (self.index,self.label)
        for nodo in self.neighbours:
            vizinhos += str("\t%s\n" % (nodo.getLabel()))
        return "%s%s" % (retorno, vizinhos)

    def getLabel(self):
        return self.label

    def getIndex(self):
        return self.index

    def addNeighbour(self, node):
        self.neighbours.add(node)

    def getNeighbours(self):
        return self.neighbours

class Grafo():
    def __init__(self):
        self.nodes = []
        self.edges = set()
        self.edgeWeight = dict()
        self.ponderado = False
        self.dirigido = False

    def setNodes(self, nodeList: [Node]):
        self.nodes = nodeList

    def setEdges(self, edgeList: set):
        self.edges = edgeList

    def setEdgeWeight(self, edgeWeights: dict):
        self.edgeWeight = edgeWeights

    def setDirigido(self, dir):
        self.dirigido = dir

    def setPonderado(self, pon):
        self.ponderado = pon

    def getDirigido(self):
        return self.dirigido

    def getPonderado(self):
        return self.ponderado

    def getNodes(self):
        return self.nodes

    def getEdgeWeight(self,edge):
        return self.edgeWeight.get(edge, math.inf)

    def getEdges(self):
        return self.edges

    def addNode(self, node: Node):
        self.nodes.append(node)

    def addEdge(self, u, v, w):
        self.edges.add((u,v))
        self.edgeWeight[(u,v)] = w

    def getNodeAmmt(self):
        return len(self.nodes)

    def getEdgeAmmt(self):
        return len(self.edges)//2

    def degree(self, node: Node):
        return len(neighbours)

    def neighbours(node: Node):
        return node.neighbours

    def hasEdge(self, u: Node, v: Node):
        return u in v.neighbours

    def getNodeFromIndex(self, idx):
        return self.nodes[idx-1]

    def openFile(self, file):
        ponderado = False
        f = open(file)
        file_lines = f.read().split("\n")

        split_line = file_lines.pop(0).split(" ")
        nodeAmt = int(split_line[1])

        ## Populando Nodos
        for i in range(nodeAmt):
            nodeLabel = ""
            split_line = file_lines.pop(0).split(" ")
            nodeLabel += split_line[1]
            for part in split_line[2:]:
                nodeLabel += " %s"%part
            if (nodeLabel != ""):
                self.nodes.append(Node(nodeLabel, int(split_line[0])))

        # Populando edges
        split_line = file_lines.pop(0).split(" ")
        
        self.dirigido = True if (split_line[0] != "*edges") else False
        for i in range(len(file_lines)-1):
            split_line = file_lines.pop(0).split(" ")
            u = int(split_line[0])-1
            v = int(split_line[1])-1
            w = float(split_line[2])
            if (w != 1):
                self.ponderado = True
            self.nodes[u].addNeighbour(self.nodes[v])
            self.addEdge(self.nodes[u], self.nodes[v], w)
            
            print(self.nodes[u].getLabel())
            if (not self.dirigido):
                self.nodes[v].addNeighbour(self.nodes[u])
                self.addEdge(self.nodes[v], self.nodes[u], w)
        print(self.dirigido)
        print(self.ponderado)
            

def BFS(g: Grafo, s: int):
    origin = g.getNodeFromIndex(s)
    nodeAncestor = dict()
    nodeDistance = dict()
    nodeVisited = dict()
    for node in g.nodes:
        nodeVisited[node] = False
        nodeDistance[node] = math.inf

    nodeVisited[origin] = True
    nodeDistance[origin] = 0
    q = [origin]

    while q:
        u = q.pop(0)
        for v in u.getNeighbours():
            if not nodeVisited[v]:
                nodeVisited[v] = True
                nodeDistance[v] = nodeDistance[u] +1
                nodeAncestor[v] = u
                q.append(v)

    sortedOp = sorted(nodeDistance.items(), key=lambda kv: kv[1])
    sorted_distances = collections.OrderedDict(sortedOp)
    showOut = ""
    actual = -1
    for elemt in sorted_distances:
        if (sorted_distances[elemt] > actual and sorted_distances[elemt] != math.inf):
            actual += 1
            showOut += "\n%d: %s" % (actual, elemt.getLabel())
        else:
            showOut += ", %s" % elemt.getLabel()
    showOut = showOut.strip()
    print(showOut)

def buscarSubcicloEuleriano(g: Grafo, s: int, visited: dict):
    node = g.getNodeFromIndex(s)
    ciclo = [node]

    end = node
    while(True):
        selected_edge = 0
        adjacent_node = 0
        for adjacent_node in node.getNeighbours():
            if(not visited[(node,adjacent_node)] or not visited[(adjacent_node,node)]):
                selected_edge = (node,adjacent_node)
                break

        if(not selected_edge):
            return (False, [])
        visited[selected_edge] = True
        visited[adjacent_node, node] = True
        node = adjacent_node
        ciclo.append(node)
        if node == end:
            break

    for vertex in ciclo:
        for adjacent_vertex in vertex.getNeighbours():
            if (not visited[(vertex, adjacent_vertex)]):
                retorno = buscarSubcicloEuleriano(g, vertex.getIndex(), visited)
                if (not retorno[0]):
                    return (False, [])
                ciclo = joinCycles(ciclo,retorno[1])
    return (True, ciclo)


def hierholzer(g: Grafo):
    visited = {}
    for edge in g.edges:
        visited[edge] = False

    node = g.getNodeFromIndex(random.randint(1,g.getNodeAmmt()))
    retorno = buscarSubcicloEuleriano(g, node.getIndex(), visited)
    if ((not retorno[0]) or (False in visited)):
        print(0)
    else:
        print(1)
        out = ""
        for vertex in retorno[1]:
            out += str(vertex.getLabel()) + ", "
        print(out)

def joinCycles(l1: [], l2: []):
    element = l2[0]
    mid = l1.index(element)
    l1.remove(element)
    for i in range(len(l2)):
        l1.insert(mid+i,l2[i])
    return l1

def printBell(dist: dict, ancest: dict, node: Node):
    origin = node
    out = "%s" % node.getLabel()
    while(ancest[node] != 0):
        out += ", %s" % ancest[node].getLabel()
        node = ancest[node]
    out+="; d=%.2f" % dist[origin]

    return out



def bellmanFord(g: Grafo, s: int):
    origin = g.getNodeFromIndex(s)
    dist = {}
    ancetral = {}

    for n in g.getNodes():
        dist[n] = math.inf
        ancetral[n] = 0
    dist[origin] = 0

    for i in g.getNodes()[:-1]:
        for edge in g.getEdges():
            if (dist[edge[1]] > dist[edge[0]] + g.edgeWeight[edge]):
                dist[edge[1]] = dist[edge[0]] + g.edgeWeight[edge]
                ancetral[edge[1]] = edge[0]

    for edge in g.getEdges():
        if (dist[edge[1]] > dist[edge[0]] + g.edgeWeight[edge]):
            return (False, None, None)
    for node in g.getNodes():
        print("%d: %s" % (node.getIndex(), printBell(dist,ancetral, node)))

    return (True, dist, ancetral)


def floydwarshal(g :Grafo):
    distances = []
    for vertex in range(g.getNodeAmmt()):
        distances.append([])

    for i in range(g.getNodeAmmt()):
        for j in range(g.getNodeAmmt()):
            u = g.getNodeFromIndex(i)
            v = g.getNodeFromIndex(j)
            distances[i].append(0) if (i == j) else distances[i].append(g.getEdgeWeight((u,v)))
                

    for k in range(g.getNodeAmmt()):
        for i in range(g.getNodeAmmt()):
            for j in range(g.getNodeAmmt()):
                distances[i][j] = min(distances[i][j], (distances[i][k] + distances[k][j]))

    out = ""
    for i in range(len(distances)):
        out += "%d:" % (i+1)
        for element in distances[i]:
            out += "%.1f, " % element
        out = out[:-2]
        out += "\n"
    print(out)
    

    return distances

def showGraph(grafo):
    for n in grafo.nodes:
       print(n)
    for e in grafo.edges:
       print("%d->%d w = %d" % (e[0].getIndex(), e[1].getIndex(), grafo.edgeWeight.get((e[0],e[1]))))

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


def main():
    g = Grafo()
    print ("Os arquivos de grafos disponíveis são:")
    os.system("ls Graph")
    fileName = input("Insira nome do arquivo do grafo a ser aberto:")
    fileName = (fileName+".net")  if fileName[-4:] != ".net"  else fileName
    print("Abrindo grafo: %s" % (fileName[:-4]))
    
    try:
        g.openFile("Graph/%s" % fileName)
    except:
        try:
            g.openFile(fileName)
        except:
            print("Arquivo não encontrado.")
            return 0

    # print ("Grafo criado")
    # print ("INICIO BFS")

    # BFS(g, 1)

    # print ("FIM BFS")
    # print ("INICIO HIERHOLZER")

    # hierholzer(g)

    # print ("FIM HIERHOLZER")
    # print ("INICIO BELLMANFORD")

    # bellmanFord(g, 1)

    # print ("FIM BELLMANFORD")
    # print ("INICIO FLOYDWARSHAL")

    # floydwarshal(g)

    # print ("FIM FLOYDWARSHAL")
    print ('=============================')

    gT = transposeGraph(g)
    # for node in g.getNodes():
    #     print(node)

    # print(len(g.getEdges()))
    # print(len(g.getNodes()))
    for edge in gT.getEdges():
        print("{} -> {}, {}".format(edge[0].getLabel(), edge[1].getLabel(), gT.getEdgeWeight(edge)))

    # for node in g.getNodes():
    #     print(node.getLabel())

if __name__ == "__main__":
    main()
