#!/bin/python

# http://www.nirg.net/using-tweepy.html

from tweepy import *
import step2
import step3

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
# screen_names = ['iowastateu', 'EhlersMitchell', 'FranzRinkleff', 'PrasanthVijay75']
# step2.run(screen_names, api)

################
#    step 3    #
################

step3.generate_graphvis_pdf('iowastateu')
step3.generate_graphvis_pdf('EhlersMitchell')
step3.generate_graphvis_pdf('FranzRinkleff')
step3.generate_graphvis_pdf('PrasanthVijay75')














