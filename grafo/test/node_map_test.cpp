#include <catch2/catch.hpp>
#include <grafo/Graph.h>
#include <grafo/NodeMap.h>
#include <grafo/Node.h>

using namespace Grafo;

TEST_CASE("Creating a nodeMap", "[NodeMap] [constructor]")
{
    SECTION("Creating an empty NodeMap" , "[NodeMap] [constructor]")
    {
        // invoke parser with file
        // construct graph
        auto graph = Grafo::Graph();
        auto node = graph.addNode();
        Grafo::NodeMap<int> nodeWeight{graph, 2};
        CHECK(nodeWeight[node] == 2);
    }

}