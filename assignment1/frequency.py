import sys
import json
import unicodedata

tbl = dict.fromkeys(i for i in xrange(sys.maxunicode) if unicodedata.category(unichr(i)).startswith('P'))
def removePunctuation(text):
  return text.translate(tbl)

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

def GetTermFrequency(tweets):
  termCount = {}
  for tweet in tweets:
    tweet = ' '.join(tweet.split())
    count = 0
    for term in tweet.split():
      term = removePunctuation(term).lower()
      try:
        termCount[term] += 1
      except:
        termCount[term] = 1

  tot = 0
  for term in termCount:
    tot += termCount[term]

  for term in sorted(termCount, key=termCount.get, reverse=True):
    encoded_term = term.encode('utf-8')
    print encoded_term, float(termCount[term])/float(tot)

def main():
  tweet_file = open(sys.argv[1])
  #lines(tweet_file)

  tweets = GetTweets(tweet_file)
  GetTermFrequency(tweets)

if __name__ == '__main__':
  main()
