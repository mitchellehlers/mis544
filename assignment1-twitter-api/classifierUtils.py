import collections
import nltk
import nltk.classify.util
from nltk.metrics import *
from nltk.classify import NaiveBayesClassifier

nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def dictionary(tweet):
    return dict([(tweet.get('text'), tweet.get('screen_name'))])


def prep_data(tweets, class_label):
    prepped_data = [(dictionary(tweet), class_label) for tweet in tweets]
    return prepped_data


def get_list_of_text(tweets):
    text_list = [tweet.get('text') for tweet in tweets]
    return text_list


def naive_bayes(negative, positive):
    print(len(negative))
    print(len(positive))

    negcutoff = int(len(negative)*3/4)
    poscutoff = int(len(positive)*3/4)

    train = negative[:negcutoff] + positive[:poscutoff]
    test = negative[negcutoff:] + positive[poscutoff:]
    print('train on %d instances, test on %d instances' % (len(train), len(test)))

    classifier = NaiveBayesClassifier.train(train)
    refsets = collections.defaultdict(set)
    testsets = collections.defaultdict(set)

    print('accuracy:', nltk.classify.util.accuracy(classifier, test))

    for i, (features, label) in enumerate(test):
        refsets[label].add(i)
        observed = classifier.classify(features)
        testsets[observed].add(i)

    print('positive precision:', precision(refsets['positive'], testsets['positive']))
    print('positive recall:', recall(refsets['positive'], testsets['positive']))
    print('positive F-measure:', f_measure(refsets['positive'], testsets['positive']))

    print('negative precision:', precision(refsets['negative'], testsets['negative']))
    print('negative recall:', recall(refsets['negative'], testsets['negative']))
    print('negative F-measure:', f_measure(refsets['negative'], testsets['negative']))

    classifier.show_most_informative_features()

