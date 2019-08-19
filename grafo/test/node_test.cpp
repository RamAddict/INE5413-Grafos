#include <catch2/catch.hpp>
#include <grafo/Node.h>

using namespace Grafo;



TEST_CASE("Creating nodes and cheking ID", "[Node] [constructor]")
{
    auto node = Grafo::Node("cat");
    CHECK(node.m_label == "cat");
    CHECK(node.m_neighbours.empty());
    auto node2 = Grafo::Node("koshka");
    CHECK(node2.m_label == "koshka");
    CHECK(node2.m_neighbours.empty());
}