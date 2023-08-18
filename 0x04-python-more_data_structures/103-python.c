#include "Python.h"
#include "lists.h"
#include <string.h>

/**
* print_python_list - prints some basic info about Python lists.
* @p: pointer to python list
*
* Return: Nothing.
*/
void print_python_list(PyObject *p)
{
	Py_ssize_t size, w;
	PyListObject *pl;
	PyBytesObject *pb;
	const char *type;
	Py_ssize_t i;


	if (p == NULL)
		return;
	pl = (PyListObject *)p;
	pb = (PyListObject *)p;
	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", pl->allocated);
	for (i = 0; i < size; i++)
	{
		type = Py_TYPE(pl->ob_item[i])->tp_name;
		printf("Element %zd: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
		{
			printf("[.] bytes object info\n");
			printf("size: %zd\n", pl->ob_item[i]->ob_refcnt);

		}
	}
}

/**
* print_python_bytes - prints some basic info about Python lists.
* @p: pointer to python list
*
* Return: Nothing.
*/
void print_python_bytes(PyObject *p)
{
	printf("test\n");
}