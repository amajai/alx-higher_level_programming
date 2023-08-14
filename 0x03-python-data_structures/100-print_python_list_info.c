#include <stdio.h>
#include "Python.h"

/**
* print_python_list_info - prints some basic info about Python lists.
* @p: pointer to python list
*
* Return: Nothing.
*/
void print_python_list_info(PyObject *p)
{
	if (p == NULL)
		return;
	Py_ssize_t size;
	PyListObject *op;
	Py_ssize_t i;
	const char *type;

	op = (PyListObject *)p;
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", op->allocated);
	for (i = 0; i < size; i++)
	{
		type = Py_TYPE(PyList_GetItem(p, i))->tp_name;
		printf("Element %zd: %s\n", i, type);
	}
}
