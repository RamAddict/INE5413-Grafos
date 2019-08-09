###############################################################################
# Find catch2 testing framework
###############################################################################
find_package(Catch2 REQUIRED)

# Fetch test files recursevely
file(GLOB_RECURSE Graph_tests_source
    "*.cpp"
)

# Add test executable
add_executable(grafo_tests ${Graph_tests_source})

# Link test with libraries
target_link_libraries(grafo_tests grafo::grafo Catch2::Catch2)

# Add test to ctest
add_test(NAME test COMMAND grafo_tests)
