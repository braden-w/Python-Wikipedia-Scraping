from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def generate_links(url):
    website = urlopen(url, context=ctx).read()
    links = BeautifulSoup(website, parse_only=SoupStrainer('a'))
    print([link['href'] for link in links if link.has_attr('href')])


generate_links("https://www.wikipedia.org/")
