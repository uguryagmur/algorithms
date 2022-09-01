#include "../src/list.h"
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

DEF_LINKED_LIST(int);

void test_append_data() {
  List *list = create_empty_list();
  assert(list->head == NULL);
  assert(list->tail == NULL);
  assert(list->size == 0);
  append_data_to_list(list, 1);
  assert(list->head != NULL);
  assert(list->tail != NULL);
  assert(list->head == list->tail);
  assert(list->size == 1);
  append_data_to_list(list, 4);
  assert(list->head != NULL);
  assert(list->tail != NULL);
  assert(list->head != list->tail);
  assert(list->size == 2);
  delete_list(list);
}

void test_get_data_from_list() {
  List *list = create_empty_list();
  append_data_to_list(list, 1);
  append_data_to_list(list, 4);
  append_data_to_list(list, 7);
  assert(get_data_from_list(list, 0) == 1);
  assert(get_data_from_list(list, 1) == 4);
  assert(get_data_from_list(list, 2) == 7);
  delete_list(list);
}

void test_create_list() {
  int data[] = {7, 3, 1, 4, 2};
  List *list = create_list(data, 5);
  assert(get_data_from_list(list, 0) == 7);
  assert(get_data_from_list(list, 1) == 3);
  assert(get_data_from_list(list, 2) == 1);
  assert(get_data_from_list(list, 3) == 4);
  assert(get_data_from_list(list, 4) == 2);
  delete_list(list);
}

int main() {
  test_append_data();
  test_get_data_from_list();
  test_create_list();
  puts("All tests are passed successfully!");
  return EXIT_SUCCESS;
}
