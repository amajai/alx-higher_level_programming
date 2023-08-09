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
	listint_t *future;

	if (list == NULL || list->next == NULL)
		return (0);
	curr = list;
	future = list->next;
	while (future != NULL && future->next != NULL)
	{
		if (curr == future)
			return (1);
		curr = curr->next;
		future = future->next->next;
	}
	return (0);
}
