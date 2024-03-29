"""find the happiest state in US"""
import sys
import json
import csv
import bz2

def get_sent(sentdict, tweettext):
    """get sentiment value according to sent_file dictionary"""
    sent_value = 0
    word_list = (tweettext
            .replace('\n', '')
            .replace(',', '')
            .replace('.', '')
            .rsplit(' '))
    for word in word_list:
        try:
            sent_value = sent_value + sentdict[word]
        except(KeyError):
            pass

    return sent_value

def parse_sent(sent_file):
    """returned dictionary of term and sentiment score"""
    sentdict = {}
    for sent_line in sent_file:
        sent_item = sent_line.replace('\n', '').rsplit('\t')
        sentdict[sent_item[0]] = float(sent_item[1])
    
    return sentdict

def hw(sent_file, tweet_file):
    """find out the happiest state"""
    sentdict = parse_sent(sent_file)
    state_happiness = {}

    for tweet_line in tweet_file:
        try:
            tweet = json.loads(tweet_line)
            try:
                place = tweet["place"]
                if (place["country_code"] == "US" and
                    place["place_type"] == "city" and
                    len(place["full_name"].split().pop()) == 2):
                    tweettext = tweet["text"]
                    sentiment = get_sent(sentdict, tweettext)
                    tweet_state = place["full_name"].split().pop()
                    try:
                        state_happiness[tweet_state].append(sentiment)
                    except(KeyError):
                        state_happiness[tweet_state] = [sentiment]
            except(KeyError, TypeError):
                pass
        except(KeyError):
            pass
    happiest_state = ""
    for state, array in state_happiness.iteritems():
        state_happiness[state] = sum(array)/float(len(array))
        try:
            if state_happiness[state] > state_happiness[happiest_state]:
                happiest_state = state
        except(KeyError):
            happiest_state = state

    print happiest_state


def main():
    """run main program"""
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
# lines(sent_file)
# lines(tweet_file)

if __name__ == '__main__':
    main()