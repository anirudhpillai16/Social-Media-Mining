import json
import re
import string
import sys


def getTeam(s):
    if s == 'rcb':
        return ['rcb', 'challenger', 'royal challengers', 'royal challengers bangalore', '#royalchallengersbangalore',
                'bangalore']
    elif s == 'kkr':
        return ['kkr', 'rider', 'knight riders', 'kolkata knight riders', '#kolkataknightriders', 'kolkata']
    elif s == 'mi':
        return ['mi', 'indian', 'mumbai indians', '#mumbaiindians', 'mumbai']
    elif s == 'dd':
        return ['dd', 'daredevil', 'delhi daredevils', '#delhidaredevils', 'delhi']
    elif s == 'srh':
        return ['srh', 'sunriser', 'sunrisers hyderabad', 'hyderabad']
    elif s == 'gl':
        return ['gl', 'lion', 'gujaratlions', 'gujarat lions', 'rajkot']
    elif s == 'kxip':
        return ['kxip', 'king', 'punjab', 'mohali', 'nagpur']
    elif s == 'rps':
        return ['rps', 'giant', 'supergiants', 'risingpunesupergiants', 'pune']


def processTweet(tweet):

    tweet = tweet.lower().encode('utf-8')
    # Remove any URL's
    tweet = re.sub('(http.*$)', '', tweet)
    tweet = re.sub(r'([^\s]+).com([^\s]+)', r'', tweet)
    # Remove #word
    tweet = re.sub(r'#([^\s]+)', r'', tweet)
    # Remove @word
    tweet = re.sub(r'@([^\s]+)', r'', tweet)
    # Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    # trim
    tweet = tweet.strip('\'"')
    return tweet


def getStopWordList():
    stopwords = []
    fp = open("resources/stopwords.txt", 'r')
    line = fp.readline()
    while line:
        word = line.strip()
        stopwords.append(word)
        line = fp.readline()
    fp.close()
    stopwords.append(list(string.punctuation))
    return stopwords


def removeStopWords(tweet):
    stopwords = getStopWordList()
    featureVector = []
    words = splitWordsAsTokens(tweet)
    for word in words:
        # check if the word starts with an alphabet
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", word)
        # ignore if its in stop words
        if word in stopwords or val is None:
            continue
        else:
            featureVector.append(word)
    return featureVector


# --------------- Conditional tokenize ------------------------------------------------------------#

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)


def tokenize(s):
    return tokens_re.findall(s)


def splitWordsAsTokens(tweets, lowercase=False):
    tokens = tokenize(tweets)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens


# ---------------------------------------------- Conditional tokenize End ----------------------------------------#

def main(argv):
    flag = True
    team = getTeam(argv[0])
    if len(argv) == 0:
        flag = True
    with open("resources/ipl_tweets.json") as datafile:
        data = json.load(datafile)

    each_tweet = [x['text'] for x in data]

    for x in range(len(each_tweet)):
        tweets = str(each_tweet[x])
        for citation in team:
            if citation in tweets:
                flag = True
        if flag:
            preProcessedTweet = processTweet(tweets)
            preProcessedTweet = removeStopWords(preProcessedTweet)
            f = open('resources/cleaned_tweets.txt', 'a')
            for word in preProcessedTweet:
                f.write(word + " ")
            f.write("\n")
            f.close()
            flag = False
            print(preProcessedTweet)
            print(tweets)


if __name__ == '__main__':
    main(sys.argv[1:])
