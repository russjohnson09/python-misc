# https://cmake.org/cmake/help/latest/guide/tutorial/Before%20You%20Begin.html#getting-the-tutorial-exercises
# https://code.visualstudio.com/docs/cpp/cmake-quickstart

cmake_minimum_required(VERSION 3.15)
project(vgmplay VERSION 0.1.0 LANGUAGES C CXX)



file(GLOB_RECURSE SRC_FILES CONFIGURE_DEPENDS
    # "VGMPlay/*.c"
    VGMPlay/VGMPlay.c
    VGMPlay/VGMFile.c
    VGMPlay/ChipMapper.c
    VGMPlay/VGMPlay_AddFmts.c
    # "VGMPlay/vgm2wav.c"
    # VGMPlay/chips/*.c


    # "VGMPlay/chips/*.c"
    # "${PROJECT_SOURCE_DIR}/VGMPlay/chips/adlibemu_opl3.c"

    # vgmlib.c

    VGMPlay/chips/adlibemu_opl3.c
    # VGMPlay/chips/opl.c
    # VGMPlay/chips/*.c
    # "${PROJECT_SOURCE_DIR}/VGMPlay/chips/*.c"
)
 
# https://stackoverflow.com/questions/5005363/undefined-reference-to-sin

# https://stackoverflow.com/questions/17511496/how-to-create-a-shared-library-with-cmake
# libmylib.so
add_library(vgm SHARED
    # vgmlib.c
    ${SRC_FILES}
    # VGMPlay/chips/adlibemu_opl3.c
    # VGMPlay/chips/262intf.c
)

# libm (math library) and libz (zlib)
# LDFLAGS := -lm -lz $(LDFLAGS)

#  windows
#  -lm -lz -lkernel32 -lwinmm
# wsl / ubuntu
# -lm -lz -lrt -lpthread -pthread
find_library(MATH_LIBRARY m)
find_library(MATH_LIBRARY z)
target_link_libraries(vgm m)
target_link_libraries(vgm z)

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