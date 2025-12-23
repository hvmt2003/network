import urllib.request
import json

url = input("Enter location: ")
print("Retrieving", url)

data = urllib.request.urlopen(url).read()
print("Retrieved", len(data), "characters")

info = json.loads(data)

total = 0
for item in info['comments']:
    total += item['count']

print("Count:", len(info['comments']))
print("Sum:", total)
