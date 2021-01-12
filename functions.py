import wikipediaapi
import cProfile as profile
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


class Graph(nx.DiGraph):
    def __init__(self, start_page: str, end_page: str, language: str = "en"):
        super().__init__()
        # initializes Wikipedia is specified language (since the language is constant as pages change)
        self.wikipedia = wikipediaapi.Wikipedia(language)
        start_page_object = self.wikipedia.page(start_page)
        self.start_page = start_page
        self.end_page = end_page
        self.image_counter = 0
        self.queue = deque(
            [
                {
                    "node_name": start_page,
                    "node_object": start_page_object,
                    "node_parent": None,
                }
            ]
        )

    def recurse_until_path(self):
        while self.queue[0]["node_name"] != self.end_page:
            self.link_node_to_parent(self.queue.popleft())
            # self.write_graph()
        await self.link_node_to_parent(self.queue.popleft())
        self.create_graph()
        return nx.shortest_path(self, source=self.start_page, target=self.end_page)

    async def link_node_to_parent(
        self, node: {"node_name": str, "node_object": object, "node_parent": str}
    ):
        if node["node_parent"] is not None:
            self.add_edge(node["node_parent"], node["node_name"])
        await self.generate_children_from_node(node)

    async def generate_children_from_node(
        self, node: {"node_name": str, "node_object": object, "node_parent": str}
    ):
        children = [
            {
                "node_name": child_name,
                "node_object": child_object,
                "node_parent": node["node_name"],
            }
            for (child_name, child_object) in node["node_object"].links.items()
        ]
        self.queue.extend(children)

    def list_nodes_edges(self):
        print(list(self.nodes), list(self.edges))
        # print(self.nodes.data())

    def create_graph(self):
        nx.draw(self, with_labels=True)
        plt.show()

    def write_graph(self):
        nx.draw(self, with_labels=True)
        plt.savefig("img" + str(self.image_counter) + ".png")
        plt.clf()
        self.image_counter += 1


G = Graph("Feyerabend", "Germany")
G.recurse_until_path()
# Feyerabend
# 18th-century history of Germany
# 11th Infantry Division (Wehrmacht)