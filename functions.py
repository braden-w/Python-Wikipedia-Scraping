import wikipediaapi
import cProfile as profile
from collections import deque
import networkx as nx


class Graph(nx.Graph):
    def __init__(self, start_page, end_page, language="en"):
        super().__init__()
        # initializes Wikipedia is specified language (since the language is constant as pages change)
        self.wikipedia = wikipediaapi.Wikipedia(language)
        self.start_page = start_page
        self.end_page = end_page
        self.current_parent = start_page
        self.queue = deque([self.start_page])
        profile.runctx("self.recurse_until_path()", globals(), locals())
        # self.recurse_until_path()

    def recurse_until_path(self):
        while self.queue[0] != self.end_page:
            self.generate_node_with_children(self.queue.popleft())
            # self.view_nodes_edges()
        self.generate_node_with_children(self.queue.popleft())
        return nx.shortest_path(self, source=self.start_page, target=self.end_page)

    def generate_node_with_children(self, node):
        try:
            self.current_parent = node["change_current_parent_to"]
        except:
            children = self.wikipedia.page(node).links.keys()
            # print(children)
            self.add_node(node)
            self.add_edge(self.current_parent, node)
            self.queue.append({"change_current_parent_to": node})
            self.queue.extend(children)
        # print(self.queue)

    def view_nodes_edges(self):
        print(list(self.nodes), list(self.edges))
        # print(self.nodes.data())


G = Graph("Feyerabend", "11th Infantry Division (Wehrmacht)")