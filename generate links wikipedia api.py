import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('en')
page_py = wiki_wiki.page('Word')


def generate_links(page):
    links = page.links
    print(links)


generate_links(page_py)