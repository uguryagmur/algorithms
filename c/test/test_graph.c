#include <assert.h>
#include "../src/graph.h"

void test_create_empty_graph()
{
    Graph *graph = create_graph_without_edge(5);
    assert(graph->num_nodes == 5);
    for (int i = 0; i < graph->num_nodes; i++)
    {
        assert(graph->adj_list[i] == NULL);
        assert(graph->adj_list_length[i] == 0);
    }
    delete_graph(graph);
}

void test_add_edge_to_graph()
{
    Graph *graph = create_graph_without_edge(2);
    Edge edge = {0, 1};
    add_edge_to_graph(graph, edge, false);
    for (int i = 0; i < graph->num_nodes; i++)
    {
        assert(graph->adj_list_length[i] == 1);
        assert(graph->adj_list[i] != NULL);
        if (i == 0)
        {
            assert(graph->adj_list[i][0] == 1);
        }
        else
        {
            assert(graph->adj_list[i][0] == 0);
        }
    }
    delete_graph(graph);
}

void test_create_graph()
{
    Edge edges[] = {
        {0, 1},
        {1, 2},
        {2, 3},
        {3, 0},
    };
    Graph *graph = create_graph(4, 4, edges, false);
    for (int i = 0; i < graph->num_nodes; i++)
    {
        assert(graph->adj_list_length[i] == 2);
        assert(graph->adj_list[i] != NULL);
        unsigned int left, right;
        if (i == 0)
        {
            left = 1;
            right = 3;
        }
        else if (i == 3)
        {
            left = 2;
            right = 0;
        }
        else
        {
            left = i - 1;
            right = i + 1;
        }
        assert(graph->adj_list[i][0] == left);
        assert(graph->adj_list[i][1] == right);
    }
    delete_graph(graph);
}

void test_dfs()
{
    Edge edges[] = {
        {0, 1},
        {0, 2},
        {1, 3},
        {1, 5},
        {2, 4},
        {4, 5},
    };
    Graph *graph = create_graph(6, 6, edges, false);
    TraverseArray *traverse_array = dfs(graph, 0);
    int expexted_traversal_array[] = {0, 1, 3, 5, 4, 2};
    for (int i = 0; i < graph->num_nodes; i++)
    {
        assert(traverse_array->array[i] == expexted_traversal_array[i]);
    }
    delete_graph(graph);
    delete_traverse_array(traverse_array);
}

void test_bfs()
{
    Edge edges[] = {
        {0, 1},
        {0, 2},
        {1, 3},
        {1, 5},
        {2, 4},
        {4, 5},
    };
    Graph *graph = create_graph(6, 6, edges, false);
    TraverseArray *traverse_array = bfs(graph, 0);
    int expexted_traversal_array[] = {0, 1, 2, 3, 5, 4};
    for (int i = 0; i < graph->num_nodes; i++)
    {
        assert(traverse_array->array[i] == expexted_traversal_array[i]);
    }
    delete_graph(graph);
    delete_traverse_array(traverse_array);
}

int main()
{
    test_create_empty_graph();
    test_add_edge_to_graph();
    test_create_graph();
    test_dfs();
    test_bfs();
    puts("All tests are passed successfully!");
    return EXIT_SUCCESS;
}