# from collections import defaultdict

# class DisjointSet:
#     def __init__(self, vertices):
#         self.parent = {v: v for v in vertices}
#         self.rank = {v: 0 for v in vertices}

#     def find(self, vertex):
#         if self.parent[vertex] != vertex:
#             self.parent[vertex] = self.find(self.parent[vertex])
#         return self.parent[vertex]

#     def union(self, vertex1, vertex2):
#         root1 = self.find(vertex1)
#         root2 = self.find(vertex2)
#         if self.rank[root1] < self.rank[root2]:
#             self.parent[root1] = root2
#         elif self.rank[root1] > self.rank[root2]:
#             self.parent[root2] = root1
#         else:
#             self.parent[root2] = root1
#             self.rank[root1] += 1


# def kruskal(graph):
#     mst = []
#     disjoint_set = DisjointSet(graph.keys())

#     edges = []
#     for vertex in graph:
#         for neighbor, weight in graph[vertex]:
#             edges.append((weight, vertex, neighbor))
#     edges.sort()

#     num_edges = 0
#     for edge in edges:
#         if(num_edges >= len(graph.keys()) - 1):
#             break

#         weight, vertex1, vertex2 = edge
#         if disjoint_set.find(vertex1) != disjoint_set.find(vertex2):
#             mst.append((vertex1, vertex2, weight))
#             num_edges += 1
#             disjoint_set.union(vertex1, vertex2)

#     return mst


# # Example graph
# # graph = {
# #     'A': [('B', 4), ('C', 2)],
# #     'B': [('A', 4), ('C', 1), ('D', 5)],
# #     'C': [('A', 2), ('B', 1), ('D', 8)],
# #     'D': [('B', 5), ('C', 8)]
# # }

# graph = defaultdict(list)

# print("enter the edges and weights with nodes seperated by space eg. u v w (enter -1 to finish)")
# while(True):
#     edge = input().split()
#     if edge[0] == "-1":
#         break
#     graph[edge[0]].append((edge[1], int(edge[2])))


# # Find the minimum spanning tree using Kruskal's algorithm
# mst = kruskal(graph)

# # Print the minimum spanning tree
# for vertex1, vertex2, weight in mst:
#     print(f"{vertex1} - {vertex2}: {weight}")



class Graph:  
    def __init__(self, vertices):  
        self.vertices = vertices  
        self.edges = []  
        self.adjacency_list = {v: [] for v in vertices}  
  
    def add_edge(self, u, v, weight):  
        self.edges.append((u, v, weight))  
        self.adjacency_list[u].append((v, weight))  
        self.adjacency_list[v].append((u, weight))  
  
    def find_parent(self, parent, i):  
        if parent[i] == i:  
            return i  
        return self.find_parent(parent, parent[i])  
  
    def union(self, parent, rank, x, y):  
        root_x = self.find_parent(parent, x)  
        root_y = self.find_parent(parent, y)  
        if rank[root_x] < rank[root_y]:  
            parent[root_x] = root_y  
        elif rank[root_x] > rank[root_y]:  
            parent[root_y] = root_x  
        else:  
            parent[root_y] = root_x  
            rank[root_x] += 1  
  
    def kruskal(self):  
        minimum_spanning_tree = set()  
        parent = {}  
        rank = {}  
        for v in self.vertices:  
            parent[v] = v  
            rank[v] = 0  
        sorted_edges = sorted(self.edges, key=lambda x: x[2])  
        for edge in sorted_edges:  
            u, v, weight = edge  
            root_u = self.find_parent(parent, u)  
            root_v = self.find_parent(parent, v)  
            if root_u != root_v:  
                minimum_spanning_tree.add(edge)  
                self.union(parent, rank, root_u, root_v)  
        return minimum_spanning_tree  
vertices = [0, 1, 2, 3]  
g = Graph(vertices)  
g.add_edge(0, 1, 5)  
g.add_edge(0, 2, 10)  
g.add_edge(0, 3, 3)  
g.add_edge(1, 3, 1)  
g.add_edge(2, 3, 4)  
minimum_spanning_tree = g.kruskal()  
print(minimum_spanning_tree)


