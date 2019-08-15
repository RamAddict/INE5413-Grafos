#include <catch2/catch.hpp>
#include <grafo/Graph.h>
#include <grafo/EdgeMap.h>


using namespace Grafo;

TEST_CASE("Creating a edgeMap", "[edgeMap] [constructor]")
{
    SECTION("Creating an empty edgeMap" , "[edgeMap] [constructor]")
    {
        // invoke parser with file
        // construct graph
        auto graph = Grafo::Graph();
        auto node1 = graph.addNode();
        auto node2 = graph.addNode();
        auto edge = graph.addEdge(node1, node2);
        
        Grafo::EdgeMap<int> edgeWeight{graph, 3};
        edgeWeight[edge] = 3;
    }

}