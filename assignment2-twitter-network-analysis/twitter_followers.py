from tweepy import *
import time
import json_utils

from date_utils import *


def build_graph_of_followers(tweepy_api, node_screen_name):

    graph = {}
    followers = []

    max_count = 200
    max_graph_size = 100
    users = Cursor(tweepy_api.followers, screen_name=node_screen_name).items(max_count)

    for count in range(0, max_count):
        try:
            followers.append(next(users))
            if len(followers) == max_graph_size:
                break
        except TweepError as ex:
            if "Not authorized" in str(ex.message):
                print("Not authorized skipping user")
                break
            else:
                print "TweepError ... sleeping 10 min : %s" % ex.message
                time.sleep(60*10)
                followers.append(next(users))
        except StopIteration:
            break

    followers_names = list()
    for follower in followers:
        followers_names.append(str(follower.screen_name))

    graph[node_screen_name] = followers_names

    return graph


def build_graph_of_followers_followers(tweepy_api, followers_screen_names, json_file):

    follower_graph = {}
    for screen_name in followers_screen_names:
        print(get_current_time_as_str()+" "+screen_name+" adding followers")
        next_graph = build_graph_of_followers(tweepy_api, screen_name)

        if len(next_graph) > 0:
            follower_graph = merge_two_graphs(follower_graph, next_graph)

            json_utils.append(json_file, follower_graph)

            print(get_current_time_as_str()+" "+screen_name+" "+str(len(follower_graph[screen_name]))
                  + " followers added sleeping for 5 sec ...")
        else:
            print(get_current_time_as_str()+" "+screen_name+" did not add user, they had zero followers. "
                                                            "sleeping for 5 sec ...")

        time.sleep(5*60)

    return follower_graph


def merge_two_graphs(x, y):
    z = x.copy()
    z.update(y)
    return z

