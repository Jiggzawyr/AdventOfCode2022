def get_elevation(char):
    if char == 'S': return 97
    if char == 'E': return 122
    return ord(char)

def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]  
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f]
    matrix = []
    for line in lines:
        row = []
        for l in line:
            row.append(l)
        matrix.append(row)
    M = len(matrix)
    N = len(matrix[0])
    graph = {}
    cnt = 1
    for m, row in enumerate(matrix):
        for n, elem in enumerate(row):
            if matrix[m][n] == 'S': S = cnt
            if matrix[m][n] == 'E': E = cnt
            curr = get_elevation(matrix[m][n])
            next = set()
            if m + 1 < M and curr + 1 >= get_elevation(matrix[m+1][n]): next.add(cnt + N)
            if m - 1 >= 0 and curr + 1 >= get_elevation(matrix[m-1][n]): next.add(cnt - N)
            if n + 1 < N and curr + 1 >= get_elevation(matrix[m][n+1]): next.add(cnt + 1)
            if n - 1 >= 0 and curr + 1 >= get_elevation(matrix[m][n-1]): next.add(cnt - 1)
            graph[cnt] = next
            cnt += 1
    # print(graph)
    path = shortest_path(graph, S, E)
    print(len(path)-1)