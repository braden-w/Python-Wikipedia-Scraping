import wikipediaapi

import networkx as nx


class Graph(nx.Graph):
    def __init__(self, start_page_name, end_page_name, language="en"):
        super().__init__()
        self.wikipedia = wikipediaapi.Wikipedia(language)

    def recurse_until_path(self, root):
        self.generate_node_with_children(start_page_name)

    def generate_node(self, node, children):
        self.add_node(node, children=children)
    def check_path(self, a, b):
        super().shortest_path(G, source=a, target=b)

    def view_nodes_edges(self):
        print(list(self.nodes), list(self.edges))


# G = Graph()
# G.add_nodes(1, 2)

G = Graph("Germany")
G.add_node(1)
G.view_nodes_edges()
# generate_edges_by_one_step("Germany")