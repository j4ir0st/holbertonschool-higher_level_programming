#include "lists.h"

/**
 * insert_node - adds a new node into a sorted linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = *head, *new, *tmp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL)
		return (NULL)
	while (curr->next->n < number)
	{
		if (curr->next == NULL)
		{
			curr->next = new;
			return (new);
		}
		curr = curr->next;
	}
	tmp = curr->next;
	curr->next = new;
	new->next = tmp;

	return (new);
}
