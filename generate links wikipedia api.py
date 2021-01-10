import wikipediaapi

# page_name is a page name, not a URL


def generate_links(page_name, language='en'):
    wiki_wiki = wikipediaapi.Wikipedia(language)
    page = wiki_wiki.page(page_name)
    links = page.links
    print(links.keys())
