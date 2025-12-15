cmake_minimum_required(VERSION 3.15)

# https://github.com/scikit-build/scikit-build-core/blob/main/tests/packages/simplest_c/CMakeLists.txt

# cpp
# project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX)

# set(PYBIND11_FINDPYTHON ON)
# find_package(pybind11 CONFIG REQUIRED)

# pybind11_add_module(_core MODULE src/main.cpp)
# install(TARGETS _core DESTINATION ${SKBUILD_PROJECT_NAME})



#c
# https://github.com/scikit-build/scikit-build-core
# C:\Users\russj\AppData\Local\uv\cache\sdists-v9\.tmp4e015A\vgmplay-0.1.0\src\vgmplay\VGMPlay\chips\262intf.h(38,61): error C2059: syntax error: ')' [C:\Users\russj\AppData\Local\uv\cache\sdists-v9\.tmp4e015A\vgmplay-0.1.0\build\cp313-cp313-win_amd64\_module.vcxproj]
#   (compiling source file '../../src/main.c')

project(${SKBUILD_PROJECT_NAME} LANGUAGES C)

find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)

file(GLOB_RECURSE SRC_FILES CONFIGURE_DEPENDS
    # "${PROJECT_SOURCE_DIR}/src/vgmplay/VGMPlay/*.c"
    # "${PROJECT_SOURCE_DIR}/src/vgmplay/VGMPlay/chips/*.c"
    "${PROJECT_SOURCE_DIR}/src/main.c"
)


Python_add_library(_module MODULE 
${SRC_FILES}
WITH_SOABI)

install(TARGETS _module DESTINATION ${SKBUILD_PROJECT_NAME})