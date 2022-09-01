/*
 * Linked List definition for any type
 * <stdlib.h> should be included where this definition is used !
 *
 */

#define DEF_LINKED_LIST(TYPE)                                                  \
                                                                               \
  struct ListNode {                                                            \
    TYPE data;                                                                 \
    struct ListNode *next;                                                     \
  };                                                                           \
                                                                               \
  struct List {                                                                \
    unsigned int size;                                                         \
    struct ListNode *head, *tail;                                              \
  };                                                                           \
                                                                               \
  typedef struct List List;                                                    \
  typedef struct ListNode ListNode;                                            \
                                                                               \
  void append_data_to_list(List *list, const TYPE data) {                      \
    ListNode *node = (ListNode *)malloc(sizeof(ListNode));                     \
    node->data = data;                                                         \
    node->next = NULL;                                                         \
    if (list->head == NULL) {                                                  \
      list->head = node;                                                       \
    } else {                                                                   \
      list->tail->next = node;                                                 \
    }                                                                          \
    list->tail = node;                                                         \
    list->size += 1;                                                           \
  }                                                                            \
                                                                               \
  TYPE get_data_from_list(List *list, unsigned int index) {                    \
    if (index >= list->size) {                                                 \
      puts("SHIT2");                                                           \
      exit(EXIT_FAILURE);                                                      \
    }                                                                          \
    ListNode *current = list->head;                                            \
    unsigned int current_index = 0;                                            \
    while (current_index++ < index) {                                          \
      current = current->next;                                                 \
    }                                                                          \
    return current->data;                                                      \
  }                                                                            \
                                                                               \
  List *create_empty_list() {                                                  \
    List *list = (List *)malloc(sizeof(List));                                 \
    list->head = NULL;                                                         \
    list->tail = NULL;                                                         \
    list->size = 0;                                                            \
    return list;                                                               \
  }                                                                            \
                                                                               \
  List *create_list(const TYPE data[], unsigned int size) {                    \
    List *output = create_empty_list();                                        \
    for (int i = 0; i < size; i++) {                                           \
      append_data_to_list(output, data[i]);                                    \
    }                                                                          \
    return output;                                                             \
  }                                                                            \
                                                                               \
  void delete_list(List *list) {                                               \
    ListNode *current = list->head, *next;                                     \
    while (current != NULL) {                                                  \
      next = current->next;                                                    \
      free(current);                                                           \
      current = next;                                                          \
    }                                                                          \
    free(list);                                                                \
  }
