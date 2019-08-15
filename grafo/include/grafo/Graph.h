#ifndef GRAFO_GRAPH_H
#define GRAFO_GRAPH_H

#include <grafo/Node.h>
#include <grafo/Edge.h>
#include <unordered_map>
#include <vector>

namespace Grafo
{

class Graph
{
    public:
    using ammount_t = int;
    using node_t = Node;
    using edge_t = Edge;
    using bool_t = bool;
    using edge_container_t = std::vector<edge_t>;
    using node_container_t = std::vector<node_t>;
    using parser_t = /* parser class */ int;
    using filename_t = std::string;

    // required by me
    //Ideally a factory that receives the Graph object and returns it populated.
    Graph(parser_t parser);
    Graph();
    Graph(filename_t name);

    node_t addNode();
    edge_t addEdge(const node_t& source, const node_t& target);

    // required by teacher
    ammount_t nodeAmmount() const;
    ammount_t edgeAmmount() const;
    edge_t findEdge(/* ideally should receive the graph by parameter */ const node_t u, const node_t v) const;
    // there will be no neighbours function, will be done via iterator of the maps
    // not so sure about this ammount_t degree(const node_t node) const;
    // or this rotulo();
    // or this peso(s,t);
    // or this lerArquivo();


    
    public:
    // m_node_name_map
    node_container_t m_nodes{};
    edge_container_t m_edges{};
};


}

#endif /* GRAFO_GRAPH_H */