/* vulnerable.c — original broken version */
list_t *add_node_end(list_t *head, const int n) {
    list_t *new_node = malloc(sizeof(list_t));
    list_t *current = head;
    if (!head)
        return (new_node);
    while (current)
        current = current->next;
    current = new_node;   /* BUG: only changes local pointer */
    new_node->n = n;      /* BUG: new_node may be NULL (no malloc check) */
    new_node->next = NULL;
    return (head);
}
