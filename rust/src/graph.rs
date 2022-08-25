use std::collections::HashMap;

#[derive(Eq, Clone, Copy, Hash, PartialEq, Debug)]
pub struct GraphNode<T> {
    _id: usize,
    _data: T,
}

impl GraphNode<usize> {
    pub fn create_with_id(data: usize) -> Self {
        Self { _id: data, _data: data }
    }
}

impl<T> GraphNode<T> {
    pub fn create(id: usize, data: T) -> Self {
        Self {_id: id, _data: data}
    }
}

#[derive(Debug)]
pub struct UndirectedGraph<T> {
    _adj_list: HashMap<GraphNode<T>, Vec<GraphNode<T>>>,
}

pub struct DirectedGraph<T> {
    _adj_list: HashMap<GraphNode<T>, Vec<GraphNode<T>>>,
}

impl<T: Copy + Clone + Eq + std::hash::Hash + std::fmt::Debug> UndirectedGraph<T> {
    pub fn create(edges: &[(&GraphNode<T>, &GraphNode<T>)]) -> UndirectedGraph<T> {
        let mut graph: UndirectedGraph<T> = UndirectedGraph {
            _adj_list: HashMap::new(),
        };
        for i in 0..edges.len() {
            graph.add_edge(edges[i].0, edges[i].1);
            graph.add_edge(edges[i].1, edges[i].0);
        }
        graph
    }

    pub fn add_edge(&mut self, node1: &GraphNode<T>, node2: &GraphNode<T>) {
        if self._adj_list.get(&node1).is_none() {
            self._adj_list.insert(*node1, vec![*node2]);
        } else {
            self._adj_list.get_mut(&node1).unwrap().push(*node2);
        }
    }

    pub fn dfs(&self, source: &GraphNode<T>) {
        let mut visited = vec![false; self._adj_list.len()];
        visited[source._id] = true;

        for (node, list) in &self._adj_list {
            if !visited[node._id] {
                self._dfs(source, &mut visited);
            }
        }
        print!("\n");
    }

    pub fn bfs(&self, source: GraphNode<T>){

    }

    fn _dfs(&self, source: &GraphNode<T>, visited: &mut Vec<bool>) {
        visited[source._id] = true;
        print!("{:?} ", source._data);
        for i in 0..self._adj_list.get(&source).unwrap().len() {
            if !visited[self._adj_list.get(&source).unwrap()[i]._id] {
                self._dfs(&self._adj_list.get(source).unwrap()[i], visited);
            }
        }
    }
}
