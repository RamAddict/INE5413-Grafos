import math
import collections

class Node():
    def __init__(self, label, index):
        self.label = label
        self.index = index
        self.neighbours = set()
    
    def __str__(self):
        if(not self.index):
            return ""
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

    def getNodes(self):
        return self.nodes

    def getEdgeWeight(self,edge):
        return self.edges[edge]
    
    def getEdges(self):
        return self.edges
    
    def addNode(self, node: Node):
        self.nodes.append(node)

    def addEdge(self, u, v, w):
        self.edges.add((u,v))
        self.edgeWeight[(u,v)] = w

    def getNodeAmmt(self):
        return len(self.nodes)-1
    
    def getEdgeAmmt(self):
        return len(self.edges)

    def degree(self, node: Node):
        return len(neighbours)
    
    def neighbours(node: Node):
        return node.neighbours

    def hasEdge(self, u: Node, v: Node):
        return u in v.neighbours

    def weight(self, edge):
        return edgeWeight[edge]

    def getNodeFromIndex(self, idx):
        return self.nodes[idx]

    def openFile(self, file):
        f = open(file)
        file_lines = f.read().split("\n")
        #print(file_lines)
        
        split_line = file_lines[0].split(" ")
        nodeAmt = int(split_line[1])
        
        ## Populando Nodos
        self.nodes.append(Node("vazio",0))
        for i in range(1, nodeAmt+2):
            nodeLabel = ""
            split_line = file_lines[i].split(" ")
            split_line.pop(0)
            for part in split_line:
                nodeLabel += "%s "%part
            if (nodeLabel != ""):
                self.nodes.append(Node(nodeLabel, i))
                #print("Nodo(indice: %d label: %s)" % (i,nodeLabel))
           
        
        split_line = file_lines[nodeAmt+1].split(" ")
        for i in range(nodeAmt+2, len(file_lines)-1):
            split_line = file_lines[i].split(" ")
            u = int(split_line[0])
            v = int(split_line[1])
            w = float(split_line[2])
            #print("Criando edge %d->%d , w =%d" % (u,v,w))
            thisEdge = (self.nodes[u], self.nodes[v])
            self.nodes[u].addNeighbour(self.nodes[v])
            #if(!directed):
            self.nodes[v].addNeighbour(self.nodes[u])
            self.addEdge( u, v, w)
            #print("Aresta do nodo %d -> %d com peso %d" % (u,v,w))
            
        
def BFS(g: Grafo, s: int):
    origin = Grafo.getNodeFromIndex(g,s)
    # creating map of visited nodes
    nodeVisited = dict()
    for node in g.nodes:
        nodeVisited[node] = False
    nodeDistance = dict()
    for node in g.nodes:
        nodeDistance[node] = math.inf
    nodeAncestor = dict()
    
    nodeVisited[origin] = True
    nodeDistance[origin] = 0
    q = [origin]

    while q:
        u = q.pop()
        # print(nodeDistance[u])
        for v in u.getNeighbours():
            if not nodeVisited[v]:
                nodeVisited[v] = True
                nodeDistance[v] = nodeDistance[u] +1
                nodeAncestor[v] = u
                q.append(v)

    sortedShit = sorted(nodeDistance.items(), key=lambda kv: kv[1])                
    sorted_distances = collections.OrderedDict(sortedShit)
    showOut = ""
    actual = -1
    for elemt in sorted_distances:     
        if (sorted_distances[elemt] > actual and sorted_distances[elemt] != math.inf):
            actual += 1
            showOut += "\n%d: %d" % (actual, elemt.getIndex())
        elif (elemt.getIndex() is not 0):
            showOut += ", %d" % elemt.getIndex()
    print(showOut)

def hierholzer(g: Grafo):
    edge_count = {}
    # for e in g.edges:
#       
        
    

def showGraph(grafo):
    for n in grafo.nodes:
       print(n)
    for e in grafo.edges:
       print("%d->%d w = %d" % (e[0], e[1], grafo.edgeWeight.get((e[0],e[1]))))


def main():
    g = Grafo()
    g.openFile("Graph/facebook_santiago.net")
    BFS(g, 2)
    
    # n tem nodo 0 é pq existe de 1 -> 3 é, mas tem indice 0 no array de nodos

    #print(g.hasEdge(g.getNodeFromIndex(1), g.getNodeFromIndex(2)))

    #showGraph(g)
    


if __name__ == "__main__":
    main()
    