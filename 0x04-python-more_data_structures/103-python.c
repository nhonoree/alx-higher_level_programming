#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints basic information about Python bytes objects
 * @p: A PyObject pointer to a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
    char *string;
    Py_ssize_t size, i;

    printf("[.] bytes object info\n");
    
    // Check if p is a valid bytes object
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    // Get size and string content
    size = PyBytes_Size(p);
    string = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);

    // Print the first 10 bytes in hex
    printf("  first %ld bytes:", size < 10 ? size + 1 : 10);
    for (i = 0; i < size + 1 && i < 10; i++) {
        printf(" %02x", (unsigned char)string[i]);
    }
    printf("\n");
}

/**
 * print_python_list - Prints basic information about Python lists
 * @p: A PyObject pointer to a Python list
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");

    // Check if p is a valid list object
    if (!PyList_Check(p)) {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    // Get size and allocated memory
    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    // Iterate over the elements
    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, item->ob_type->tp_name);
        if (PyBytes_Check(item))
            print_python_bytes(item);
    }
}
