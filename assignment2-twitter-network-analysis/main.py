#!/bin/python

# http://www.nirg.net/using-tweepy.html

from tweepy import *
import step2
import step3
import step4
import step7
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

#step4.run('merged-graph', screen_names)

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

step7.run("step4/merged-graph.json")

# snap graph clustering coefficient
# nodes count = 4521
# edges count = 4550
# Clustering coefficient: 0.000221
# Clustering coefficient is low. This indicates a very low probability two of a users followers share
# the same follower. I my opinion this is low because myself and my team members are not heavy Twitter users.
# So we don't have many followers, limiting the chance our networks would share many edges.
# https://snap.stanford.edu/snappy/doc/reference/GetClustCf.html
# https://networkscience.wordpress.com/2013/09/08/defining-the-clustering-coefficient/

################
#    step 8    #
################














