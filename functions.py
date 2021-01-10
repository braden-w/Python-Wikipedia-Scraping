import wikipediaapi

import networkx as nx

class Graph:
    def __init__(self):
        self.G = nx.Graph()
    def from_a_to_b(a, b, path=[]):
        self.G.add_nodes(generate_edges_by_one_step(a))
            from_a_to_b(generate_edges_by_one_step(key), b, path + list(key))
    def generate_edges_by_one_step(page_name, language="en"):
        # page_name is a page name, not a URL

        wiki_wiki = wikipediaapi.Wikipedia(language)
        page = wiki_wiki.page(page_name)
        links = page.links
        print(links.keys())
        return links.keys()





generate_edges_by_one_step("Germany")