from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

try:
    html = urlopen("https://webscraper.io/test-sites/e-commerce/allinone/computers")
    bsObject = BeautifulSoup(html.read(), features='xml')
    # class_data = bsObject.find("div", {"class": "sidebar-nav navbar-collapse"}).descendants

    for i in bsObject.findAll("p", {"class": "description"}):
        print(i)

except HTTPError as e:
    print("Error parsing the URL")

except URLError as e:
    print("Server not found")




