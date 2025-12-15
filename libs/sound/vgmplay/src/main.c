// #include <pybind11/pybind11.h>

// std::string hello_from_bin() { return "Hello from vgmplay!"; }

// namespace py = pybind11;

// PYBIND11_MODULE(_core, m) {
//   m.doc() = "pybind11 hello module";

//   m.def("hello_from_bin", &hello_from_bin, R"pbdoc(
//       A function that returns a Hello string.
//   )pbdoc");
// }


#define PY_SSIZE_T_CLEAN
#include <Python.h>

//libs\sound\vgmplay\src\vgmplay\VGMPlay\chips\262intf.c
// C:\Users\russj\AppData\Local\uv\cache\sdists-v9\.tmpua0Gfk\vgmplay-0.1.0\src\main.c(20,10): 
// error C1083: Cannot open include file: 'VGMPlay/chips/262intf.h': No such file or directory [C:\Users\russj\AppData\Local\uv\cache\sdists-v9\.tmpua0Gfk\vgmplay-0.1.0\build\cp313-cp313-win_amd64\_module.vcxproj]

// #include "vgmplay/VGMPlay/chips/262intf.h"  
// #include "vgmplay/VGMPlay/chips/262intf.h"  
// #include "vgmplay/VGMPlay/vgm2wav.c"

// C:\Users\russj\AppData\Local\uv\cache\sdists-v9\.tmpdRmhRr\vgmplay-0.1.0\src\vgmplay\VGMPlay\chips\opl.h(45,17): error C2061: syntax error: identifier 'Bitu' [C:\Users\russj\AppData\Local\uv\cache\sdists-v9\.tmpdRmhRr\vgmplay-0.1.0\build\cp313-cp313-win_amd64\_module.vcxproj]

// libs\sound\vgmplay-legacy\VGMPlay\chips\opl.h
// This parts failing and I'm not sure why

      // error: unknown type name ‘UINT32’
      //    31 | typedef UINT32          Bitu;
//  git clean -dxf -- .
// uv run pytest -s
// wsl only is having this issue of this not being defined.
// typedef UINT32		Bitu; // rm .venv is necessary
typedef uint32_t	Bit32u;


float square(float x) { return x * x; }

static PyObject *square_wrapper(PyObject *self, PyObject *args) {
  float input, result;
  if (!PyArg_ParseTuple(args, "f", &input)) {
    return NULL;
  }
  result = square(input);
  return PyFloat_FromDouble(result);
}

static PyMethodDef pysimple_methods[] = {
    {"square", square_wrapper, METH_VARARGS, "Square function"},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef pysimple_module = {PyModuleDef_HEAD_INIT, "_module",
                                             NULL, -1, pysimple_methods};

PyMODINIT_FUNC PyInit__module(void) {
  return PyModule_Create(&pysimple_module);
}