from lib import Graph


def has_route_between_nodes(G: Graph, S: str, E: str):
    """
    Checks if there is a route from S to E in a graph G
    """
    adj_dict = G.get_adjacency_dict()

    def find_route(queue, visited):
        if not len(queue):
            return False

        current = queue.pop()

        if current == E:
            return True

        for neighbour in adj_dict[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

        return find_route(queue, visited)

    return find_route([S], set())


nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edges = [
    ('A', 'B'),
    ('B', 'C'),
    ('C', 'D'),
    ('C', 'F'),
    ('C', 'G'),
    ('D', 'E'),
    ('E', 'F'),
]

G = Graph(nodes, edges)

assert has_route_between_nodes(G, 'A', 'F') == True
assert has_route_between_nodes(G, 'F', 'C') == False
assert has_route_between_nodes(G, 'C', 'G') == True
assert has_route_between_nodes(G, 'C', 'A') == False
