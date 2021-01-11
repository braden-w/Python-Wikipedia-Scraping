import wikipediaapi
import cProfile as profile
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


class Graph(nx.DiGraph):
    def __init__(self, start_page, end_page, language="en"):
        super().__init__()
        # initializes Wikipedia is specified language (since the language is constant as pages change)
        self.wikipedia = wikipediaapi.Wikipedia(language)
        start_page_object = self.wikipedia.page(start_page)
        self.start_page = start_page
        self.end_page = end_page
        self.queue = deque(
            [
                {
                    "node_name": start_page,
                    "node_object": start_page_object,
                    "node_parent": None,
                }
            ]
        )
        profile.runctx("print(self.recurse_until_path())", globals(), locals())
        # self.recurse_until_path()

    def recurse_until_path(self):
        counter = 0
        while self.queue[0] != self.end_page:
            self.generate_node_with_children(self.queue.popleft())
            counter += 1
        self.generate_node_with_children(self.queue.popleft())
        return nx.shortest_path(self, source=self.start_page, target=self.end_page)

    def generate_node_with_children(
        self, node: {"node_name": str, "node_object": object, "node_parent": str}
    ):
        children = [
            {
                "node_name": child_name,
                "node_object": child_object,
                "node_parent": node["node_object"],
            }
            for child_name, child_object in node["node_object"].links.items()
        ]
        if node["node_parent"] is not None:
            self.add_edge(node["node_parent"], node["node_object"])
        self.queue.extend(children)
        # print(self.queue)

    def view_nodes_edges(self):
        print(list(self.nodes), list(self.edges))
        # print(self.nodes.data())


G = Graph("Feyerabend", "Germany")
# 11th Infantry Division (Wehrmacht)