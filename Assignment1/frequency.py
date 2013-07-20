import sys
import json

def hw(tweet_file):
    wordl = []
    word_dict = {}
    for tweet_line in tweet_file:
        try:
            tweet = json.loads(tweet_line)
            tweettxt = tweet["text"]
            words = (tweettxt
# .replace('\n', ' ')
# .replace(',', ' ')
# .replace('.', ' ')
# .replace(':', ' ')
# .replace('@', ' ')
# .replace('#', ' ')
            .split())
            wordl.extend(words)
        except(KeyError):
            pass

    total_words = len(wordl)
    #iterate through words and count word frequency in word_dict
    for word in wordl:
        if word.strip() != "":
            try:
                word_dict[word.strip()] += 1
            except(KeyError):
                word_dict[word.strip()] = 1

    #go through word_dict and print word frequency
    #divided by total number of words
    for term, frequency in word_dict.iteritems():
        try:
            print term.encode('utf-8'), float(frequency) / float(total_words)
        except(UnicodeDecodeError):
            pass





def main():
    """run main program"""
    tweetf = open(sys.argv[1])
    hw(tweetf)

if __name__ == '__main__':
    main()

