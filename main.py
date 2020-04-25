from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

class_data = []
try:
    html = urlopen("https://webscraper.io/test-sites/e-commerce/allinone/computers")
    bsObject = BeautifulSoup(html.read(), features='xml')
    class_data = bsObject.find("div", {"class":"thumbnail"}).descendants

except HTTPError as e:
    print("Error parsing the URL")

except URLError as e:
    print("Server not found")

for i in class_data:
    print(i)
