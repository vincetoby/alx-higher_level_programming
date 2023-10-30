#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @s_list: The singly-linked list to check
 * Return: 0 if no cycle, 1 otherwise.
 */

int check_cycle(listint_t *s_list)
{
	listint_t *mv1, *mv2;

	if (s_list == NULL || s_list->next == NULL)
		return (0);

	mv1 = s_list->next;
	mv2 = s_list->next->next;

	while (mv1 && mv2 && mv2->next)
	{
		if (mv1 == mv2)
			return (1);

		mv1 = mv1->next;
		mv2 = mv2->next->next;
	}
	return (0);
}
