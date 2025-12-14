#include <iostream>
#include <vector>
#include <string>

using namespace std;

// open msys
// cd /c/Users/russj/dev/python-misc/libs/c/hello_world
// g++ main.cpp
int main()
{
    vector<string> msg {"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!"};

    for (const string& word : msg)
    {
        cout << word << " ";
    }
    cout << endl;
}