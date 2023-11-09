#include "lists.h"

/**
 * dlistint_len - prints all elements in a linked dlistint_t list
 * @h: head pointer
 * Return: length of linked list
 */

size_t print_dlistint(const dlistint_t *h)
{
	size_t len = 0;

	if (h == NULL)
		return (0);
	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		len++;
	}
	if (len == 1)
	{
		printf("-> %lu element\n", len);
	}
	else
	{
		printf("-> %lu elements\n", len);
	}
	return (len);
}
