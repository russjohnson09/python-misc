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

# https://stackoverflow.com/questions/79292616/undefined-reference-when-building-with-f2py-and-scikit-build-core
# https://github.com/ofloveandhate/scikit-build_boost-python
find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)
# find_package(Python COMPONENTS Interpreter Development.Module NumPy REQUIRED)
# find_package(Python REQUIRED COMPONENTS Interpreter Development.Module NumPy)

# https://cmake.org/cmake/help/latest/command/file.html
# file(GLOB_RECURSE SRC_FILES CONFIGURE_DEPENDS
file(GLOB SRC_FILES CONFIGURE_DEPENDS
    # "${PROJECT_SOURCE_DIR}/src/vgmplay/VGMPlay/chips/*.c"

    "${PROJECT_SOURCE_DIR}/libs/VGMPlay/VGMPlay.c"
    "${PROJECT_SOURCE_DIR}/libs/VGMPlay/*.c"
    # "${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/*.c"

    ${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/adlibemu_opl2.c
    ${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/adlibemu_opl3.c



 ${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/sn76489.c 
 ${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/262intf.c 
 ${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/2151intf.c 
 ${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/2610intf.c 
 ${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/2203intf.c 
 ${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/2413intf.c 
 ${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/2608intf.c 
 ${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/2612intf.c 
 ${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/3526intf.c 
 ${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/3812intf.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/8950intf.c


${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/adlibemu_opl2.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/adlibemu_opl3.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/ay8910.c


${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/ay_intf.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/c140.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/c352.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/c6280.c


${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/c6280intf.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/dac_control.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/es5503.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/es5506.c


${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/emu2149.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/emu2413.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/fm2612.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/fm.c


${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/fmopl.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/gb.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/iremga20.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/k051649.c


${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/k053260.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/k054539.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/multipcm.c


${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/nes_apu.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/nes_intf.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/np_nes_apu.c


${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/np_nes_dmc.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/np_nes_fds.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/okim6258.c


${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/okim6295.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/Ootake_PSG.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/opll.c


${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/opm.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/panning.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/pokey.c


${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/pwm.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/qsound_ctr.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/qsound_mame.c


${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/qsound_intf.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/rf5c68.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/saa1099.c


${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/segapcm.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/scd_pcm.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/scsp.c


${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/scspdsp.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/sn76496.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/sn764intf.c


${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/upd7759.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/vsu.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/ws_audio.c


${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/x1_010.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/ym2151.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/ym2413.c


${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/ym2612.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/ym3438.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/ymdeltat.c


${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/ymf262.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/ymf271.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/ymf278b.c


${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/ymz280b.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/ay8910_opl.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/sn76496_opl.c


${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/ym2413hd.c
${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/ym2413_opl.c
)

# file(GLOB_RECURSE REMOVE_FILES CONFIGURE_DEPENDS
#     # "${PROJECT_SOURCE_DIR}/src/vgmplay/VGMPlay/chips/*.c"

#     "${PROJECT_SOURCE_DIR}/libs/VGMPlay/VGMPlay.c"
#     "${PROJECT_SOURCE_DIR}/libs/VGMPlay/*.c"
#     # "${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/*.c"

#     ${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/adlibemu_opl2.c
#     ${PROJECT_SOURCE_DIR}/libs/VGMPlay/chips/adlibemu_opl3.c


# )
include(CMakePrintHelpers)

# if (WIN32)
#     message(WINDOWS)
#     message(WINDOWS)
#     message(WINDOWS)
#     message(WINDOWS)
#     message(WINDOWS)

#     set(WIN32 TRUE)
# endif (WIN32)

if(LINUX) 
    message(STATUS ">>> Linux")
    message(STATUS ">>> Linux")
    message(STATUS ">>> Linux")
    message(STATUS ">>> Linux")
    # linux stuff here

    # find_package(z REQUIRED)

        # CMake to find a package configuration file provided by "z", but CMake did
else()
# https://stackoverflow.com/questions/9160335/os-specific-instructions-in-cmake-how-to
    message(STATUS ">>> Not Linux")
    message(STATUS ">>> Not Linux")
    message(STATUS ">>> Not Linux")
    message(STATUS ">>> Not Linux")
    message(STATUS ">>> Not Linux")
    message(STATUS ">>> Not Linux")
    # stuff that should happen not on Linux 
    # set(WIN32 TRUE)

    # https://stackoverflow.com/questions/46398035/in-cmake-how-do-you-change-default-compiler-flags-for-a-build-type-on-a-per-use
    # SET (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} $ENV{MY_CXXFLAGS}")
    # https://cmake.org/cmake/help/latest/variable/CMAKE_LANG_FLAGS.html

    #       cl : command line  warning D9002: ignoring unknown option '-lwinmm' [C:\Users\russj\dev\python-misc\libs\sound\vgmplay\build\cp313-cp313-win_amd64\vgm.vcxproj]
    # SET (CMAKE_C_FLAGS "-DWIN32 -lkernel32 -lwinmm")

    #       C:\Users\russj\dev\python-misc\libs\sound\vgmplay\libs\VGMPlay\VGMPlay.c(85,10): error C1083: Cannot open include file: 'zlib.h': No such file or directory
    # https://stackoverflow.com/questions/29505121/cmake-zlib-build-on-windows
    
    
    # SET (CMAKE_C_FLAGS "-DWIN32")

    # LDFLAGS += -lkernel32 -lwinmm

    # https://stackoverflow.com/questions/49289364/how-do-i-use-zlib-within-windows-using-cmake-and-mingw
    #         Could NOT find ZLIB (missing: ZLIB_LIBRARY ZLIB_INCLUDE_DIR)
    # find_package(ZLIB REQUIRED)

    # set(ZLIB_INCLUDE_DIR "C:/MinGW/bin")
    # https://packages.msys2.org/packages/zlib?variant=x86_64
    # pacman -S zlib

    #  /c/Users/russj/.local/bin/uv run pytest -s

    # find_package(z REQUIRED)

    # find_package(z REQUIRED) # ubuntu wasn't able to find this either

    # find_package(ZLIB REQUIRED)


endif()

# list(REMOVE_ITEM SRC_FILES REMOVE_FILES)
# message(SRC_FILES="${SRC_FILES}")
# cmake_print_variables(SRC_FILES)

# OUTPUT=""
message(OUTPUT="${CMAKE_RUNTIME_OUTPUT_DIRECTORY}")

# OUTPUT2="/home/devcontainers/.cache/uv/sdists-v9/.tmpmhYmzD/vgmplay-0.1.0/build/cp313-cp313-linux_x86_64"
message(OUTPUT2="${CMAKE_BINARY_DIR}")

add_library(vgm SHARED
    # vgmlib.c
    ${SRC_FILES}
    # VGMPlay/chips/adlibemu_opl3.c
    # VGMPlay/chips/262intf.c
)
# target_link_libraries(vgm m)
# target_link_libraries(vgm z)


# vgm2wav.c:(.text.startup+0x18): undefined reference to `VGMPlay_Init'
# add_executable(
#     vgm4444wav ${PROJECT_SOURCE_DIR}/libs/VGMPlay/vgm2wav.c
# )
# vgm2wav.c:(.text.startup+0x18): undefined reference to `VGMPlay_Init'
# target_link_libraries( vgm4444wav PRIVATE vgm )



Python_add_library(_module MODULE 
    ${SRC_FILES}
    "${PROJECT_SOURCE_DIR}/libs/wrapper.c"
WITH_SOABI)

target_link_libraries(_module PRIVATE vgm)

# math
target_link_libraries(_module PRIVATE m)

# zlib
# https://scikit-build-core.readthedocs.io/en/latest/guide/cmakelists.html#finding-other-packages
# https://scikit-build-core.readthedocs.io/en/latest/about/projects.html
target_link_libraries(_module PRIVATE z)

install(TARGETS _module DESTINATION ${SKBUILD_PROJECT_NAME})

