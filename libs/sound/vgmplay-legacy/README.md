
 obj/VGMPlayUI.o: in function `wprintc':
VGMPlayUI.c:(.text+0x2c5): undefined reference to `__vswprintf_chk'



russj@beam UCRT64 /c/Users/russj/dev/python-misc/libs/sound/vgmplay-legacy/VGMPlay
$ make WINDOWS=1



https://code.visualstudio.com/docs/cpp/config-mingw



pacman -S --needed base-devel mingw-w64-ucrt-x86_64-toolchain
C:\msys64\ucrt64\bin
pacman -S make
C:\msys64\usr\bin

https://www.msys2.org/

https://github.com/vgmrips/vgmplay-legacy

Add the path of your MinGW-w64 bin folder to the Windows PATH environment variable by using the following steps:




gcc --version
g++ --version
gdb --version


make WINDOWS=1


Package 'dbus-1' not found

WINDOWS=1 make 





https://github.com/msys2/msys2-installer/releases/tag/nightly-x86_64

https://github.com/msys2/msys2-installer/releases/download/nightly-x86_64/msys2-x86_64-latest.exe

C:\msys64

'C:\WINDOWS\system32\drivers\etc\hosts' -> '/etc/hosts'

# VGMPlay [![Build Status](https://travis-ci.org/vgmrips/vgmplay.svg?branch=master)](https://travis-ci.org/vgmrips/vgmplay)

The official and always up-to-date player for all [VGM](https://en.wikipedia.org/wiki/VGM_(file_format)) files.

In the future, the existing VGMPlay will be replaced by [libvgm](https://github.com/ValleyBell/libvgm), which is currently in development.

## Contact

* [VGMRips Forums](http://vgmrips.net/forum/index.php)
* IRC: irc.digibase.ca #vgmrips

## Compile VGMPlay under Windows

### Using MS Visual Studio 6.0:

1. Open `VGMPlay.dsw`.
2. Build the project.
3. Done.

### Using later versions of MS Visual Studio:
https://www.reddit.com/r/vscode/comments/socvt7/what_is_msys2_and_why_do_i_need_it_to_code_in_c/

The build tools for Visual Studio 2010 (Platform Toolset = 'v100') cannot be found. To build using the v100 build tools, please install Visual Studio 2010 build tools.  Alternatively, you may upgrade to the current Visual Studio tools by selecting the Project menu or right-click the solution, and then selecting "Retarget solution".


https://github.com/microsoft/vcpkg?tab=readme-ov-file#use-vcpkg

cannot open file 'zlib64.lib'

cannot open file 'zlibstat64d.lib'
      <AdditionalDependencies>kernel32.lib;user32.lib;advapi32.lib;winmm.lib;zlibstat64d.lib;%(AdditionalDependencies)</AdditionalDependencies>


.\vcpkg install zlib:x64-windows-static

$env:VCPKG_VISUAL_STUDIO_PATH = "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools"

C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools

C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\vcpkg
https://learn.microsoft.com/en-us/vcpkg/troubleshoot/build-failures?WT.mc_id=vcpkg_inproduct_cli

      vcpkg install zlib

Project properties -> linker -> input -> Additional Dependencies

I removed zlib

unresolved external symbol gzread

1

Make sure vcpkg is installed in Visual Studio Installer. Use command vcpkg install zlib.

Install In classic mode, run the following vcpkg command:
vcpkg install zlib
vcpkg
https://www.youtube.com/watch?v=ulftqyA3A8o

1>C:\Users\russj\dev\python-misc\libs\sound\vgmplay-legacy\VGMPlay\zlib\zlib.lib : warning LNK4272: library machine type 'x86' conflicts with target machine type 'x64'
1>C:\Users\russj\dev\python-misc\libs\sound\vgmplay-legacy\VGMPlay\Debug_Win64\VGMPlay.exe : fatal error LNK1120: 7 unresolved externals


1. Open `VGMPlay.vcxproj`.
2. Build the project.
3. Done.

### Using MinGW/MSYS:

1. open MSYS and run `make WINDOWS=1` in VGMPlay's folder.
2. Done.

Note: You can compile it without MSYS, but you need to manually create
the OBJDIRS paths (or make them use the backslash '\'), because mkdir fails
at paths with a forward slash.

## Compile VGMPlay under Linux

1. [optional step] If you have libao installed, you can edit the 
Makefile to make VGMPlay use `libao` instead of `OSS`.
2. run `make` in VGMPlay's folder
3. Done. Optionally `sudo make install` and `sudo make play_install`.

### Building on Ubuntu (16.04)

#### Requirements

The following packages are needed in order to compile the binaries

```sh
sudo apt-get install make gcc zlib1g-dev libao-dev libdbus-1-dev
```

#### Building
```sh
cd VGMPlay
make
```

./VGMPlay/vgmplay nakama.vgm


It doesn't seem to like wsl

Track Title:    Jingle - Nakama [Comrades Jingle 1 (Happily)]
Game Name:      Shining Force
System:         Sega Mega Drive / Genesis
Composer:       Masahiko Yoshimura
Release:        1992
Version:        1.50      Gain: 1.00    Loop: No
VGM by:         Duchemole & Danjuro
Notes:

Used chips:     SEGA PSG, YM2612  

Error openning Sound Device!

## Compile VGMPlay under macOS

1. install libao by executing the line `brew install libao`
2. run `make install MACOSX=1 DISABLE_HWOPL_SUPPORT=1` in VGMPlay's folder 
(Alternatively edit the Makefile to set those constants and just run `make`.)
3. Done.

Thanks to grauw for macOS compilation instructions.

## Compile VGMPlay under Android
1. Install [Termux](https://github.com/termux/termux-app) on [F-Droid](https://f-droid.org/en/packages/com.termux/) or [GitHub](https://github.com/termux/termux-app/releases). Do not download Termux from Play Store for security and depreciation reasons
2. Open Termux and do `pkg update`
3. When you do pkg update, do `pkg install clang dbus git libao make pkg-config -y`
4. After the installation is done, do `git clone https://github.com/vgmrips/vgmplay`
5. After Done Cloning, do `cd vgmplay/VGMPlay`
6. And then do `make`
