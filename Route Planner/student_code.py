import math
import heapq as hq

def shortest_path(M,start,goal):
    # A* search expands using f = g + h, where g = path cost, and h = estimated distance
    # We will use the euclidean distance equation for h estimation
    node_set = set(M.intersections.keys())
    # Dict to store SP from start node
    g = {node: float('inf') for node in node_set}
    g[start] = 0
    
    # Dict to store the total estimated cost from node to end
    f = {node: float('inf') for node in node_set}
    f[start] = euclidean_distance(M.intersections[start], M.intersections[goal])
    
    # Use a priority queue to store and pop min f distance to goal
    pq = [(f[start], start)]
    path_to = {}
    
    while pq:
        
        curr_f, curr_node = hq.heappop(pq)
        
        #Check for if we have reached goal, and return the path to end
        if curr_node == goal:
            path = [curr_node]
            while curr_node in path_to:
                curr_node = path_to[curr_node]
                path.append(curr_node)
            return path[::-1]
        
        for neighbour in M.roads[curr_node]:
            g_dist = g[curr_node] + euclidean_distance(M.intersections[curr_node], M.intersections[neighbour])
            
            if g_dist < g[neighbour]:
                path_to[neighbour] = curr_node
                g[neighbour] = g_dist
                f[neighbour] = g[neighbour] + euclidean_distance(M.intersections[neighbour], M.intersections[goal])
                hq.heappush(pq, (f[neighbour], neighbour))
    
    return None


def euclidean_distance(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)