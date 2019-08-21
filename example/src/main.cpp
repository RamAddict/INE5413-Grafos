#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <array>
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
      auto node_ammt = std::stoi(line.substr(10));
      g.m_nodes.reserve(node_ammt);

      //  Node Population
      for(int i = 0; i < node_ammt; i++)
      {
          std::getline(file, line);
          // std::cout << line << std::endl;
          std::vector<std::string> split_line;
          std::istringstream iss(line);

          for(std::string s; iss >> s; )
            split_line.push_back(s);

          g.addNode(Node(split_line[1]));
      }

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
          Node* u = g.getNode(stoi(split_line[0])-1);
          Node* v = g.getNode(stoi(split_line[1])-1);
          u->addNeighbour(v);
          // if(!directed)
          v->addNeighbour(u);
          g.addEdge(u,v);
      }

      // system("ls");
      // system("ls ..");
  }

}

int main(int argc, char *argv[])
{
  auto grafo = Grafo::Graph();
  parser(grafo, argv[1]);
  return 0;
}


