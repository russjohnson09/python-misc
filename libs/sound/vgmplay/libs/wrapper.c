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
// https://github.com/icecube/kde/blob/9f65f3de7d228b61a27a4433e87b951de96ffec2/kde/kde.c#L107
#include <Python.h>
#include <stdint.h>

// /home/devcontainers/.cache/uv/sdists-v9/.tmpm5Z008/vgmplay-0.1.0/libs/./VGMPlay/VGMFile.h:5:9: error: unknown type name ‘UINT32’
// #include "./VGMPlay/VGMPlay.h"
// #include "./VGMPlay/VGMFile.h"
#include "./VGMPlay/vgm2wav.h"



float square(float x) { return x * x; }

// TODO change name to square
int square_int(int x) { return x * x; }

static PyObject *square_wrapper(PyObject *self, PyObject *args) {
  float input, result;
  if (!PyArg_ParseTuple(args, "f", &input)) {
    return NULL;
  }
  result = square(input);
  // https://github.com/python/cpython/blob/bef63d2fb81ae28760040157ea589541bed47d02/Include/floatobject.h#L39
  // https://docs.python.org/3.15/c-api/float.html#c.PyFloat_FromDouble
  return PyFloat_FromDouble(result);
}

// https://tenthousandmeters.com/blog/python-behind-the-scenes-8-how-python-integers-work/
// https://dev.to/artyomkaltovich/how-the-integer-type-is-implemented-in-cpython-8ei
// https://github.com/syakesaba/c-icap-python/issues/2
static PyObject *square_int_wrapper(PyObject *self, PyObject *args) {
  int input, result;
//   f (float) [float]
// Convert a Python floating-point number to a C float.

// https://docs.python.org/3/c-api/arg.html
  if (!PyArg_ParseTuple(args, "i", &input)) {
    return NULL;
  }
  result = square_int(input);
  // return PyLong_FromLong(result);
  // https://github.com/capi-workgroup/decisions/issues/32
  // return PyLong_FromInt(9);
  // return PyLong_FromInt64(9);
  // https://github.com/python/cpython/blob/bef63d2fb81ae28760040157ea589541bed47d02/Objects/longobject.c#L6775
  // return PyLong_FromInt32(9);

  // long x = 9;
  return PyLong_FromLong((long int) (result)); // https://github.com/python/cpython/blob/bef63d2fb81ae28760040157ea589541bed47d02/Objects/longobject.c#L401C1-L401C16

}

// static PyObject *square_int_wrapper(PyObject *self, PyObject *args) {
//   int input, result;
// //   f (float) [float]
// // Convert a Python floating-point number to a C float.

// // https://docs.python.org/3/c-api/arg.html
//   if (!PyArg_ParseTuple(args, "i", &input)) {
//     return NULL;
//   }
//   result = square_int(input);
//   return PyStr((long int) (result)); // https://github.com/python/cpython/blob/bef63d2fb81ae28760040157ea589541bed47d02/Objects/longobject.c#L401C1-L401C16

// }

static PyObject *echo(PyObject *self, PyObject *args) {

// https://github.com/periscope-ps/blipp/blob/002d08e911fb94c34d7f05e34883efa8f6138a4f/README.org#L132

  int input, result;
	char *filename;

//   f (float) [float]
// Convert a Python floating-point number to a C float.

// https://docs.python.org/3/c-api/arg.html
  if (!PyArg_ParseTuple(args, "s", &filename)) {
    return NULL;
  }

  // https://docs.python.org/3/c-api/bytes.html#c.PyBytes_FromString
  return PyBytes_FromString(filename);

}

static PyObject *echo2(PyObject *self, PyObject *args) {

// https://github.com/periscope-ps/blipp/blob/002d08e911fb94c34d7f05e34883efa8f6138a4f/README.org#L132

  int input, result;
	char *filename;
	char *filename2;

//   f (float) [float]
// Convert a Python floating-point number to a C float.

// https://docs.python.org/3/c-api/arg.html
  if (!PyArg_ParseTuple(args, "ss", &filename, &filename2)) {
    return NULL;
  }

  // https://docs.python.org/3/c-api/bytes.html#c.PyBytes_FromString
  return PyBytes_FromString(filename2);

}


static PyObject *vgm2wav_wrapper(PyObject *self, PyObject *args) {

// https://github.com/periscope-ps/blipp/blob/002d08e911fb94c34d7f05e34883efa8f6138a4f/README.org#L132

  int input, result;
	char *vgm_filepath;
	char *out_filepath;

//   f (float) [float]
// Convert a Python floating-point number to a C float.

// https://docs.python.org/3/c-api/arg.html
  if (!PyArg_ParseTuple(args, "ss", &vgm_filepath, &out_filepath)) {
    return NULL;
  }

  vgm2wav(vgm_filepath, out_filepath);
  // https://docs.python.org/3/c-api/bytes.html#c.PyBytes_FromString
  return PyBytes_FromString(out_filepath);
}



// PyFloat_FromString
// https://docs.python.org/3/c-api/float.html#c.PyFloat_FromString

// https://docs.python.org/3/c-api/structures.html#c.Py_T_STRING
// https://vstinner.github.io/c-api-abstract-pyobject.html
static PyMethodDef pysimple_methods[] = {
    {"square", square_wrapper, METH_VARARGS, "Square function"},
    {"square_int", square_int_wrapper, METH_VARARGS, "Square function"},
      {"echo", echo, METH_VARARGS, "echo"},
      {"echo2", echo2, METH_VARARGS, "echo"},
      {"vgm2wav", vgm2wav_wrapper, METH_VARARGS, "echo"},


    {NULL, NULL, 0, NULL}};

static struct PyModuleDef pysimple_module = {PyModuleDef_HEAD_INIT, "_module",
                                             NULL, -1, pysimple_methods};

PyMODINIT_FUNC PyInit__module(void) {
  return PyModule_Create(&pysimple_module);
}