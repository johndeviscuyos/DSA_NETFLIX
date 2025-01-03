import networkx as nx
import matplotlib.pyplot as plt


def create_train_graph():
    # Initialize a graph
    G = nx.Graph()

    # Define MRT and LRT stations as edges (connections)
    edges = [
        # MRT-3 Line
        ('North Avenue', 'Quezon Avenue', 1),
        ('Quezon Avenue', 'GMA Kamuning', 1),
        ('GMA Kamuning', 'Araneta Center-Cubao', 1),
        ('Araneta Center-Cubao', 'Santolan-Annapolis', 1),
        ('Santolan-Annapolis', 'Ortigas', 1),
        ('Ortigas', 'Shaw Boulevard', 1),
        ('Shaw Boulevard', 'Boni', 1),
        ('Boni', 'Guadalupe', 1),
        ('Guadalupe', 'Buendia', 1),
        ('Buendia', 'Ayala', 1),
        ('Ayala', 'Magallanes', 1),
        ('Magallanes', 'Taft Avenue', 1),

        # LRT-1 Line
        ('Roosevelt', 'Balintawak', 1),
        ('Balintawak', 'Monumento', 1),
        ('Monumento', '5th Avenue', 1),
        ('5th Avenue', 'R. Papa', 1),
        ('R. Papa', 'Abad Santos', 1),
        ('Abad Santos', 'Blumentritt', 1),
        ('Blumentritt', 'Tayuman', 1),
        ('Tayuman', 'Bambang', 1),
        ('Bambang', 'Doroteo Jose', 1),
        ('Doroteo Jose', 'Carriedo', 1),
        ('Carriedo', 'Central Terminal', 1),
        ('Central Terminal', 'UN Avenue', 1),
        ('UN Avenue', 'Pedro Gil', 1),
        ('Pedro Gil', 'Quirino', 1),
        ('Quirino', 'Vito Cruz', 1),
        ('Vito Cruz', 'Gil Puyat', 1),
        ('Gil Puyat', 'Libertad', 1),
        ('Libertad', 'EDSA', 1),
        ('EDSA', 'Baclaran', 1),
        ('Baclaran', 'Redemptorist', 1),
        ('Redemptorist', 'MIA', 1),
        ('MIA', 'Asiaworld', 1),
        ('Asiaworld', 'Ninoy Aquino', 1),
        ('Ninoy Aquino', 'Dr.Santos', 1),
        ('Dr.Santos', 'Las Piñas', 1),
        ('Las Piñas', 'Zapote', 1),
        ('Zapote', 'Niog', 1),

        # LRT-2 Line
        ('Recto', 'Legarda', 1),
        ('Legarda', 'Pureza', 1),
        ('Pureza', 'V. Mapa', 1),
        ('V. Mapa', 'J. Ruiz', 1),
        ('J. Ruiz', 'Gilmore', 1),
        ('Gilmore', 'Betty Go-Belmonte', 1),
        ('Betty Go-Belmonte', 'Araneta Center-Cubao', 1),
        ('Araneta Center-Cubao', 'Anonas', 1),
        ('Anonas', 'Katipunan', 1),
        ('Katipunan', 'Santolan', 1),
        ('Santolan', 'Marikina-Pasig', 1),
        ('Marikina-Pasig', 'Antipolo', 1),

        # Transfer Stations
        ('Doroteo Jose', 'Recto', 1),  # LRT-1 to LRT-2 transfer
        ('Araneta Center-Cubao', 'Araneta Center-Cubao', 0)  # MRT-3 to LRT-2 transfer (self-loop for transfer)
    ]

    # Add edges to the graph with weights
    G.add_weighted_edges_from(edges)
    return G



def find_shortest_path(G, source, target):
    # Find the shortest path using Dijkstra's algorithm
    try:
        path = nx.shortest_path(G, source=source, target=target, weight='weight')
        distance = nx.shortest_path_length(G, source=source, target=target, weight='weight')
        return path, distance
    except nx.NetworkXNoPath:
        return None, None


def main():
    G = create_train_graph()


    print("MRT and LRT Train Stations Shortest Path Finder")
    source = input("Enter the starting station: ")
    target = input("Enter the destination station: ")

    path, distance = find_shortest_path(G, source, target)

    if path:
        print(f"Shortest path from {source} to {target}: {path}")
        print(f"Total distance: {distance} stations")
    else:
        print(f"No path found between {source} and {target}.")


if __name__ == "__main__":
    main()
