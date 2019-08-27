class Node():
    def __init__(self, label, index):
        self.label = label
        self.index = index
        self.neighbours = {}
    

class Grafo():
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.edgeWeight = {}

    def addNode(self, node: Node):
        self.nodes.append(node)

    def addEdge(self, u, v):
        self.edges.append(u,v)

    def getNodeAmmt(self):
        return len(self.nodes)
    
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


    def openFile(self, file):
        f = open(file)
        file_lines = f.read().split("\n")
        #print(file_lines)
        
        split_line = file_lines[0].split(" ")
        nodeAmt = int(split_line[1])
        
        ## Populando Nodos
        for i in range(1, nodeAmt+1):
            nodeLabel = ""
            split_line = file_lines[i].split(" ")
            split_line.pop(0)
            for part in split_line:
                nodeLabel += part
            self.nodes.append(Node(nodeLabel, i-1))
            print("Nodo(indice: %d label: %s)" % (i-1,nodeLabel))
        
        split_line = file_lines[nodeAmt+1].split(" ")
        for i in range(nodeAmt+2, len(file_lines)):
            split_line = file_lines[i].split(" ")
            u = int(split_line[0])
            v = int(split_line[1])
            w = float(split_line[2])

            thisEdge = (self.nodes[u], self.nodes[v])
            
            print(file_lines[i])
            
        
def BFS(g: Grafo, s: int):
    print("s")



def main():
    g = Grafo()
    g.openFile("Graph/dolphins.net")




if __name__ == "__main__":
    main()
    