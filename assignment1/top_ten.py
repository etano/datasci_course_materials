import sys
import json

def lines(fp):
  print str(len(fp.readlines()))

def GetTags(fp):
  tags = []
  for line in fp.readlines():
    tweet = json.loads(line)
    try:
      for tag in tweet['entities']['hashtags']:
        tags.append(tag['text'])
    except:
      continue
  return tags

def CountTags(tags):
  tagsHist = {}
  for tag in tags:
    try:
      tagsHist[tag] += 1
    except:
      tagsHist[tag] = 1

  return tagsHist

def main():
  tweet_file = open(sys.argv[1])

  tags = GetTags(tweet_file)
  tagsHist = CountTags(tags)

  count = 0
  for tag in sorted(tagsHist, key=tagsHist.get, reverse=True):
    count += 1
    encoded_tag = tag.encode('utf-8')
    print encoded_tag, float(tagsHist[tag])
    if count == 10:
      break

if __name__ == '__main__':
  main()
