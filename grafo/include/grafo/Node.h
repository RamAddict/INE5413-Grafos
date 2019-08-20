#ifndef GRAFO_NODE_H
#define GRAFO_NODE_H

#include <set>
#include <string>

namespace Grafo
{
class Node
{
    public:
    struct Node_ptr_compare;
    // bool Node_ptr_compare::operator()(const Node* lhs, const Node* rhs) const;
    using string_t = std::string;
    using node_container_t = std::set<Node*, Node_ptr_compare>;
    using ammount_t = double;
    using node_t = Node;


    Node(string_t label);

    inline bool operator==(const Node &rhs) const
    {
        return m_label == rhs.m_label;
    }

    struct Node_ptr_compare
    {
        bool operator()(const Node* lhs, const Node* rhs) const
        { 
            return *lhs == *rhs;
        }
    };
    struct node_hash {
        inline std::size_t operator()(const Node& n) const
        {
            return std::hash<string_t>()(n.m_label);
        }
    };

    ammount_t nodeDegree() const;

    void addNeighbour(Node* neighbour);

    bool isConnectedTo(const Node& target) const;
    
    string_t nodeLabel() const;
    
    public:
    string_t m_label;
    node_container_t m_neighbours{};

};


}

#endif /* GRAFO_NODE_H */