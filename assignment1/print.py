import urllib
import json

for page in range(1,11):
  response = json.load(urllib.urlopen("http://search.twitter.com/search.json?q=microsoft&page="+str(page)))
  results = response['results']
  for tweet in results:
    print tweet['text']
