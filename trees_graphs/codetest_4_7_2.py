from enum import Enum
from collections import deque

def find_builder_order(projects, dependencies):
  graph = build_graph(projects, dependencies)
  return order_projects(projects)
  
def order_projects(projects):
  order_list = deque()
  for project in projects:
    if project.state == Project.State.BLANK:
      if not dfs(projects, order_list):
        return None
  return order_list

def dfs(project, order_list):
  # found cycle.
  if project.state == Project.State.PARTIAL:
    return False
  if project.state == Project.State.BLANK:
    project.state = Project.State.PARTIAL
    children = project.children
    for child in children:
      if not dfs(child,order_list):
        return False
    project.state = Project.State.COMPLETE
    order_list.append(project)
  return True
    
def build_graph(projects, dependencies):
  graph = Graph()
  for project in projects:
    graph.get_or_create_node(project)
  for dependency in dependencies:
    first = dependency[0]
    second = dependency[1]
    graph.add_edge(first, second)
  return graph

class Project:

  def __init__(self, name):
    self.name = name
    self.map = {}
    self.dependencies = 0
    self.children = []
    self.state = self.State.BLANK

  class State(Enum):
    COMPLETE = 1
    PARTIAL = 2
    BLANK = 3

  def add_neighbor(self, node:'Project'):
    if node.name not in self.map:
      self.map[node.name] = node
      self.children.append(node)
      node.increment_dependencies()

  def increment_dependencies(self):
    self.dependencies += 1

  def decrement_dependencies(self):
    self.dependencies -= 1

class Graph:
  def __init__(self):
    self.nodes = []
    self.map = {}

  def get_or_create_node(self, name)-> Project:
    if name not in self.map:
      node = Project(name)
      self.nodes.append(node)
      self.map[name] = node
    return self.map[name]

  def add_edge(self, start_name, end_name):
    start = self.get_or_create_node(start_name)
    end = self.get_or_create_node(end_name)
    start.add_neighbor(end)