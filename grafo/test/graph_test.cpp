#include <catch2/catch.hpp>
#include <grafo/Graph.h>

using namespace Grafo;

TEST_CASE("Creating an empty graph", "[graph] [constructor]")
{
    SECTION("Creating an empty graph" , "[graph] [constructor]")
    {
        // invoke parser with file
        // construct graph
        auto graph = Grafo::Graph();

        CHECK(graph.nodeAmmount() == 0);
        CHECK(graph.edgeAmmount() == 0);

        graph.addNode();
        CHECK(graph.nodeAmmount() == 1);
        
    }


    SECTION("Creating a graph from test file" , "[graph] [constructor]")
    {
        auto graph = Grafo::Graph("../../test/test_files/agm_tiny.net");
        CHECK(graph.nodeAmmount() == 0);
        CHECK(graph.edgeAmmount() == 0);
    }
}