import wikipediaapi

import networkx as nx


class Graph(nx.Graph):
    def __init__(self, page_name, language="en"):
        super().init()
        self.page_name = page_name
        self.language = language

    # def from_a_to_b(a, b, path=[]):
    #     self.G.add_nodes(generate_edges_by_one_step(a))
    #         from_a_to_b(generate_edges_by_one_step(key), b, path + list(key))
    def generate_edges_by_one_step(page_name, language="en"):
        # page_name is a page name, not a URL

        wiki_wiki = wikipediaapi.Wikipedia(language)
        page = wiki_wiki.page(page_name)
        links = page.links
        print(links.keys())
        return links.keys()


# G = Graph()
# G.add_nodes(1, 2)

G = Graph()
G.add_node(1)
print(list(G.nodes), list(G.edges))
print(G.number_of_nodes())
# generate_edges_by_one_step("Germany")