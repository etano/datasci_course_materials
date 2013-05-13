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

def ParseTweets(fp,tweets):
  sentiments = {}
  multiWordSentiments = []
  for line in fp.readlines():
    line = line.split()
    sentiment = ' '.join(line[:-1])
    score = int(line[-1])
    sentiments[sentiment] = int(score)
    if len(line) > 2:
      multiWordSentiments.append(sentiment)

  scores = []
  for tweet in tweets:
    tweet = ' '.join(tweet.split())
    score = 0
    for word in tweet.split():
      try:
        score += sentiments[word]
      except:
        continue
    for mws in multiWordSentiments:
      if mws in tweet:
        score += sentiments[mws]
    scores.append(score)

  return scores

def main():
  sent_file = open(sys.argv[1])
  tweet_file = open(sys.argv[2])
  #lines(sent_file)
  #lines(tweet_file)

  tweets = GetTweets(tweet_file)
  scores = ParseTweets(sent_file,tweets)

  for score in scores:
    print score

if __name__ == '__main__':
  main()
