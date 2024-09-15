#include "lists.h"
#include <stdlib.h>

/**
 * reverse_list - Reverses a singly linked list
 * @head: pointer to head of list
 * Return: pointer to head of reversed list
 */
listint_t *reverse_list(listint_t *head)
{
    listint_t *prev = NULL, *next = NULL;

    while (head)
    {
        next = head->next;
        head->next = prev;
        prev = head;
        head = next;
    }
    return prev;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    if (!head || !(*head) || !(*head)->next)
        return 1;

    listint_t *slow = *head, *fast = *head, *prev_slow = NULL, *second_half = NULL;

    while (fast && fast->next)
    {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    if (fast)
        slow = slow->next;

    second_half = reverse_list(slow);
    listint_t *copy_second_half = second_half;

    while (second_half)
    {
        if ((*head)->n != second_half->n)
        {
            reverse_list(copy_second_half); // Restore the original list
            return 0;
        }
        *head = (*head)->next;
        second_half = second_half->next;
    }

    reverse_list(copy_second_half); // Restore the original list
    return 1;
}
