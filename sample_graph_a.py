from graph import Graph

# Create a graph instance
graph = Graph()

# Add nodes with values
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')
graph.add_node('F')
graph.add_node('G')
graph.add_node('H')

# Add directed edges (A -> B, A -> C, B -> C)
graph.add_edge('A', 'B')
graph.add_edge('A', 'F')
graph.add_edge('B', 'C')
graph.add_edge('B', 'D')
graph.add_edge('D', 'E')
graph.add_edge('E', 'B')
graph.add_edge('E', 'G')
graph.add_edge('G', 'H')
graph.add_edge('I', 'E')

# Display the graph
graph.display_graph()
