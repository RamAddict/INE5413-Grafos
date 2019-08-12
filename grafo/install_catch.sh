#!/bin/bash

sudo apt-get install build-essential

DEPENDENCIES='3rdparty'

rm -rf $DEPENDENCIES && mkdir $DEPENDENCIES

git clone https://github.com/catchorg/Catch2.git 
cd Catch2

cmake -DCMAKE_INSTALL_PREFIX=../$DEPENDENCIES -Bbuild -H. -DBUILD_TESTING=OFF
cmake --build build/ --target install
cd ..
rm -rf Catch2