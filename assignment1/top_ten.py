import sys
import json

def lines(fp):
  print str(len(fp.readlines()))

def GetTweets(fp):
  tweets = []
  for line in fp.readlines():
    tweet = json.loads(line)
    try:
      tweets.append(tweet['text'])
    except:
      continue
  return tweets

def ParseTweets(tweets):
  tags = {}
  for tweet in tweets:
    tweet = ' '.join(tweet.split())
    for word in tweet.split():
      if word[0] == '#':
        word = word[1:]
        try:
          tags[word] += 1
        except:
          tags[word] = 1

  return tags

def main():
  tweet_file = open(sys.argv[1])
  #lines(sent_file)
  #lines(tweet_file)

  tweets = GetTweets(tweet_file)
  tags = ParseTweets(tweets)

  count = 0
  for tag in sorted(tags, key=tags.get, reverse=True):
    count += 1
    encoded_tag = tag.encode('utf-8')
    print encoded_tag, float(tags[tag])
    if count == 10:
      break

if __name__ == '__main__':
  main()
