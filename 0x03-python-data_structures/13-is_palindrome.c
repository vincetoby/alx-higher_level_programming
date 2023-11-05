#include "lists.h"
/**
 * is_palindrome - checks if a list is pallindrome
 * @head: pointer to first node of list
 * Description: a pallindrome is when the first half and last half
 * of a string is the same.
 * Return: 0 or 1
 */

int is_palindrome(listint_t **head)
{
	const listint_t *curr;
	int length = 0, i = 0, j, buff[20000];
	
	if (*head == NULL)
		return (1);
	curr = *head;
	while (curr != NULL)
	{
		curr = curr->next;
		length++; /*get length of linkrd list*/
	}
	if (length == 1) /*if only one node in linked list*/
		return (1);
	curr = *head; /*re-initialize curr to head*/

	while (curr != NULL)/*copy content of list to buffer*/
	{
		buff[i] = curr->n;
		i++; /*increment i*/
		curr = curr->next; /*move to next node*/
	}
	j = 0;
	i--; /*decrement to be at index of the last value*/
	length--;/*decrement length as well*/
	while (i >= (length / 2)) /*this ensures it stops at half*/
	{
		if (buff[i] != buff[j])/*if its not a pallindrome*/
			return (0);
		i--;
		j++;
	}
	return (1);
}
