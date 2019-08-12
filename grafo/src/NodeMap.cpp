#include <grafo/NodeMap.h>

namespace Grafo
{

template<typename T>
NodeMap<T>::NodeMap(const NodeMap::graph_t& graph)
{
    std::unordered_map<key_t, T, key_t::node_hash, key_t::node_compare> m_node_map{};
}

// template<typename T>
// NodeMap<T>::NodeMap(const NodeMap::graph_t& graph, NodeMap::value_t value)
// {
//     std::unordered_map<graph_t::node_t, T, graph_t::node_t::node_hash, graph_t::node_t::node_compare> m_node_map{value};
// }
// template<typename T>
// T& NodeMap<T>::operator[] (const NodeMap::key_t& key)
// {
//     return m_node_map[key];
// }

// NodeMap::NodeMap(const NodeMap::graph_t& graph)
// {

// }











}