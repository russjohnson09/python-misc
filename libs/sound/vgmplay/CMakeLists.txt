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
project(${SKBUILD_PROJECT_NAME} LANGUAGES C)

find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)

file(GLOB_RECURSE SRC_FILES CONFIGURE_DEPENDS
    # "${PROJECT_SOURCE_DIR}/src/internal/*.c"
    "${PROJECT_SOURCE_DIR}/src/main.c"
)


Python_add_library(_module MODULE 
${SRC_FILES}
WITH_SOABI)

install(TARGETS _module DESTINATION ${SKBUILD_PROJECT_NAME})