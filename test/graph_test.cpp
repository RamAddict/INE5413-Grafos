#include <3rdparty/catch.hpp>
#include <Graph/Graph.h>

using namespace Grafo;

TEST_CASE("Creating an empty graph", "[graph] [constructor]")
{
    // invoke parser with file
    // construct graph
    auto graph = Grafo::Graph(1);
    
    CHECK(graph.nodeAmmount() == 0);
    CHECK(graph.edgeAmmount() == 0);

}