#include "list.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

struct Graph
{
  unsigned int num_nodes;
  unsigned int *adj_list_length;
  unsigned int **adj_list;
};

struct Edge
{
  unsigned int from, to;
};

struct TraverseArray
{
  int *array;
  unsigned int index;
};

typedef struct Edge Edge;
typedef struct Graph Graph;
typedef struct TraverseArray TraverseArray;

Graph *create_graph_without_edge(unsigned int num_nodes);

void add_edge_to_graph(Graph *graph, Edge edge, bool is_directed);

Graph *create_graph(unsigned int num_nodes, unsigned int num_edges,
                    Edge edges[], bool is_directed);

void delete_graph(Graph *graph);

void delete_traverse_array(TraverseArray *array);

TraverseArray *dfs(Graph *graph, unsigned int source);
TraverseArray *bfs(Graph *graph, unsigned int source);