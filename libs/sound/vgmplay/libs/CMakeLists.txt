# https://cmake.org/cmake/help/latest/guide/tutorial/Before%20You%20Begin.html#getting-the-tutorial-exercises
# https://code.visualstudio.com/docs/cpp/cmake-quickstart

cmake_minimum_required(VERSION 3.15)
project(vgmplay VERSION 0.1.0 LANGUAGES C CXX)


# make WINDOWS=1 && ./vgm2wav.exe ../nakama.vgm ../../../../assets/shining_force_nakama.wav
add_executable(
    vgm2wav main.c
)


# install(TARGETS _module DESTINATION ${SKBUILD_PROJECT_NAME})

# camke .