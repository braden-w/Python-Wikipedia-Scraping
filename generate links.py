from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen


def generate_links(url):
    website_html = urlopen(url)
    links = BeautifulSoup(website_html, parse_only=SoupStrainer('a'))
    print([link['href'] for link in links if link.has_attr('href')])


generate_links("https://www.wikipedia.com/en/Adolf_Hitler")
