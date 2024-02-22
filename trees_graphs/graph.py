from enum import Enum, auto


class State(Enum):
  UNVISITED = auto()
  VISITING = auto()
  VISITED = auto()


class Node:

  def __init__(self, value):
    self.value = value
    self.state = State.UNVISITED
    self.neighbors = []  # List to hold neighbors

  def add_neighbor(self, neighbor):
    self.neighbors.append(neighbor)

  def __eq__(self, other):
    if isinstance(other, Node):
      return self.value == other.value
    return False

  def __str__(self):
    return str(self.value)


class Graph:

  def __init__(self):
    self.nodes = {}  # Dictionary to store nodes by value for easy lookup

  def add_node(self, value):
    if value not in self.nodes:
      self.nodes[value] = Node(value)

  def add_edge(self, source_value, destination_value):
    if source_value in self.nodes and destination_value in self.nodes:
      self.nodes[source_value].add_neighbor(self.nodes[destination_value])
    else:
      # Create nodes if they don't exist
      if source_value not in self.nodes:
        self.add_node(source_value)
      if destination_value not in self.nodes:
        self.add_node(destination_value)
      self.nodes[source_value].add_neighbor(self.nodes[destination_value])

  def display_graph(self):
    for node in self.nodes.values():
      neighbors_values = [neighbor.value for neighbor in node.neighbors]
      print(
          f"{node.value} ({node.state.name}) -> {' '.join(neighbors_values)}")
