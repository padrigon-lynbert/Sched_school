import urllib
from urllib import request

resp = request.urlopen("https://www.wikipedia.org")
r = resp.read()
# print(r)

html = r.decode("UTF-8")

print(html)