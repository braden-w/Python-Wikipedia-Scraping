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
    soup = BeautifulSoup(website, "html.parser")
    for link in soup.findAll("a", attrs={"href": re.complie("^http://")}):
        print(link.get("href"))
