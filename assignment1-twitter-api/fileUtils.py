import time
import json


def flatten_list(list):
    flat_list = [item for sublist in list for item in sublist]
    return flat_list


def read_business_entities():
    text_file = open("business-entities.txt", "r")
    lines = text_file.readlines()
    text_file.close()

    # strip newline and white space from each business entity term
    lines = list(map(lambda term: term.strip(), lines))

    return lines


def current_milli_time():
    return str(round(time.time() * 1000))


def write_tweets_to_file(file_name, max_count, tweets):
    # sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
    file = open(file_name, "w", encoding='utf-8')

    for tweet in tweets:
        # print(tweet)
        file.write(tweet)

        max_count -= 1
        if max_count <= 0:
            break

    file.close()


def write_json_file(file_name, data):
    with open(file_name, 'a') as f:
        for tweet in data:
            f.write('\n')
            json.dump(tweet, f)


def write_json_entity_file(file_name, data):
    with open(file_name, 'a') as f:
            f.write('\n')
            json.dump(data, f)


def write_sentiment_to_tsv_file(file_name, tweets_sentiment):
    file = open(file_name, "w", encoding='utf-8')

    headers="screen_name\ttext\tsentiment\tpolarity\n"
    file.write(headers)

    for tweet in tweets_sentiment:
        line = f"{tweet.get('screen_name')}\t{tweet.get('text').encode('utf-8')}" \
               f"\t{tweet.get('sentiment')}\t{tweet.get('polarity')}\n"
        file.write(line)

    file.close()
