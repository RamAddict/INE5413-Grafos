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
        auto name_1 = Node("Nodo1");
        auto node1 = graph.addNode(name_1);
        auto name_2 = Node("Nodo2");
        auto node2 = graph.addNode(name_2);
        // auto edge = graph.addEdge(node1, node2);
        
        Grafo::EdgeMap<int> edgeWeight{graph, 3};
        // edgeWeight[*edge] = 3;
    }

}