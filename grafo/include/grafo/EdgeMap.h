#ifndef GRAFO_EDGE_MAP_H
#define GRAFO_EDGE_MAP_H

#include <grafo/Graph.h>
#include <grafo/Edge.h>
#include <unordered_map>

namespace Grafo
{

template<typename T>
class EdgeMap
{
    public:
    using graph_t = Grafo::Graph;
    using key_t = graph_t::edge_t;
    using value_t = T;
    using edgeMap = std::unordered_map<key_t, T, key_t::edge_hash>;
    
    EdgeMap() = default;
    // initializes map with given value
    EdgeMap(graph_t graph, const value_t& t)
    {
        for (auto edge: graph.m_edges)
            m_edge_map[edge] = t;
    }
    
    // NodeMap(const graph_t& graph, value_t t);

    T& operator[] (const key_t& key)
    {
        return m_edge_map[key];
    }
    T& operator[] (key_t&& key)
    {
        return m_edge_map[key];
    }
    
    private:
    edgeMap m_edge_map{};

};

}

#endif /* GRAFO_NODE_MAP_H */