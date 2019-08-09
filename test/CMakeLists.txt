# Fetch test files recursevely
file(GLOB_RECURSE Graph_tests_source
    "*.cpp"
    "main.cpp"
)

# Add test target
add_executable(Graph_tests ${Grafo_source_dir})

# target_link_libraries(Graph_tests
#     PRIVATE Catch
# )

# if(OPHIDIAN_TESTS_FULLY_STATIC)
#     # Link EVERYTHING staticly!
#     set_target_properties(ophidian_tests PROPERTIES
#         LINK_FLAGS "-static -static-libgcc -static-libstdc++ -pthread"
#     )
# endif()


################################################################################
# Add test to ctest
################################################################################

enable_testing()
add_test(NAME unit_test COMMAND Graph_tests)
