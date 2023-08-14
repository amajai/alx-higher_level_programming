#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *curr;
	int num_list[64];
	int r = 0, l = 0;

	if (*head == NULL)
		return (1);
	curr = *head;
	while (curr != NULL)
	{
		num_list[r] = curr->n;
		r++;
		curr = curr->next;
	}
	r--;
	while (l <= r)
	{
		if (num_list[l] != num_list[r])
			return (0);
		l++;
		r--;
	}
	return (1);
}
