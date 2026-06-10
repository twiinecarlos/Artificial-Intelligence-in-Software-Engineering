# Task 0: AI — Preemptive Bug Fixing

## Overview
Used an AI tool (ChatGPT / Gemini) acting as a Senior C Developer to review
a vulnerable C linked-list function, identify both a logical error and a
memory safety flaw, and generate the corrected code.

## Files
| File | Description |
|------|-------------|
| `vulnerable.c` | Original broken `add_node_end` function |
| `fixed.c` | Corrected function with all flaws resolved |

## Flaws Identified
### 1. Logical Error — Broken List Linkage
The `while (current)` loop ran until `current` was `NULL` (past the last
node). Assigning `current = new_node` only changed the local variable, never
updating any node's `next` pointer. Fix: change loop condition to
`while (current->next)` and then set `current->next = new_node`.

### 2. Memory Safety — Missing NULL Check After malloc
`malloc` can return `NULL` on failure. The original code used `new_node`
without checking, so `new_node->n = n` would cause a **Segmentation Fault**.
Fix: add `if (!new_node) return (NULL);` immediately after `malloc`.

## AI Tool Used
[Your tool name, e.g., ChatGPT-4o]
