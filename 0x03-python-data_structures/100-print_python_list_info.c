#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: Pointer to a Python object representing a list.
 *
 * Description: This function prints the size of the list, the
 * allocated memory, and the type of each element in the list.
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, allocated, i;
    PyObject *item;

    /* Check if the input object is a list */
    if (!PyList_Check(p))
    {
        fprintf(stderr, "Passed object is not a list\n");
        return;
    }

    /* Get the size and allocated memory of the list */
    size = PyList_Size(p);
    allocated = ((PyListObject *)p)->allocated;

    /* Print the size and allocated memory */
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    /* Print information about each element in the list */
    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
