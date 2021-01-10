import wikipediaapi


def generate_links(page_name, language="en"):
    # page_name is a page name, not a URL

    wiki_wiki = wikipediaapi.Wikipedia(language)
    page = wiki_wiki.page(page_name)
    links = page.links
    print(links.keys())
    return links.keys()


def from_a_to_b(a, b, path=[]):
    if b in a:
        return path + b
    else:
        for key in a:
            from_a_to_b(generate_links(key), b, path + list(key))


generate_links("Germany")