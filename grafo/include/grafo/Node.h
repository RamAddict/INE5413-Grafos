#ifndef GRAFO_NODE_H
#define GRAFO_NODE_H

#include <vector>

namespace Grafo
{
    using id_t = int;

class Node
{
    public:
    static id_t m_global_id;
    using node_container_t = std::vector<Node>;
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
    
    public:
    id_t my_id;
    node_container_t m_nodes{};
};


}

#endif /* GRAFO_NODE_H */