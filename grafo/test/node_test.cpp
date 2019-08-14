#include <catch2/catch.hpp>
#include <grafo/Node.h>

using namespace Grafo;



TEST_CASE("Creating nodes and cheking ID", "[Node] [constructor]")
{
    auto node = Grafo::Node();
    CHECK(node.my_id == 3);
    CHECK(node.m_nodes.empty());
    auto node2 = Grafo::Node();
    CHECK(node2.my_id == 4);
    CHECK(Grafo::Node::m_global_id == 4);
}