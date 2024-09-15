#include "lists.h"
#include <stdlib.h>

/**
 * reverse_list - Reverses a linked list.
 * @head: Pointer to the first node of the list to reverse.
 * 
 * Return: Pointer to the first node of the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
    listint_t *prev = NULL;
    listint_t *current = head;
    listint_t *next;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    return (prev);
}

/**
 * compare_lists - Compares two linked lists node by node.
 * @head1: First linked list.
 * @head2: Second linked list.
 * 
 * Return: 1 if both lists are identical, 0 otherwise.
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
    while (head1 != NULL && head2 != NULL)
    {
        if (head1->n != head2->n)
            return (0);
        head1 = head1->next;
        head2 = head2->next;
    }
    return (1);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Double pointer to the head of the list.
 * 
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head;
    listint_t *second_half, *prev_of_slow = *head;
    listint_t *mid_node = NULL;  /* To handle odd size lists */
    int result = 1;  /* Assume list is palindrome */

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    /* Find the middle of the list */
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_of_slow = slow;
        slow = slow->next;
    }

    /* Handle odd-size lists */
    if (fast != NULL)
    {
        mid_node = slow;
        slow = slow->next;
    }

    /* Reverse the second half of the list */
    second_half = reverse_list(slow);
    prev_of_slow->next = NULL;  /* Terminate the first half */

    /* Compare the two halves */
    result = compare_lists(*head, second_half);

    /* Restore the original list */
    second_half = reverse_list(second_half);  /* Reverse again to restore */
    if (mid_node != NULL)  /* If there was a middle element */
    {
        prev_of_slow->next = mid_node;
        mid_node->next = second_half;
    }
    else
    {
        prev_of_slow->next = second_half;
    }

    return (result);
}
