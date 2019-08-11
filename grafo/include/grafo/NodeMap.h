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
    using nodeMap = std::unordered_map<key_t, value_t>;
    
    NodeMap(const graph_t& graph);
    NodeMap(const graph_t& graph, value_t t);

    T& operator[] (const key_t& key);
    private:
    nodeMap m_node_map;

};

}

#endif /* GRAFO_NODE_MAP_H */