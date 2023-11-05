#include <stdio.h>
#include <stdlib.h>
#include <python.h>

/**
 * print_python_list_info - prints python list info
 * @p: python object
 */

void print_python_list_info(PyObject *p)
{
	size_t m, indx = 0;
	PyObject *objkt;

	m = PyList_Size(p);
	printf("[*] Size of the Python List = %zu\n", s);
	printf("[*] Allocated = %zu\n", ((PyListObject *)p)->allocated);
	while (indx < m)
	{
		objkt = PyList_GET_ITEM(p, indx);
		printf("Element %zu: %s\n", indx, Py_TYPE(obj)->tp_name);
		indx++;
	}
}
