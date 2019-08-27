#include <grafo/Node.h>
namespace Grafo
{
    Node::Node()
    {
        
    }

    Node::Node(string_t label)
    {
        // m_global_id++;
        // my_id = m_global_id;
        m_label = label;
    }

    Node::ammount_t Node::nodeDegree() const
    {
        return m_neighbours.size();
    }

    bool Node::isConnectedTo(const Node& target) const
    {
        
        // if(std::find(m_neighbours.begin(), m_neighbours.end(), target) != m_neighbours.end()) 
        //     return true;
        // else
        //     return false;
        
        // auto it = m_neighbours.find(&target); 
        // if (it != m_neighbours.end()) 
        //     return true;
        // else
            return false;
        
    }

    void Node::addNeighbour(Node::node_t* neightbour)
    {
        m_neighbours.insert(neightbour);
    }

    Node::string_t Node::nodeLabel() const
    {
        return m_label;
    }
}