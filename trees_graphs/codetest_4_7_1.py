def find_build_order(projects, dependencies):
  graph = build_graph(projects, dependencies)
  return order_projects(graph.nodes)


def build_graph(projects, dependencies):
  graph = Graph()
  for project in projects:
    graph.get_or_create_node(project)
  for dependency in dependencies:
    first = dependency[0]
    second = dependency[1]
    graph.add_edge(first, second)
  return graph


def order_projects(projects):
  order_list = [None] * len(projects)
  # add roots to the build order first.
  end_of_list = add_non_dependent(order_list, projects, 0)
  to_be_processed = 0
  while to_be_processed < len(order_list):
    current_project = order_list[to_be_processed]
    # we have circular dependency. since there are no remaining projects with zero dependency.
    if not current_project:
      return None
    # remove myself as a dependency
    children = current_project.children
    for child in children:
      child.decrement_dependencies()
    # add children that have no depending on them.
    end_of_list = add_non_dependent(order_list, children, end_of_list)
    to_be_processed += 1
  return order_list


def add_non_dependent(order, projects, offset):
  for project in projects:
    if project.dependencies == 0:
      order[offset] = project
      offset += 1
  return offset


class Graph:

  def __init__(self):
    self.nodes = []
    self.map = {}

  def get_or_create_node(self, name):
    if name not in self.map:
      node = Project(name)
      self.nodes.append(node)
      self.map[name] = node
    return map[name]

  def add_edge(self, start_name, end_name):
    start = self.get_or_create_node(start_name)
    end = self.get_or_create_node(end_name)
    start.add_neighbor(end)


class Project:

  def __init__(self, name):
    self.name = name
    self.map = {}
    self.dependencies = 0
    self.children = []

  def add_neighbor(self, node):
    if node.name not in self.map:
      self.map[node.name] = node
      self.children.append(node)
      node.increment_dependencies()

  def increment_dependencies(self):
    self.dependencies += 1

  def decrement_dependencies(self):
    self.dependencies -= 1
