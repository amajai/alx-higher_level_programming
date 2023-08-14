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
	listint_t *slow, *fast, *prev = NULL, *tmp, *l, *r;

	if (*head == NULL)
		return (1);
	slow = *head;
	fast = *head;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	while (slow != NULL)
	{
		tmp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = tmp;
	}
	l = *head;
	r = prev;
	while (r != NULL)
	{
		if (l->n != r->n)
			return (0);
		r = r->next;
		l = l->next;
	}
	return (1);
}
