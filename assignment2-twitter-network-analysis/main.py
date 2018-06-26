#!/bin/python

# http://www.nirg.net/using-tweepy.html

from tweepy import *
import step2
import step3
import step4
import json_utils
import twitter_followers
import snap

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

step4.run('merged-graph', screen_names)

################
#    step 6    #
################

# used the below cli command to get the number of nodes and edges for the merged graph
# source for the grapninfo.gvpr script =>
# https://stackoverflow.com/questions/28079686/graphviz-given-a-dot-file-how-to-compute-node-statistics
# gvpr -f graphinfo.gvpr step4-merged-graphvis.gv => There are 4521 nodes and 4552 edges in merged

################
#    step 7    #
################

#build snappy graph













