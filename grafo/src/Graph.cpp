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

Graph::Graph(parser_t parser)
{
    // // Reset node_global_counter ? 
    // Node::m_global_id = 0;
    // populate edges and nodes
    // for
    // this->m_edges
}

Graph::Graph()
{
    // // Reset node_global_counter ?
    // Node::m_global_id = 0;
}

Graph::Graph(filename_t name)
{
    // // Reset node_global_counter ?
    // Node::m_global_id = 0;
    
    std::fstream file;
    file.open(name);
    

    std::string line;

    std::getline(file, line);
    // Get number of nodes
    auto node_ammt = std::stoi(line.substr(10));
    m_nodes.reserve(node_ammt);

    while (true)
    {
        std::getline(file, line);
        if (line == "*edges")
            break;
        std::cout << line << std::endl;
        
        // addNode();

    }

    // system("ls");
    // system("ls ..");
}

Graph::ammount_t Graph::edgeAmmount() const
{
    return m_edges.size();
}

Graph::ammount_t Graph::nodeAmmount() const
{
    return m_nodes.size();
}

Graph::node_t Graph::addNode()
{
    // cria nodo e adiciona na lista de nodos 
    auto& node = m_nodes.emplace_back();
    
    // adiciona NodeMap<string>
    
    return node;
}


}