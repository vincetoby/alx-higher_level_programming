#include "object.h"

/* print_python_list_info - prints python list info
 * @p: object
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	int i, list;

	list = PyList_Size(p)
	for (i = 0 ; i < list ; i++)
		printf("[*] Size of the Python List = %d", list);
}
