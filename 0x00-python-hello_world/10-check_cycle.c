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
	listint_t *start_node;

	if (list == NULL || list->next == NULL)
		return (0);
	curr = list;
	start_node = list;
	while (curr != NULL)
	{
		curr = curr->next;
		if (curr == start_node)
			return (1);
	}
	return (0);
}
