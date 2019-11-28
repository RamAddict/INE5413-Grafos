import math
import collections
import os

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

    def clearNeighbour(self):
        self.neighbours = set()

    def getNeighbours(self):
        return self.neighbours
   
    def __repr__(self):
        return str(self.label)

class Grafo():
    def __init__(self):
        self.nodes = [None]*5000
        self.partition1 = [None]*2500
        self.partition2 = [None]*2500
        self.edges = set()
        self.edgeWeight = dict()
        self.dirigido = False
        self.bipartido = False
        self.source = None
        self.target = None
    
    def setSource(self, node):
        self.source = node

    def getSource(self):
        return self.source

    def setTarget(self, node):
        self.target = node

    def setBipartido(self):
        self.bipartido = True

    def getTarget(self):
        return self.target

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

    def getEdgeWeights(self):
        return self.edgeWeight

    def getEdgeWeight(self,edge):
        return self.edgeWeight.get(edge, math.inf)

    def getEdges(self):
        return self.edges

    def addNode(self, node: Node):
        if(self.nodes[node.getIndex()] == None):
            self.nodes.insert(node.getIndex(),node)
    
    def addToPartition1(self, node: Node):
        if(self.partition1[node.getIndex()] == None):
                self.partition1.insert(node.getIndex(),node)
    
    def addToPartition2(self, node: Node):
        if(self.partition2[node.getIndex()] == None):
                self.partition2.insert(node.getIndex(),node)
    
    def addEdge(self, u, v, w):
        self.edges.add((u,v))
        self.edgeWeight[(u,v)] = w

    def getNodeAmmt(self):
        return len(self.nodes)

    def getEdgeAmmt(self):
        return len(self.edges) if self.dirigido else len(self.edges)//2

    def degree(self, node: Node):
        return len(node.neighbours)

    def neighbours(self, node: Node):
        return node.neighbours

    def hasEdge(self, u: Node, v: Node):
        return u in v.neighbours

    def getNodeFromIndex(self, idx):
        return self.nodes[idx-1]

    def openFileNet(self):
        print ("Escolha o grafo a ser aberto.\nOs arquivos de grafos disponíveis são:")
        os.system("ls Graph")
        fileName = input("Insira nome do arquivo do grafo a ser aberto:")
        fileName = (fileName+".net")  if fileName[-4:] != ".net"  else fileName
        print("Abrindo grafo: %s\n" % (fileName[:-4]))
        
        try:
            f = open("Graph/%s" % fileName)
        except:
            try:
                f = open(fileName)
            except OSError as e:
                print(e)
                return 0

        file_lines = f.read().split("\n")
        split_line = file_lines.pop(0).split(" ")
        # nodeAmt = int(split_line[1])

        split_line = file_lines.pop(0).split(" ")
        ## Populando Nodos
        while(not split_line[0][0] == '*'):
            nodeLabel = ""
            nodeLabel += split_line[1]
            for part in split_line[2:]:
                nodeLabel += " %s"%part
            if (nodeLabel != ""):
                self.nodes.append(Node(nodeLabel, int(split_line[0])))
            split_line = file_lines.pop(0).split(" ")

        # Populando edges
        self.dirigido = True if (split_line[0] != "*edges") else False
        split_line = file_lines.pop(0).split(" ")
        while(not split_line[0] == ""):
            u = int(split_line[0])-1
            v = int(split_line[1])-1
            w = float(split_line[2])
            self.nodes[u].addNeighbour(self.nodes[v])
            self.addEdge(self.nodes[u], self.nodes[v], w)
            if file_lines:
                split_line = file_lines.pop(0).split(" ")
            else:
                break
            if (not self.dirigido):
                self.nodes[v].addNeighbour(self.nodes[u])
                self.addEdge(self.nodes[v], self.nodes[u], w)

    def openFileGr(self):
        print ("Escolha o grafo a ser aberto.\nOs arquivos de grafos disponíveis são:")
        os.system("ls Graph")
        fileName = input("Insira nome do arquivo do grafo a ser aberto:")
        fileName = (fileName+".gr")  if fileName[-3:] != ".gr"  else fileName
        print("Abrindo grafo: %s\n" % (fileName[:-3]))
        
        try:
            f = open("Graph/%s" % fileName)
        except:
            try:
                f = open(fileName)
            except OSError as e:
                print(e)
                return 0

        file_lines = f.read().split("\n")
        split_line = file_lines.pop(0).split(" ")

        split_line = file_lines.pop(0).split(" ")
        # Removing useless lines of the file
        while(split_line[0] != 'a' and split_line[0] != 'e'):
            split_line = file_lines.pop(0).split(" ")

        self.dirigido = split_line[0] == 'a'
        ponderado = True

        try:
            split_line[3]
        except:
            ponderado = False

        # Enquanto houver linhas válidas no arquivo
        while(not split_line[0] == ""):
            u = int(split_line[1])-1
            v = int(split_line[2])-1
            w = int(split_line[3]) if ponderado else 1
            nodeU = Node(u+1,u)
            nodeV = Node(v+1,v)
            self.addNode(nodeU)
            self.addNode(nodeV)
            self.nodes[u].addNeighbour(nodeV)
            self.addEdge(nodeU,nodeV,w)
            if(not self.dirigido):
                self.nodes[v].addNeighbour(nodeU)
                self.addEdge(nodeV,nodeU,w)

            if(self.bipartido):
                self.addToPartition1(nodeU)
                self.addToPartition2(nodeV)
                self.partition1[u].addNeighbour(nodeV)
                if(not self.dirigido):
                    self.partition2[v].addNeighbour(nodeU)

            if file_lines:
                split_line = file_lines.pop(0).split(" ")
            else:
                break
            # print("Criando nodo {} e {}".format(u,v))

def transposeGraph(grafo: Grafo):
    new_edges = []
    new_weights = dict()

    for source,target in grafo.getEdges():
        transposed_edge = (target, source)
        new_edges.append(transposed_edge)
        new_weights[transposed_edge] = grafo.getEdgeWeight((source,target))
    
    transposed_graph = Grafo()
    transposed_graph.setEdges(new_edges)
    transposed_graph.setEdgeWeight(new_weights)
    transposed_graph.setNodes(grafo.getNodes())
    transposed_graph.setDirigido(grafo.getDirigido())
    
    for node in transposed_graph.getNodes():
        node.clearNeighbour()
    for source,target in grafo.getEdges():
        transposed_graph.getNodeFromIndex(target.getIndex()).addNeighbour(source)
    
    return transposed_graph