#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

size_t print_listint(const listint_t *h)
{
    size_t nodes = 0;

    while (h)
    {
        printf("%d\n", h->n);
        h = h->next;
        nodes++;
    }
    return nodes;
}

listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new = malloc(sizeof(listint_t));
    listint_t *last = *head;

    if (!new)
        return NULL;

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
    {
        *head = new;
        return new;
    }

    while (last->next)
        last = last->next;

    last->next = new;

    return new;
}

void free_listint(listint_t *head)
{
    listint_t *current;

    while (head)
    {
        current = head;
        head = head->next;
        free(current);
    }
}
