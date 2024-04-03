// Square root calculation - C extension example
#include <Python.h>

static PyObject *
c_sqrt(PyObject *self, PyObject *args) {
    double n;

    // unbox
    if (!PyArg_ParseTuple(args, "d", &n)) {
        return NULL; // signal error
    }

    // work
    double guess = 1.0;
    double epsilon = 0.0001;

    while (fabs(guess*guess - n) > epsilon) {
        guess = ((n/guess) + guess) / 2.0;
    }

    // box
    return Py_BuildValue("d", guess);
}

static PyMethodDef SqrtMethods[] = {
    {"sqrt",  c_sqrt, METH_VARARGS, "Return square root"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef csqrtmodule = {
    PyModuleDef_HEAD_INIT,
    "csqrt",   /* name of module */
    NULL, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    SqrtMethods
};

PyMODINIT_FUNC
PyInit_csqrt(void)
{
    return PyModule_Create(&csqrtmodule);
}
