import wikipediaapi
from collections import deque
import networkx as nx


class Graph(nx.Graph):
    def __init__(self, start_page_name, end_page_name, language="en"):
        super().__init__()
        self.wikipedia = wikipediaapi.Wikipedia(language)
        self.queue = deque()
        self.queue.append(start_page)

    def recurse_until_path(self, root):
        self.generate_node_with_children(start_page_name)

    def generate_node(self, node, children):
        self.add_node(node, children=children)

    def generate_node_with_children(self, page_name):
        page_children = self.wikipedia.page(page_name).links.keys()
        self.generate_node(page_name, page_children)

    def check_path(self, a, b):
        super().shortest_path(G, source=a, target=b)

    def view_nodes_edges(self):
        print(list(self.nodes), list(self.edges))
        print(self.nodes.data())


G = Graph("Germany", "Spain")
G.view_nodes_edges()
nx.draw(G, with_labels=True, with_weight=True)