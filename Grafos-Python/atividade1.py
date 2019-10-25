from graph import *

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


def main():
    g = Grafo()
    g.openFile()

    print ("Grafo criado")
    print ("INICIO BFS")

    BFS(g, 1)

    print ("FIM BFS")
    print ("INICIO HIERHOLZER")

    hierholzer(g)

    print ("FIM HIERHOLZER")
    print ("INICIO BELLMANFORD")

    bellmanFord(g, 1)

    print ("FIM BELLMANFORD")
    print ("INICIO FLOYDWARSHAL")

    floydwarshal(g)

    print ("FIM FLOYDWARSHAL")
    print ('=============================')

main()