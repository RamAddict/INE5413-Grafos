# Graph project

# Build as Macro project
``` bash
git clone https://github.com/RamAddict/INE5413-Grafos
cd INE5413-Grafos
mkdir build
cd build
cmake ..
make
```

## Test 
``` bash
cd build
make test
```
### Running graph_test
``` bash
cd build
cd grafo
cd test
./grafo_tests
```

# Build one project at a time
```
cd mylib
mkdir build && cd build
cmake ..
make -j
make install
```
<!-- 
```
cd mybin
mkdir build && cd build
cmake ..
make -j
make install
``` -->