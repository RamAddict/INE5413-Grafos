#ifndef GRAFO_NODE_MAP_H
#define GRAFO_NODE_MAP_H

#include <grafo/Graph.h>
// #include <grafo/Node.h>
#include <unordered_map>

namespace Grafo
{

template<typename T>
class NodeMap
{
    public:
    using graph_t = Grafo::Graph;
    using key_t = graph_t::node_t;
    using value_t = T;
    using nodeMap = std::unordered_map<key_t, T, key_t::node_hash>;
    
    NodeMap(){ };
    // initializes map with given value
    NodeMap(graph_t graph, const value_t& t)
    {
        for (auto node: graph.m_nodes)
            m_node_map[node] = t;
    }
    
    // NodeMap(const graph_t& graph, value_t t);

    T& operator[] (const key_t& key)
    {
        return m_node_map[key];
    }
    
    private:
    nodeMap m_node_map{};

};

}

#endif /* GRAFO_NODE_MAP_H */