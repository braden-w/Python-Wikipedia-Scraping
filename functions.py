import wikipediaapi
import cProfile as profile
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
import asyncio


class Graph(nx.DiGraph):
    def __init__(self, start_page: str, end_page: str, language: str = "en"):
        super().__init__()
        # initializes Wikipedia is specified language (since the language is constant as pages change)
        self.wikipedia = wikipediaapi.Wikipedia(language)
        start_page_object = self.wikipedia.page(start_page)
        self.start_page = start_page
        self.end_page = end_page
        self.image_counter = 0
        self.done = False
        self.queue = deque(
            [
                {
                    "node_name": start_page,
                    "node_object": start_page_object,
                    "node_parent": None,
                }
            ]
        )

    async def recurse_until_path(self):
        while self.done == False:
            await asyncio.gather(
                *(self.process_first_queue(node) for node in self.queue)
            )
            self.queue.clear()
            # self.write_graph()
        self.create_graph()
        return nx.shortest_path(self, source=self.start_page, target=self.end_page)

    async def process_first_queue(self):
        current_node = self.queue.popleft()
        self.link_node_to_parent(current_node)
        self.add_children_to_queue(
            await self.generate_children_from_node(current_node),
            current_node["node_name"],
        )
        if current_node["node_name"] == self.end_page:
            self.done = True

    def link_node_to_parent(
        self, node: {"node_name": str, "node_object": object, "node_parent": str}
    ):
        if node["node_parent"] is not None:
            self.add_edge(node["node_parent"], node["node_name"])

    def add_children_to_queue(self, children, parent):
        children_payload = [
            {
                "node_name": child_name,
                "node_object": child_object,
                "node_parent": parent,
            }
            for (child_name, child_object) in children
        ]
        self.queue.extend(children_payload)

    async def generate_children_from_node(
        self, node: {"node_name": str, "node_object": object, "node_parent": str}
    ):
        def generate_links(node):
            return node["node_object"].links

        loop = asyncio.get_event_loop()

        links = await loop.run_in_executor(None, generate_links, node)
        return links.items()

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
print(asyncio.run(G.recurse_until_path()))
# Feyerabend
# 18th-century history of Germany
# 11th Infantry Division (Wehrmacht)