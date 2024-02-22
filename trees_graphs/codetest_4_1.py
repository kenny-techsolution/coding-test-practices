from .graph import Graph, Node, State
from .sample_graph_a import graph
from collections import deque


def search(graph: Graph, start: Node, end: Node):
  # check if the start and end is the same.
  if start == end:
    return True

  for n in graph.nodes.values():
    n.state = State.UNVISITED

  q = deque()
  # put the start on to queue, so set the state to visiting.
  start.state = State.VISITING

  q.append(start)

  while q:
    node = q.popleft()
    for adj_node in node.neighbors:
      # for all the neighbors, if it's unvisited, check if it
      # match the condition, if not, put on the queue to be visited.
      if adj_node.state == State.UNVISITED:
        if adj_node == end:
          return True
        else:
          # visiting means it is put into queue. to be visited.
          adj_node.state = State.VISITING
          print(adj_node)
          q.append(adj_node)
    # visited means it visited its neighbors. left the queue.
    node.state = State.VISITED
  return False


# case A  and I . no path.
start = graph.nodes["A"]
end = graph.nodes["I"]
print(search(graph, start, end))

# case A  and H . yes path.
start = graph.nodes["A"]
end = graph.nodes["E"]
print(search(graph, start, end))
