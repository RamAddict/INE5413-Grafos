#ifndef GRAFO_EDGE_H
#define GRAFO_EDGE_H

#include <grafo/Node.h>

namespace Grafo
{
    using id_t = int;

class Edge
{
    public:
    static id_t m_global_edge_id;
    using node_t = Node;

    using node_container_t = std::vector<Node>;
    Edge(const Edge::node_t& u, const Edge::node_t& v);

    inline bool operator==(const Edge &rhs) const
    {
        return my_id == rhs.my_id;
    }

    struct edge_hash {
        inline std::size_t operator()(const Edge& n) const
        {
            return std::hash<id_t>()(n.my_id);
        }
    };
    struct edge_compare {
        inline bool operator()(const Edge& n1, const Edge& n2) const
        {
            return n1.my_id == n2.my_id;
        }
    };

    protected:
    id_t my_id;
    node_t m_u;
    node_t m_v;
};


}

#endif /* GRAFO_EDGE_H */