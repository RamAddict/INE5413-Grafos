#include <grafo/Edge.h>

namespace Grafo
{
    Edge::Edge(const Edge::node_t& u, const Edge::node_t& v)
    {
        m_global_edge_id++;
        my_id = m_global_edge_id;
        m_u = u;
        m_v = v;
    }

    
    id_t Edge::m_global_edge_id{0};
}