#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info about Python lists
 * @p: A PyObject list
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, alloc, i;
    const char *type;

    if (!PyList_Check(p))
    {
        printf("[ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    alloc = ((PyListObject *)p)->allocated;
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", alloc);

    for (i = 0; i < size; i++)
    {
        type = (p->ob_type->tp_name);
        printf("Element %zd: %s\n", i, type);

        if (strcmp(type, "bytes") == 0)
            print_python_bytes(PyList_GetItem(p, i));
        else if (strcmp(type, "float") == 0)
            print_python_float(PyList_GetItem(p, i));
    }
}

/**
 * print_python_bytes - Prints basic info about Python bytes
 * @p: A PyObject bytes
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *string;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    string = PyBytes_AsString(p);
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", string);
    printf("  first %zd bytes:", size < 10 ? size + 1 : 10);

    for (i = 0; i < size + 1 && i < 10; i++)
        printf(" %02x", string[i] & 0xFF);
    printf("\n");
}

/**
 * print_python_float - Prints basic info about Python float
 * @p: A PyObject float
 */
void print_python_float(PyObject *p)
{
    double value;

    printf("[.] float object info\n");
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    value = PyFloat_AsDouble(p);
    printf("  value: %g\n", value);
}
