#include <pybind11/pybind11.h>

std::string hello_from_bin() { return "Hello from lib-add-c!"; }

int add(int a, int b) {
    return a + b;
}

namespace py = pybind11;

PYBIND11_MODULE(_core, m) {
  m.doc() = "pybind11 hello module";

  m.def("hello_from_bin", &hello_from_bin, R"pbdoc(
      A function that returns a Hello string.
  )pbdoc");

  
  m.def("add", &add, R"pbdoc(
      A function that adds.
  )pbdoc");
}
