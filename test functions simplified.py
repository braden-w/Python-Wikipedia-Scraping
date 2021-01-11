import wikipediaapi
from collections import deque
import networkx as nx
import pprint
import matplotlib.pyplot as plt


def test_wikipedia(start_page, end_page, graph, language="en"):
    wikipedia = wikipediaapi.Wikipedia(language)
    start_page_object = wikipedia.page(start_page)
    queue = deque(
        [
            {
                "node_name": start_page,
                "node_object": start_page_object,
                "node_parent": None,
            }
        ]
    )
    return recurse_until_path(start_page, end_page, queue, graph)


def recurse_until_path(start_page, end_page, queue, graph):
    counter = 0
    while queue[0]["node_name"] != end_page:
        generate_node_with_children(queue.popleft(), queue, graph)
        # view_nodes_edges()
        nx.draw(
            graph, pos=nx.spring_layout(graph), with_labels=True, font_weight="bold"
        )
        plt.savefig("picture" + str(counter) + ".png")
        counter += 1

    pprint.pprint(queue[0])
    generate_node_with_children(queue.popleft(), queue, graph)
    return nx.shortest_path(graph, source=start_page, target=end_page)


def generate_node_with_children(
    node: {"node_name": str, "node_object": object, "node_parent": object},
    queue,
    graph,
):
    children = [
        {
            "node_name": child_name,
            "node_object": child_object,
            "node_parent": node["node_name"],
        }
        for child_name, child_object in node["node_object"].links.items()
    ]
    # pprint.pprint(children)
    if node["node_parent"] is not None:
        graph.add_edge(str(node["node_name"]), str(node["node_parent"]))
    queue.extend(children)


G = nx.DiGraph()
print(test_wikipedia("Feyerabend", "Germany", G))
# 11th Infantry Division (Wehrmacht)