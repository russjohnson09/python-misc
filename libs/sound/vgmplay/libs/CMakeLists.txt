# https://cmake.org/cmake/help/latest/guide/tutorial/Before%20You%20Begin.html#getting-the-tutorial-exercises
# https://code.visualstudio.com/docs/cpp/cmake-quickstart

cmake_minimum_required(VERSION 3.15)
project(vgmplay VERSION 0.1.0 LANGUAGES C CXX)



# https://stackoverflow.com/questions/17511496/how-to-create-a-shared-library-with-cmake
# libmylib.so
add_library(vgm SHARED
    vgmlib.c
)

# https://discourse.cmake.org/t/creating-shared-libraries-and-an-executable/2846

# make WINDOWS=1 && ./vgm2wav.exe ../nakama.vgm ../../../../assets/shining_force_nakama.wav
# add_executable(
#     vgm2wav vgmlib.c main.c
# )
add_executable(
    vgm2wav main.c
)
# add_dependencies( vgm2wav vgm  )
target_link_libraries( vgm2wav PRIVATE vgm )




# install(TARGETS _module DESTINATION ${SKBUILD_PROJECT_NAME})

# camke .