cmake_minimum_required(VERSION 3.15)


# https://github.com/scikit-build/scikit-build-core
project(${SKBUILD_PROJECT_NAME} LANGUAGES C)


# FILE(GLOB MyCSources *.c)
# ADD_EXECUTABLE(MyExecutable ${MyCSources})
# https://stackoverflow.com/questions/3201154/automatically-add-all-files-in-a-folder-to-a-target-using-cmake

# file(GLOB_RECURSE ASTERI_SRC_FILES CONFIGURE_DEPENDS
#     "${PROJECT_SOURCE_DIR}/Application/*.cpp"
#     "${PROJECT_SOURCE_DIR}/Graphics/*.cpp"
# )


find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)

# add_executable(${SKBUILD_PROJECT_NAME} src/internal/tokenizer)
# target_link_libraries(main ${PROJECT_SOURCE_DIR}/src/internal/*.c)

# https://stackoverflow.com/questions/28597351/how-do-i-add-a-library-path-in-cmake
# link_directories(${CMAKE_SOURCE_DIR}/src/internal)

# main.obj : error LNK2019: unresolved external symbol next_pgn referenced in function PyPGNFile_read_next_game [C:\Users\russj\AppData\Local\uv\cache\sdists-v9\.tmpKEeeEJ\lib_bulletchess-0.1.0\build\cp313-cp313-win_amd64\_module.vcxproj]

# Python_add_library(_module MODULE src/main.c src/internal/pgn.c WITH_SOABI)


# https://stackoverflow.com/questions/27992346/how-to-use-cmake-glob-recurse-for-only-some-subdirectories
file(GLOB_RECURSE SRC_FILES CONFIGURE_DEPENDS
    "${PROJECT_SOURCE_DIR}/src/internal/*.c"
    "${PROJECT_SOURCE_DIR}/src/main.cc"
)

Python_add_library(_module MODULE 
${SRC_FILES}
# src/internal/pgn.c
# src/internal/rules.c
# src/internal/fen.c # depends on board.c
# src/internal/board.c

# src/main.c 
WITH_SOABI)

# Python_add_library(_module MODULE src/main.c WITH_SOABI)

# https://github.com/ofloveandhate/scikit-build_boost-python/blob/main/core/CMakeLists.txt

# https://github.com/GalSim-developers/GalSim
install(TARGETS _module DESTINATION ${SKBUILD_PROJECT_NAME})


# project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX) # cpp
# set(PYBIND11_FINDPYTHON ON)
# find_package(pybind11 CONFIG REQUIRED)

# pybind11_add_module(_core MODULE src/main.c)
# install(TARGETS _core DESTINATION ${SKBUILD_PROJECT_NAME})