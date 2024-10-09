#include <Python.h>

void print_python_string(PyObject *p) {
    if (PyUnicode_Check(p)) {
        // Python string (Unicode)
        PyObject *utf8_str = PyUnicode_AsEncodedString(p, "utf-8", "ignore");
        if (utf8_str) {
            printf("[.] string object info\n");
            printf("  type: compact unicode object\n");
            printf("  length: %zd\n", PyUnicode_GET_LENGTH(p));
            printf("  value: %s\n", PyBytes_AS_STRING(utf8_str));
            Py_XDECREF(utf8_str);  // Decoding the string and decrementing reference count
        }
    } else if (PyBytes_Check(p)) {
        // Python bytes string (not Unicode)
        printf("[.] string object info\n");
        printf("  type: compact ascii\n");
        printf("  length: %zd\n", PyBytes_Size(p));
        printf("  value: %s\n", PyBytes_AsString(p));
    } else {
        // Not a valid string object
        printf("[.] string object info\n");
        printf("  [ERROR] Invalid String Object\n");
    }
}

