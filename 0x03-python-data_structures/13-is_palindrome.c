#include "lists.h"
/**
 * palindrome_function - check if is palindrome with recursion
 * @l: variable 1
 * @r: variable 2
 *
 * Return: 1 palindrome and 0 not palindrome
 */
int palindrome_function(listint_t **l, listint_t *r)
{
	int response;

	if (r != NULL)
	{
		response = palindrome(l, r->next);
		if (response != 0)
		{
			response = (r->n == (*l)->n);
			*l = (*l)->next;
			return (response);
		}
		return (0);

	}
	return (1);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: linked lists head
 *
 * Return: 1 palindrome and 0 not palindrome
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL)
	{
		return (0);
	}
	return (palindrome_funcion(head, *head));
}
