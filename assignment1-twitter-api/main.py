#!/bin/python

from tweepy import *

from twitterUtils import *

from classifierUtils import *

from nltk import word_tokenize, pos_tag, ne_chunk

# ######## Useful Links ########
# https://pythonprogramming.net/twitter-api-streaming-tweets-python-tutorial/
# http://veekaybee.github.io/2018/02/19/creating-a-twitter-art-bot/
# https://github.com/tweepy/tweepy
# http://socialmedia-class.org/twittertutorial.html
# ##############################

print("--------- STEP 1-2 ---------\r\n")

# Variables that contains the user credentials to access Twitter API
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

businessEntitiesList = read_business_entities()
print(businessEntitiesList)

api = API(auth)

print("--------------------------\r\n")

# STEP 3) Identify proper user ids (@) corresponding to the following 20 business entities
print("--------- STEP 3 ---------\r\n")

users = []
for term in businessEntitiesList:
    user = api.get_user(term)
    users.append(user)
    print(f"{user.screen_name} userId => {user.id}")

print("--------------------------\r\n")

# STEP 4) 10 real-time public tweets for one of the user ids found in STEP 3
print("--------- STEP 4 ---------\r\n")

userId = users[0].id  # using CNN as there are a lot of live tweets to test with
twitterStream = Stream(auth, Listener())
twitterStream.filter(follow=[f"{userId}"])

print("--------------------------\r\n")

# STEP 5) For each business entity id use the search api to find 100 + and 100 - tweets and write the JSON to a file
print("--------- STEP 5 ---------\r\n")

all_positive_sentiments = []
all_negative_sentiments = []
for user in users:
    tweets_sentiments = get_positive_and_negative_tweets(api=api, user_id=user.id, max_count=100)

    positive = tweets_sentiments[0]
    all_positive_sentiments.append(positive)
    fileName = "results/step5/step5-positive-tweets-" + user.name + "-" + ".json"
    write_json_file(fileName, positive)

    negative = tweets_sentiments[1]
    all_negative_sentiments.append(negative)
    fileName = "results/step5/step5-negative-tweets-" + user.name + "-" + ".json"
    write_json_file(fileName, negative)

    print(user.name + " ... done")

print("--------------------------\r\n")


# STEP 6) For each business entity id use the search api to find 100 + and 100 - tweets and write the JSON to a file
# STEP 7) Find the accuracy, recall, precision, and F-measure
print("--------- STEP 6-7 ---------\r\n")

flat_neg = flatten_list(all_negative_sentiments)
flat_pos = flatten_list(all_positive_sentiments)

prepped_neg = prep_data(flat_neg, "negative")
prepped_pos = prep_data(flat_pos, "positive")

naive_bayes(prepped_neg, prepped_pos)

print("--------------------------\r\n")

print("--------- STEP 8 ---------\r\n")

pos_named_entities = []
neg_named_entities = []

# Positive named entities
for tweet in flat_pos:
    result = ne_chunk(pos_tag(word_tokenize(tweet.get('text'))))
    pos_named_entities.append((tweet.get('screen_name'), str(result)))

# Negative named entities
for tweet in flat_neg:
    result = ne_chunk(pos_tag(word_tokenize(tweet.get('text'))))
    neg_named_entities.append((tweet.get('screen_name'), str(result)))

print("--------------------------\r\n")

print("--------- STEP 9 ---------\r\n")


def print_positive_named_entities_labels():
    pos_label_count = {}
    for entity in pos_named_entities:
        person_count = entity[1].count('PERSON ')
        org_count = entity[1].count('ORGANIZATION ')
        gpe_count = entity[1].count('GPE ')
        if entity[0] in pos_label_count:
            count = pos_label_count.get(entity[0])
            person_count += count[0]
            org_count += count[1]
            gpe_count += count[2]
            pos_label_count[entity[0]] = (person_count, org_count, gpe_count)
        else:
            pos_label_count[entity[0]] = (person_count, org_count, gpe_count)
    print("Positive Named Entities Label Counts:")
    print("screen_name | person | organization | gpe")
    print(pos_label_count)
    file_name = "results/step9/step9-positive-entity-label-counts.json"
    write_json_entity_file(file_name, pos_label_count)


print_positive_named_entities_labels()


def print_negative_named_entities_labels():
    neg_label_count = {}
    for entity in neg_named_entities:
        person_count = entity[1].count('PERSON ')
        org_count = entity[1].count('ORGANIZATION ')
        gpe_count = entity[1].count('GPE ')
        if entity[0] in neg_label_count:
            count = neg_label_count.get(entity[0])
            person_count += count[0]
            org_count += count[1]
            gpe_count += count[2]
            neg_label_count[entity[0]] = (person_count, org_count, gpe_count)
        else:
            neg_label_count[entity[0]] = (person_count, org_count, gpe_count)
    print("Negative Named Entities Label Counts:")
    print("screen_name | person | organization | gpe")
    print(neg_label_count)
    file_name = "results/step9/step9-negative-entity-label-counts.json"
    write_json_entity_file(file_name, neg_label_count)


print_negative_named_entities_labels()

print("--------------------------\r\n")

