import wikipediaapi
from collections import deque
import networkx as nx


class Graph(nx.Graph):
    def __init__(self, start_page, end_page, language="en"):
        super().__init__()
        # initializes Wikipedia is specified language (since the language is constant as pages change)
        self.wikipedia = wikipediaapi.Wikipedia(language)
        self.start_page = start_page
        self.end_page = end_page
        self.queue = deque()
        self.queue.append(start_page)
        self.recurse_until_path()

    def recurse_until_path(self):
        while self.queue[0] != self.end_page:
            self.generate_node_with_children(self.queue.popleft())
        self.generate_node_with_children(self.queue.popleft())
        return nx.shortest_path(self, source=self.start_page, target=self.end_page)

    def generate_node_with_children(self, node):
        children = self.wikipedia.page(node).links.keys()
        self.add_node(node)
        self.queue.extend(children)

    def view_nodes_edges(self):
        print(list(self.nodes), list(self.edges))
        print(self.nodes.data())


G = Graph("Germany", "Spain")
G.view_nodes_edges()
nx.draw(G, with_labels=True, with_weight=True)