#!/bin/python

from tweepy import *
import step2
import step3
import step4
import step7
import step8

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

# this takes a very long time to run due to Twitter api throttle limits.
# you can only make 180 request per 15min. Due to this IowaState took ~24 hours to get all the followers
# This code is commented out for this reason, we save all the data in json files using a Python Dictionary
# as a adjacency list, and these files are used to every other step. Commenting step2 for this reason.

# step2.run(screen_names, api)

################
#    step 3    #
################

step3.run('iowastateu')
step3.run('EhlersMitchell')
step3.run('FranzRinkleff')
step3.run('PrasanthVijay75')

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

snap_graph = step7.run("step4/merged-graph.json")

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

step8.run(snap_graph)

# Top 10 page ranks from the merged graph =>
# JJMovingForward 0.000442008655522
# SportsNewsBk 0.000404251820609
# sarah_zavoral 0.000402678619155
# irenegarcia73 0.00031095700719
# KevinKemp6 0.00027985873605
# softwaremperor 0.00026430960048
# Wilson_IBMCloud 0.000263916300117
# Bluejstudio1 0.000254980119138
# pmpautzke 0.00024876046491
# phightinphils 0.00023839437453

# x <= y (what I mean by this is y follows x), a => b (this means a follows b)
# EhlersMitchell <= sarah_zavoral => cyclonedaily <= ncarlone2 => iowastateu
#
# I also found a path including both of you to iowastateu ...
# iowastateu => sjhlfc => jasonagastrich <= virginiaemartin <= AmoursHideous <= Wilson_IBMCloud <= FranzRinkleff => PrasanthVijay75















