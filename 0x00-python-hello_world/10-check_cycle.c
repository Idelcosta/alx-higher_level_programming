#include "lists.h"

/**
* check_cycle - check if a linked list has a cycle
* @list: the linked list to check
*
* return: 1 if the linked list has a cycle, 0 if it does not
*/
int check_cycle(listint_t *list)
{
    listint_t *first = list;
    listint_t *last = list;

    if (!list)
        return (0);

    while (first && last && last->next)
    {
        first = first->next;
        last = last->next->next;
        if (first == last)
            return (1);
    }

    return (0);
}