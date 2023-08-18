#include "Python.h"
#include "lists.h"

/**
* print_python_list - prints some basic info about Python lists.
* @p: pointer to python list
*
* Return: Nothing.
*/
void print_python_list(PyObject *p)
{
	Py_ssize_t size;
	PyListObject *pl;
	const char *type;
	Py_ssize_t i;

	if (p == NULL)
		return;
	pl = (PyListObject *)p;
	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", pl->allocated);
	for (i = 0; i < size; i++)
	{
		type = Py_TYPE(pl->ob_item[i])->tp_name;
		printf("Element %zd: %s\n", i, type);
		if (PyBytes_Check(pl->ob_item[i]))
			print_python_bytes(pl->ob_item[i]);
	}
}

/**
* print_python_bytes - prints some basic info about Python bytes.
* @p: pointer to python list
*
* Return: Nothing.
*/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i;
	char *buf;
	Py_ssize_t length;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		PyBytes_AsStringAndSize(p, &buf, &length);
		printf("size: %zd\n", length);
		printf("trying string: %s\n", buf);
		printf("first %zd bytes:", length + 1 <= 10 ? length + 1 : 10);
		for (i = 0; i <= length && i < 10; i++)
			printf(" %02x", buf[i] & 0xff);
		printf("\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}
