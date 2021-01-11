import wikipediaapi
from collections import deque
import networkx as nx
import pprint


def test_wikipedia(start_page, end_page, graph, language="en"):
    wikipedia = wikipediaapi.Wikipedia(language)
    start_page_object = wikipedia.page(start_page)
    queue = deque(
        [
            {
                "node_name": start_page,
                "node_links_dictionary": start_page_object.links,
                "node_parent": None,
            }
        ]
    )
    return recurse_until_path(start_page, end_page, queue, graph)


def recurse_until_path(start_page, end_page, queue, graph):
    while queue[0]["node_name"] != end_page:
        generate_node_with_children(queue.popleft(), queue, graph)
        # view_nodes_edges()
    pprint.pprint(queue[0])
    generate_node_with_children(queue.popleft(), queue, graph)
    return nx.shortest_path(graph, source=start_page, target=end_page)


def generate_node_with_children(
    node: {"node_name": str, "node_links_dictionary": object, "node_parent": object},
    queue,
    graph,
):
    # pprint.pprint(node["node_links_dictionary"])
    # pprint.pprint([item for item in queue])

    # print(node["node_links_dictionary"])
    children = [
        {
            "node_name": child_name,
            "node_links_dictionary": child_object.links,
            "node_parent": node["node_name"],
        }
        for child_name, child_object in node["node_links_dictionary"].items()
    ]
    # pprint.pprint(children)

    graph.add_node(node["node_name"])
    graph.add_edge(node["node_name"], node["node_parent"])
    queue.extend(children)


G = nx.Graph()
print(test_wikipedia("Feyerabend", "11th Infantry Division (Wehrmacht)", G))
# 11th Infantry Division (Wehrmacht)