import urllib.request
from bs4 import BeautifulSoup

url = "http://py4e-data.dr-chuck.net/known_by_Maram.html"
count = 7
position = 18

for i in range(count):
    print("Retrieving:", url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position - 1].get('href', None)

print("Final URL:", url)
print("Name:", url.split('_')[-1].replace('.html',''))
