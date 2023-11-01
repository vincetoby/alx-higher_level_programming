#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts node in sorted list
 * @head: address of head pointer
 * @number: number to insert
 * Return: inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *temp;

	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return (NULL);

	temp->n = number;
	temp->next = NULL;

	if (!node || temp->n < node->n)
	{
		temp->next = node;
		return (*head = temp);
	}

	while (node)
	{
		if (!node->next || temp->n < node->next->n)
		{
			temp->next = node->next;
			node-> next = new;
			return (node);
		}
		node = node->next;
	}
	return (NULL);
}
