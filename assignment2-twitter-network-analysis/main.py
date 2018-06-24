#!/bin/python

# http://www.nirg.net/using-tweepy.html

from tweepy import *
import step2

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = API(auth, wait_on_rate_limit=True)

# EhlersMitchell FranzRinkleff PrasanthVijay75 iowastateu
screen_names = ['PrasanthVijay75']

step2.run(screen_names, api)

step2.get_json_file_name(screen_names[0])

#step 3











