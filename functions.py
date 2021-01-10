import wikipediaapi

import networkx as nx

G = nx.Graph()

def generate_links(page_name, language="en"):
    # page_name is a page name, not a URL

    wiki_wiki = wikipediaapi.Wikipedia(language)
    page = wiki_wiki.page(page_name)
    links = page.links
    print(links.keys())
    return links.keys()


def from_a_to_b(a, b, path=[]):
    G.add_nodes(generate_links(a))
            from_a_to_b(generate_links(key), b, path + list(key))



generate_links("Germany")