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
  newSentiments = {}
  for tweet in tweets:
    tweet = ' '.join(tweet.split())
    tmpNewSentiments = []
    score = 0
    for word in tweet.split():
      word = removePunctuation(word)
      try:
        score += sentiments[word]
      except:
        tmpNewSentiments.append(word)
    for mws in multiWordSentiments:
      if mws in tweet:
        score += sentiments[mws]
    scores.append(score)

    for newSentiment in tmpNewSentiments:
      try:
        newSentiments[newSentiment][0] += score
        newSentiments[newSentiment][1] += 1
      except:
        newSentiments[newSentiment] = [score,1]

  for newSentiment in newSentiments:
    score = float(newSentiments[newSentiment][0])/float(newSentiments[newSentiment][1])
    newSentiments[newSentiment] = score

  for sentiment in sorted(newSentiments, key=newSentiments.get, reverse=True):
    encoded_sentiment = sentiment.encode('utf-8')
    print encoded_sentiment, newSentiments[sentiment]
  return scores

def main():
  sent_file = open(sys.argv[1])
  tweet_file = open(sys.argv[2])
  #lines(sent_file)
  #lines(tweet_file)

  tweets = GetTweets(tweet_file)
  scores = ParseTweets(sent_file,tweets)

if __name__ == '__main__':
  main()
