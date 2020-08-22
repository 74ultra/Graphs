"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            # self.vertices[v2].add(v1)
        return

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = [starting_vertex]
        result = []
        visited = {}

        visited[starting_vertex] = True
        while len(queue) > 0:
            current_vertex = queue.pop(0)
            result.append(current_vertex)
            for i in self.vertices[current_vertex]:
                if i not in visited:
                    visited[i] = True
                    queue.append(i)

        for i in result:
            print(i)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = [starting_vertex]
        result = []
        visited = {}

        visited[starting_vertex] = True
        while len(stack) > 0:
            current_vertex = stack.pop()
            result.append(current_vertex)
            for i in self.vertices[current_vertex]:
                if i not in visited:
                    visited[i] = True
                    stack.append(i)
        for i in result:
            print(i)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = {}
        result = []
        self.dft_rec_helper(starting_vertex, visited, result)
        # return result
        for i in result:
            print(i)

    def dft_rec_helper(self, vertex, visited_obj, result_arry):
        # if vertex == False:
        #     return None
        visited_obj[vertex] = True
        result_arry.append(vertex)
        for i in self.vertices[vertex]:
            if i not in visited_obj:
                self.dft_rec_helper(i, visited_obj, result_arry)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = [[starting_vertex]]
        visited = {}

        visited[starting_vertex] = True
        while len(queue) > 0:
            current_path = queue.pop(0)
            if current_path[-1] == destination_vertex:
                return current_path
            for i in self.vertices[current_path[-1]]:
                if i not in visited:
                    visited[i] = True
                    new_path = current_path + [i]
                    queue.append(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        queue = [[starting_vertex]]
        visited = {}

        visited[starting_vertex] = True
        while len(queue) > 0:
            current_path = queue.pop()
            if current_path[-1] == destination_vertex:
                return current_path
            for i in self.vertices[current_path[-1]]:
                if i not in visited:
                    visited[i] = True
                    new_path = current_path + [i]
                    queue.append(new_path)

    def dfs_recursive(self, v1, v2, path=[], visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if path is None:
            path = []
        if visited is None:
            visited = set()

        visited.add(v1)
        path = path + [v1]
        if v1 == v2:
            return path
        for i in self.vertices[v1]:
            print('i', i)
            if i not in visited:
                xer = self.dfs_recursive(i, v2, path, visited)

                if xer:
                    print('xer', xer)
                    return xer


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''

    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # print(graph.bft(1))

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # print(graph.dft(1))
    # print(graph.dft_recursive(1))

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
