

// g++ sum.c -o sum.o
// /usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/13/../../../x86_64-linux-gnu/Scrt1.o: in function `_start':
// (.text+0x1b): undefined reference to `main'
// collect2: error: ld returned 1 exit status

// This is a shared library so use that argument to avoid the main ref error


// g++ -shared -o libsum.so sum.c
// g++ libsum.so main.c -o main.o

// https://stackoverflow.com/questions/31541451/create-shared-library-from-cpp-files-and-static-library-with-g

// g++ -shared sum.c -o sum.so

// https://stackoverflow.com/questions/67099759/ctypes-function-not-found

//https://realpython.com/python-bindings-overview/#c-or-c-source


// https://stackoverflow.com/questions/1041866/what-is-the-effect-of-extern-c-in-c
// Don't mangle my names

//  g++ -shared -o libsum.so sum.cpp
// 
extern "C" int add(int, int);

int add(int a, int b) {
    return a + b;
}