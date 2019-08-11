#ifndef GRAFO_NODE_H
#define GRAFO_NODE_H

#include <vector>

namespace Grafo
{

class Node
{
    public:
    using node_container_t = std::vector<Node>;
    using id_t = int;
    Node();

    inline bool operator==(const Node &rhs) const
    {
        return my_id == rhs.my_id;
    }

    struct node_hash {
        inline std::size_t operator()(const Node& n) const
        {
            return std::hash<id_t>()(n.my_id);
        }
    };
    struct node_compare {
        inline bool operator()(const Node& n1, const Node& n2) const
        {
            return n1.my_id == n2.my_id;
        }
    };

    protected:
    id_t my_id;
    static id_t m_global_id;
    node_container_t m_nodes{};
};


}

#endif /* GRAFO_NODE_H */