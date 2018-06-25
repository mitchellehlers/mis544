#!/bin/python

# http://www.nirg.net/using-tweepy.html

from tweepy import *
import step2
import step3
import step4
import json_utils
import twitter_followers

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = API(auth, wait_on_rate_limit=True)

################
#    step 2    #
################

# EhlersMitchell FranzRinkleff PrasanthVijay75 iowastateu
screen_names = ['iowastateu', 'EhlersMitchell', 'FranzRinkleff', 'PrasanthVijay75']
# step2.run(screen_names, api)

################
#    step 3    #
################

# step3.run('iowastateu')
# step3.run('EhlersMitchell')
# step3.run('FranzRinkleff')
# step3.run('PrasanthVijay75')

################
#  step 4 -5   #
################

step4.run('merged', screen_names)

################
#    step 6    #
################
















