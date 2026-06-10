/* fixed.c — corrected version */
list_t *add_node_end(list_t *head, const int n) {
    list_t *new_node = malloc(sizeof(list_t));
    list_t *current = head;

    /* FIX 1 — Memory Safety: check malloc result before dereferencing */
    if (!new_node)
        return (NULL);

    new_node->n = n;
    new_node->next = NULL;

    /* Edge case: empty list */
    if (!head)
        return (new_node);

    /* FIX 2 — Logic: stop at the LAST node, not past it */
    while (current->next)
        current = current->next;

    /* Now current IS the last node; link it to the new node */
    current->next = new_node;

    return (head);
}
