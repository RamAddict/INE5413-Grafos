#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <array>
#include <vector>
#include <grafo/Graph.h>

namespace Grafo
{
  void parser(Graph& g, Graph::filename_t name)
  {
      std::fstream file;
      file.open(name);


      std::string line;

      std::getline(file, line);
      // Get number of nodes
      
      int node_ammt = std::atoi(line.substr(10).c_str());
      g.m_nodes.reserve(node_ammt);

      //  Node Population
      for(int i = 0; i < node_ammt; i++)
      {
          std::getline(file, line);
          // std::cout << line << std::endl;
          std::vector<std::string> split_line;
          std::istringstream iss(line);
          std::string nodeLabel;

          for(std::string s; iss >> s; )
            split_line.push_back(s);
          
          split_line.erase(split_line.begin());
          
          for(std::string palavra : split_line)
            nodeLabel += palavra;

          g.addNode(Node(nodeLabel));
      }
      std::getline(file, line);
      //  Edge Population
      // bool directed = false;
      for (std::string line; std::getline(file, line); )
      {
          std::vector<std::string> split_line;
          std::istringstream iss(line);
          for(std::string s; iss >> s; )
            split_line.push_back(s);

          // if(stod(split_line[2]) != 1)
          //   directed = true;
          Node* u = g.getNode(atoi(split_line[0].c_str())-1);
          Node* v = g.getNode(atoi(split_line[1].c_str())-1);
          u->addNeighbour(v);
          // if(!directed)
          v->addNeighbour(u);
          auto edge = Edge(u, v);
          g.addEdge(edge);
      }
  }

}

int main(int argc, char *argv[])
{
    auto grafo = Grafo::Graph();
    Grafo::parser(grafo, argv[1]);
    std::cout << (grafo.m_nodes.at(0)).m_label;

  
  // system("ls");
  return 0;
}


