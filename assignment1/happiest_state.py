import sys
import json

def lines(fp):
  print str(len(fp.readlines()))

def GetStates():
  states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
  stateabbrs = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
  return states,stateabbrs

def VerifyLocation(location,states,stateabbrs):
  locationEstablished = False
  locale = ''
  for i in range(0,len(states)):
    if states[i] in location:
      locale = stateabbrs[i]
      locationEstablished = True
      break
  if not locationEstablished:
    for i in range(0,len(stateabbrs)):
      if stateabbrs[i] in location:
        locale = stateabbrs[i]
        locationEstablished = True
        break
  return locale,locationEstablished

def GetTweets(fp):
  states,stateabbrs = GetStates()

  tweets = []
  for line in fp.readlines():
    data = json.loads(line)
    locationEstablished = False
    try:
      tweet = data['text']

      # Get Location
      locale = ''

      # Try 'place' first
      place = data['place']
      if place != 'None':
        try:
          location = place['full_name']
          locale,locationEstablished = VerifyLocation(location,states,statebbrs)
        except:
          pass

      # Try 'user'/'location' next
      user = data['user']
      location = user['location']
      if location != 'None' and not locationEstablished:
        locale,locationEstablished = VerifyLocation(location,states,stateabbrs)

      if locationEstablished:
        tweets.append([tweet,locale])
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

  scores = {}
  for [tweet,locale] in tweets:
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
    try:
      scores[locale] += score
    except:
      scores[locale] = score

  return scores

def main():
  sent_file = open(sys.argv[1])
  tweet_file = open(sys.argv[2])
  #lines(sent_file)
  #lines(tweet_file)

  tweets = GetTweets(tweet_file)
  scores = ParseTweets(sent_file,tweets)


  locale = sorted(scores, key=scores.get, reverse=True)[0]
  encoded_locale = locale.encode('utf-8')
  print encoded_locale

if __name__ == '__main__':
  main()
