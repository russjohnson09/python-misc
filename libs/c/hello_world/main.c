// Header file for input output functions
#include <stdio.h>


// I have some much better examples using cmake and other things.
// but this is a very simple way to include some shared library



// g++ sum.c main.c -o main.o
extern int add(int a, int b);


// from a wsl environment

// sudo apt install g++

// Main function: entry point for execution

//  g++ ./main.c -o main.o
// ./main.o

// https://stackoverflow.com/questions/31541451/create-shared-library-from-cpp-files-and-static-library-with-g
// g++ -o prog main_file.o -L. -ladd

// g++  sum.c main.c -o main.o
int main() {

    // Writing print statement to print hello world
    // printf("Hello World");

    // g++ libsum.so main.c -o main.o
    // add(1,2); // main.c:(.text+0x27): undefined reference to `add(int, int)'
    printf("Hello the output is %d \n",add(10,15));


    return 0;
}