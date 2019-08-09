#include <grafo/Graph.h>
namespace Grafo
{

Graph::Graph(parser_t parser)
{
    // populate edges and nodes
    // for
    // this->m_edges
}

Graph::ammount_t Graph::edgeAmmount() const
{
    return m_edges.size();
}

Graph::ammount_t Graph::nodeAmmount() const
{
    return m_nodes.size();
}

}