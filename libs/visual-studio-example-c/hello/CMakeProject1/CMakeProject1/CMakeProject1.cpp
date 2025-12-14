// CMakeProject1.cpp : Defines the entry point for the application.
//

#include "CMakeProject1.h"

using namespace std;

// devcontainers@beam:/mnt/c/Users/russj/dev/python-misc/libs/visual-studio-example-c/hello/CMakeProject1/out/build/x64-debug/CMakeProject1$ ./CMakeProject1.exe 
// Hello CMake.

// It seems odd that I can run this on wsl?
//   command = "C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\CommonExtensions\Microsoft\CMake\CMake\bin\cmake.exe" -E cmake_ninja_dyndep --tdi=CMakeProject1\CMakeFiles\CMakeProject1.dir\CXXDependInfo.json --lang=CXX --modmapfmt=msvc --dd=$out @$out.rsp


int main()
{
	cout << "Hello CMake." << endl;
	return 0;
}
