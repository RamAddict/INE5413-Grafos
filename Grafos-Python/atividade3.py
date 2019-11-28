from graph import *
def main():
    g = Grafo()
    g.openFileGr()
    r = hopcroftkarp(g)
    print(r[0])
    print(r[1])


# def lawler(g: Grafo):



def hopcroftkarp(g: Grafo):
    def dfs(v):
        if v != None:
            for u in g.getNodeFromIndex(v).getNeighbors(v):
                if dist[pair[u]] == dist[v] + 1 and dfs(pair[u]):
                    pair[u] = v
                    pair[v] = u
                    return True

            dist[v] = math.inf
            return False

        return True

    def bfs():
        for v in g.partition1:
            if pair[v] == None:
                dist[v] = 0
                q.append(v)
            else:
                dist[v] = math.inf

        dist[None] = math.inf

        while len(q) > 0:
            v = q.popleft()
            if v != None:
                for u in g.getNodeFromIndex(v).getNeighbors(v):
                    if dist[pair[u]] == math.inf:
                        dist[pair[u]] = dist[v] + 1
                        q.append(pair[u])

        return dist[None] != math.inf

    pair = {}
    dist = {}
    q = collections.deque()

    for v in g.getNodes():
        pair[v] = None
        dist[v] = math.inf

    matching = 0

    while bfs():
        for v in g.partition1:
            if pair[v] is None and dfs(v):
                matching = matching + 1

    return (matching,pair)

    




main()