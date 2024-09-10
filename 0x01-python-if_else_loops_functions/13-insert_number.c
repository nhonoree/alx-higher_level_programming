#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Double pointer to the head of the linked list
 * @number: The number to insert
 *
 * Return: The address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *current, *prev;

    /* Create a new node */
    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);

    new_node->n = number;
    new_node->next = NULL;

    /* If the list is empty or the number is smaller than the head */
    if (*head == NULL || (*head)->n >= number)
    {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }

    /* Traverse the list to find the correct insertion point */
    current = *head;
    while (current != NULL && current->n < number)
    {
        prev = current;
        current = current->next;
    }

    /* Insert the new node at the correct position */
    prev->next = new_node;
    new_node->next = current;

    return (new_node);
}
