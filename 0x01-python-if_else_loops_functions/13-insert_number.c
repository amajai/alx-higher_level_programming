#include <stdio.h>
#include "lists.h"
/**
 *
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *curr;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	curr = *head;
	while(curr != NULL)
	{
		if (number < curr->n && number > curr->next->n)
		{
			
		}
		curr = curr->next;
	}
	

}

