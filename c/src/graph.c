#include "graph.h"
#include <memory.h>

struct Queue
{
  unsigned int *queue;
  unsigned int begin_index;
  unsigned int last_index;
};

typedef struct Queue Queue;

Queue *create_empty_queue(unsigned int size)
{
  Queue *queue = malloc(sizeof(Queue));
  if (queue != NULL)
  {
    queue->queue = malloc(sizeof(unsigned int) * (size + 1));
    memset(queue->queue, 0, size + 1);
    queue->begin_index = 0;
    queue->last_index = 0;
  }
  return queue;
}

void delete_queue(Queue *queue)
{
  free(queue->queue);
  free(queue);
}

void enqueue(Queue *queue, unsigned int data)
{
  queue->queue[queue->last_index] = data;
  queue->last_index += 1;
}

unsigned int dequeue(Queue *queue)
{
  queue->begin_index += 1;
  return queue->queue[queue->begin_index - 1];
}

Graph *create_graph_without_edge(unsigned int num_nodes)
{
  Graph *graph = (Graph *)malloc(sizeof(Graph));
  graph->num_nodes = num_nodes;
  graph->adj_list = (unsigned int **)malloc(num_nodes * sizeof(unsigned int *));
  graph->adj_list_length =
      (unsigned int *)malloc(num_nodes * sizeof(unsigned int *));
  for (unsigned int i = 0; i < num_nodes; i++)
  {
    graph->adj_list_length[i] = 0;
    graph->adj_list[i] = NULL;
  }
  return graph;
}

void add_edge_to_graph(Graph *graph, Edge edge, bool is_directed)
{
  graph->adj_list_length[edge.from] += 1;
  graph->adj_list[edge.from] = (unsigned int *)realloc(
      graph->adj_list[edge.from],
      graph->adj_list_length[edge.from] * sizeof(unsigned int));
  graph->adj_list[edge.from][graph->adj_list_length[edge.from] - 1] = edge.to;
  if (!is_directed)
  {
    Edge reversed = {edge.to, edge.from};
    add_edge_to_graph(graph, reversed, true);
  }
}

Graph *create_graph(unsigned int num_nodes, unsigned int num_edges,
                    Edge edges[], bool is_directed)
{
  Graph *graph = create_graph_without_edge(num_nodes);
  for (unsigned int i = 0; i < num_edges; i++)
  {
    add_edge_to_graph(graph, edges[i], is_directed);
  }
  return graph;
}

void delete_graph(Graph *graph)
{
  if (graph->adj_list_length != NULL)
  {
    free(graph->adj_list_length);
  }
  if (graph->adj_list != NULL)
  {
    for (unsigned int i = 0; i < graph->num_nodes; i++)
    {
      if (graph->adj_list[i] != NULL)
      {
        free(graph->adj_list[i]);
      }
    }
    free(graph->adj_list);
  }
  free(graph);
}

TraverseArray *create_traverse_array(unsigned int size)
{
  TraverseArray *traverse_array = malloc(sizeof(TraverseArray));
  traverse_array->index = 0;
  traverse_array->array = malloc(size * sizeof(int));
  memset(traverse_array->array, -1, size);
  return traverse_array;
}

void delete_traverse_array(TraverseArray *array)
{
  free(array->array);
  free(array);
}

void dfs_util(Graph *graph, unsigned int source, TraverseArray *traverse_array, bool *visited)
{
  traverse_array->array[traverse_array->index] = source;
  traverse_array->index += 1;
  visited[source] = true;
  for (int i = 0; i < graph->adj_list_length[source]; i++)
  {
    if (!visited[graph->adj_list[source][i]])
    {
      dfs_util(graph, graph->adj_list[source][i], traverse_array, visited);
    }
  }
}

TraverseArray *dfs(Graph *graph, unsigned int source)
{
  bool *visited = malloc(sizeof(bool) * graph->num_nodes);
  memset(visited, false, graph->num_nodes);
  TraverseArray *traverse_array = create_traverse_array(graph->num_nodes);
  dfs_util(graph, source, traverse_array, visited);
  free(visited);
  return traverse_array;
}

TraverseArray *bfs(Graph *graph, unsigned int source)
{
  TraverseArray *traverse_array = create_traverse_array(graph->num_nodes);

  Queue *queue = create_empty_queue(graph->num_nodes);
  bool *visited = malloc(sizeof(bool) * graph->num_nodes);
  memset(visited, false, graph->num_nodes);
  enqueue(queue, source);
  visited[source] = true;

  while (queue->begin_index < queue->last_index)
  {
    source = dequeue(queue);
    traverse_array->array[traverse_array->index] = source;
    traverse_array->index += 1;
    for (int i = 0; i < graph->adj_list_length[source]; i++)
    {
      if (!visited[graph->adj_list[source][i]])
      {
        visited[graph->adj_list[source][i]] = true;
        enqueue(queue, graph->adj_list[source][i]);
      }
    }
  }
  free(visited);
  delete_queue(queue);
  return traverse_array;
}