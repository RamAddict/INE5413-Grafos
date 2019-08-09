# Set up minimal cmake version
cmake_minimum_required(VERSION 3.7.2)

# Set project version
set(Grafo_VERSION 0.1.0)

# Set project name
project(Grafo VERSION ${ophidian_VERSION})

# Set c++14 globally
set(CMAKE_CXX_STANDARD 17)

# Set Grafo source dir
set(Grafo_source_dir ${PROJECT_SOURCE_DIR})

#include 
include_directories(${PROJECT_SOURCE_DIR})

# add_executable(tap )

# Add subdirectories
add_subdirectory(3rdparty)
# add_subdirectory(Graph)
add_subdirectory(test)
# add_subdirectory(parser)

