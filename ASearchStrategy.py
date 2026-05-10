import heapq

def a_star(start, goal, graph, heuristic):
    """
    A* search that optimizes path cost.
    
    :param start: starting node
    :param goal: goal node
    :param graph: dict of dicts; graph[node] = {neighbor: cost, ...}
    :param heuristic: dict; heuristic[node] = estimated cost to goal
    :return: (path, total_cost) or (None, float('inf')) if no path
    """
    # Priority queue: (f_score, g_score, node, path)
    open_set = [(heuristic[start], 0, start, [start])]
    heapq.heapify(open_set)
    
    # Visited nodes with best known g_score
    closed_set = {}
    
    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        
        # Goal test
        if current == goal:
            return path, g
        
        # If we already found a better path to this node, skip
        if current in closed_set and closed_set[current] <= g:
            continue
        closed_set[current] = g
        
        for neighbor, cost in graph.get(current, {}).items():
            new_g = g + cost
            new_f = new_g + heuristic.get(neighbor, float('inf'))
            new_path = path + [neighbor]
            
            # If neighbor not visited or found a better path
            if neighbor not in closed_set or new_g < closed_set[neighbor]:
                heapq.heappush(open_set, (new_f, new_g, neighbor, new_path))
    
    return None, float('inf')  # No path found

# Example usage
if __name__ == "__main__":
    # Graph: A, B, C, D, G as nodes. Costs on edges.
    graph = {
        'A': {'B': 1, 'C': 3},
        'B': {'A': 1, 'D': 1, 'G': 5},
        'C': {'A': 3, 'G': 2},
        'D': {'B': 1, 'G': 1},
        'G': {}
    }
    # Heuristic (straight-line distance estimates to G)
    heuristic = {
        'A': 3,
        'B': 2,
        'C': 1,
        'D': 1,
        'G': 0
    }
    
    path, cost = a_star('A', 'G', graph, heuristic)
    print(f"Optimal path: {path}, Total cost: {cost}")