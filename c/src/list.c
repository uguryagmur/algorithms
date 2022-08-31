#include <stdio.h>
#include <stdlib.h>

#define DEF_NODE(TYPE)                                                         \
  struct ListNode {                                                            \
    TYPE data;                                                                 \
    ListNode *next;                                                            \
  };

typedef struct List List;
typedef struct ListNode ListNode;

DEF_NODE(int);

struct List {
  unsigned int size;
  ListNode *head, *tail;
};

void append_data_to_array(const int data, List *ptr) {
  ListNode *node = malloc(sizeof(ListNode));
  node->data = data;
  node->next = NULL;
  if (ptr->head == NULL) {
    ptr->head = node;
  } else {
    ptr->tail->next = node;
  }
  ptr->tail = node;
}

List *create_list(const int data[], unsigned int size) {
  List *output = malloc(sizeof(List));
  for (int i = 0; i < size; i++) {
    append_data_to_array(data[i], output);
  }
  return output;
}

void delete_list(List *ptr) {
  ListNode *current = ptr->head, *next;
  while (current != NULL) {
    next = current->next;
    free(current);
    current = next;
  }
  free(ptr);
}
