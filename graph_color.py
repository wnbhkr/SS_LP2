
def printConfiguration(colorArray):
    print("The assigned colors are as follows:")
    for i in range(4):
        print("Vertex: ",
              i, " Color: ", colorArray[i])



def isSafe(v, graph, colorArray, j):
    for i in range(4):
        if graph[v][i] == 1 and j == colorArray[i]:
            return False
    return True



def graphColoringAlgorithm(graph, m, i, colorArray):
    if(i == 4):
        printConfiguration(colorArray)
        return True

    # Assigning color to the vertex and recursively calling the function.
    for j in range(1, m + 1):
        if isSafe(i, graph, colorArray, j):
            colorArray[i] = j
            if (graphColoringAlgorithm(graph, m, i + 1, colorArray)):
                return True
            colorArray[i] = 0
    return False



graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0],
]
m = 3

# Initially the color list is initialized with 0.
colorArray = [0 for i in range(4)]

if (graphColoringAlgorithm(graph, m, 0, colorArray)):
    print("Coloring is possible!")
else:
    print("Coloring is not possible!")