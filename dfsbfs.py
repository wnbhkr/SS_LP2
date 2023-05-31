from collections import defaultdict

# def dfs(root,visited):
#     visited.append(root)
#     for i in graph[root]:
#         if i not in visited:
#             dfs(i,visited)
#     return visited

def bfs(graph, queue, visited):
    if not queue:
        return
    
    node=queue.pop(0)
    for i in graph[node]: 
        if i not in visited:
            visited.append(i)
            queue.append(i)
    bfs(graph,queue,visited)
    

graph=defaultdict(list)
print("enter the edges with nodes seperated by space eg. u v (enter -1 to finish)")
while(True):
    edge=input().split()
    if edge[0]=='-1':
        break
    graph[edge[0]].append(edge[1])
    

root=input('Enter the start node')

# for dfs
# visited = []
# print('The dfs traversal of the graph is ',dfs(root,visited))

# for bfs
visited=[root]
queue=[root]
bfs(graph,queue,visited)
print('The bfs traversal of graph is ',visited)
