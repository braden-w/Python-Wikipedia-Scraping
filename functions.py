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
        self.current_parent = start_page
        self.queue = deque([(start_page, start_page)])
        self.recurse_until_path()

    def recurse_until_path(self):
        while self.queue[0][0] != self.end_page:
            self.generate_node_with_children(self.queue.popleft())
            # self.view_nodes_edges()
        self.generate_node_with_children(self.queue.popleft())
        print(nx.shortest_path(self, source=self.start_page, target=self.end_page))
        # nx.draw(self, with_labels=True)
        # plt.show()
        return nx.shortest_path(self, source=self.start_page, target=self.end_page)

    def generate_node_with_children(self, node):
        children = [
            (node_child, node[0])
            for node_child in self.wikipedia.page(node).links.keys()
        ]
        # print(children)
        self.add_node(node[0])
        self.add_edge(node[1], node[0])
        self.queue.extend(children)
        # print(self.queue)

    def view_nodes_edges(self):
        # print(list(self.nodes), list(self.edges))
        print(self.nodes.data())


G = Graph("Germany", "Abkhazia")