import json

from textblob import TextBlob
from tweepy.streaming import StreamListener

from fileUtils import *


def get_positive_and_negative_tweets(api, user_id, max_count):
    positive_tweets = []
    negative_tweets = []
    attempts = 0

    while len(positive_tweets) < max_count:
        tweets = api.user_timeline(id=user_id, count=500)
        tweets_sentiments = get_tweets_sentiment(tweets)

        positive = list(filter(lambda tweet: tweet['sentiment'] == 'positive', tweets_sentiments))
        positive_tweets = positive_tweets + positive

        negative = list(filter(lambda tweet: tweet['sentiment'] == 'negative', tweets_sentiments))
        negative_tweets = negative_tweets + negative

        attempts += 1

        if attempts >= max_count:
            break

    return positive_tweets[-100:], negative_tweets[-100:]


def get_tweets_sentiment(tweets):
    results = []

    for tweet in tweets:
        sentiment = get_tweet_sentiment(tweet._json['text'])

        name_sentiment = {}
        name_sentiment['screen_name'] = tweet.author._json['screen_name']
        name_sentiment['text'] = tweet._json['text']
        name_sentiment['sentiment'] = sentiment[0]
        name_sentiment['polarity'] = sentiment[1]
        results.append(name_sentiment)

    return results


def get_tweet_sentiment(tweet):
    analysis = TextBlob(tweet)
    sentiment_value = analysis.sentiment.polarity

    if sentiment_value > 0:
        return 'positive', sentiment_value
    elif sentiment_value < 0:
        return 'negative', sentiment_value
    else:
        return 'neutral', sentiment_value


def twitter_stream(stream, term, count=1):
    # Get a sample of the public data following through Twitter
    iterator = stream.statuses.filter(track=term, language="en")

    tweet_count = count
    for tweet in iterator:
        tweet_count -= 1
        # Twitter Python Tool wraps the data returned by Twitter
        # as a TwitterDictResponse object.
        # We convert it back to the JSON format to print/score
        print(json.dumps(tweet))

        # The command below will do pretty printing for JSON data, try it out
        # print json.dumps(tweet, indent=4)

        if tweet_count <= 0:
            break
    return


class Listener(StreamListener):
    fileName = "results/step4/step4.txt"
    counter = 0
    limit = 10
    file = open(fileName, "w", encoding='utf-8')

    def on_data(self, data):
        self.counter += 1
        tweet_json = json.loads(data.encode('utf-8', 'ignore'))
        print(tweet_json)
        self.file.write(tweet_json["text"] + "\r\n")

        if self.counter < self.limit:
            return True
        else:
            self.file.close()
            return False

    def on_error(self, status):
        print("ERROR ==> " + status)
        self.file.close()

    def on_timeout(self):
        print('Timeout...')
        return True  # To continue listening
