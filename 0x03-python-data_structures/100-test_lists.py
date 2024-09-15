import ctypes

# Load the shared library
lib = ctypes.CDLL('./libPyList.so')

# Define the argument type for the function
lib.print_python_list_info.argtypes = [ctypes.py_object]

# Test with various list operations
l = ['hello', 'World']
lib.print_python_list_info(l)

del l[1]
lib.print_python_list_info(l)

l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], "My string"]
lib.print_python_list_info(l)

l = []
lib.print_python_list_info(l)

l.append(0)
lib.print_python_list_info(l)

l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list_info(l)

l.pop()
lib.print_python_list_info(l)
