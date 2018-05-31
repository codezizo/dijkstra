import heapq
import sys

class Graph:
	def __init__(self, nodes):
		self.nodes = set(nodes)
		self.edges = {}
		for node in nodes:
			self.edges[node] = {}

	def connect(self, x, y, value):
		self.edges[x][y] = value

	def dikjstra(self, start):
		dist = {}
		path = {}
		unvisited = []
		for node in self.nodes:
			if node == start:
				dist[start] = 0
			else:
				dist[node] = sys.maxint # sys.maxsize in python 3
			path[node] = []
			heapq.heappush(unvisited, (dist[node], node))

		while unvisited:
			weight, u = heapq.heappop(unvisited)
			for neighbor in self.edges[u]:
				temp_dist = dist[u] + self.edges[u][neighbor]
				if temp_dist < dist[neighbor]:
					remove_and_update_priority(unvisited, dist, neighbor, temp_dist)
					dist[neighbor] = temp_dist
					path[neighbor] = path[u] + [u]
		return dist, path

# helper function to update heap based on new distance		
def remove_and_update_priority(heap, dist, node, value):
	for index, item in enumerate(heap):
		distance,potential_node = item[0], item[1]
		if potential_node == node and distance == dist[node]:
			heap.pop(index)
	heapq.heappush(heap, (value, node))



graph = Graph([1,2,3,4,5,6])
graph.connect(1,2,1)
graph.connect(1,3,5)
graph.connect(2,4,2)
graph.connect(2,5,3)
graph.connect(3,5,1)
graph.connect(5,6,1)
graph.connect(4,6,3)
print(graph.dikjstra(1))