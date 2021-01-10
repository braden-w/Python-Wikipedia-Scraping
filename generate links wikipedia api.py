import wikipediaapi


def generate_links(page):
    links = page.links
    for link in links:
        print(link)

        generate_links("")