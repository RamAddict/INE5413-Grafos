#include <grafo/Node.h>
namespace Grafo
{
    Node::Node()
    {
        m_global_id++;
        my_id = m_global_id;
    }


}