#include <grafo/Graph.h>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <array>

// std::string exec(const char* cmd) {
//     std::array<char, 128> buffer;
//     std::string result;
//     std::unique_ptr<FILE, decltype(&pclose)> pipe(popen(cmd, "r"), pclose);
//     if (!pipe) {
//         throw std::runtime_error("popen() failed!");
//     }
//     while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {
//         result += buffer.data();
//     }
//     return result;
// }

namespace Grafo
{

Graph::Graph()
{
    // // Reset node_global_counter ?
    // Node::m_global_id = 0;
}

Graph::Graph(filename_t name)
{
    
}

Graph::node_t* Graph::getNode(Graph::ammount_t index)
{
    return &m_nodes[index];
}

Graph::edge_t* Graph::getEdge(Graph::ammount_t index)
{
    return &m_edges[index];
}

Graph::ammount_t Graph::edgeAmmount() const
{
    return m_edges.size();
}

Graph::ammount_t Graph::nodeAmmount() const
{
    return m_nodes.size();
}

Graph::node_t* Graph::addNode(const node_t& source)
{
    // cria nodo e adiciona na lista de nodos 
    return &m_nodes.emplace_back(source);
    // adiciona NodeMap<string>
}

Graph::edge_t* Graph::addEdge(const edge_t& edge)
{
    return &m_edges.emplace_back(edge);
    // should also work the weights in here
}
bool Graph::edgeExists(const node_t& source, const node_t& target) const
{
    return source.isConnectedTo(target);
}

}