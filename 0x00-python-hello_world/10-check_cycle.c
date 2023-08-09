#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to head of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *curr;
	int *start_add;

	if (list == NULL || list->next == NULL)
		return (0);
	curr = list;
	start_add = &list->n;
	while (curr != NULL)
	{
		curr = curr->next;
		if (&curr->n == start_add)
			return (1);
	}
	return (0);
}
