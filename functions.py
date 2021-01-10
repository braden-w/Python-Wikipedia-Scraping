import wikipediaapi

import networkx as nx


class Graph(nx.Graph):
    def __init__(self, initial_page_name, language="en"):
        super().__init__()
        self.page = wikipediaapi.Wikipedia(language).page(initial_page_name)

    # def from_a_to_b(a, b, path=[]):
    #     self.G.add_nodes(generate_edges_by_one_step(a))
    #         from_a_to_b(generate_edges_by_one_step(key), b, path + list(key))
    def generate_edges_by_one_step(
        self,
    ):
        # page_name is a page name, not a URL
        links = page.links
        print(links.keys())
        return links.keys()


# G = Graph()
# G.add_nodes(1, 2)

G = Graph("Germany")
G.add_node(1)
print(list(G.nodes), list(G.edges))
print(G.number_of_nodes())
# generate_edges_by_one_step("Germany")