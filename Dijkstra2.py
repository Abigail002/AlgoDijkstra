from collections import defaultdict
import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start, end):
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    heap = [(0, start)]
    previous = defaultdict(lambda: None)
    while heap:
        (dist, current) = heapq.heappop(heap)
        if current == end:
            break
        for neighbor in graph[current]:
            new_distance = dist + graph[current][neighbor]
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current
                heapq.heappush(heap, (new_distance, neighbor))
    return (distances, previous)

def shortest_path(graph, start, end):
    (distances, previous) = dijkstra(graph, start, end)
    path = []
    current = end
    while current != start:
        path.append(current)
        current = previous[current]
    path.append(start)
    path.reverse()
    return path

graph = defaultdict(dict)
edges = [("A", "B", 7), ("A", "C", 9), ("A", "F", 14), ("B", "C", 10),
         ("B", "D", 15), ("C", "D", 11), ("C", "F", 2), ("D", "E", 6),
         ("E", "F", 9)]
for (start, end, cost) in edges:
    graph[start][end] = cost
    graph[end][start] = cost

def draw_graph(graph, start, end, path):
    G = nx.Graph(graph)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): graph[u][v] for u, v in G.edges()})
    path_edges = [(path[i], path[i+1]) for i in range(len(path) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
    plt.show()

graph = defaultdict(dict)
for (start, end, cost) in edges:
    graph[start][end] = cost
    graph[end][start] = cost

path = shortest_path(graph, 'A', 'E')

print(f"Le plus court chemin du point A au point E est: {path}")
draw_graph(graph, 'A', 'E', path)