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
        // auto graph = Grafo::Graph();
        Grafo::Node();
        // Grafo::NodeMap<int> map(graph);
    }


    SECTION("Creating a graph from test file" , "[graph] [constructor]")
    {
        // // auto graph = Grafo::Graph("../../test/test_files/agm_tiny.net");
        // CHECK(graph.nodeAmmount() == 0);
        // CHECK(graph.edgeAmmount() == 0);
    }
}