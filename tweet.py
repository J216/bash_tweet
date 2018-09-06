import sys
from os.path import expanduser
sys.path.append(expanduser('~/.tweet/'))

import TwitterAPI as ta
from tweetkey import *


def tweet(message):
    api = ta.TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
    r = api.request('statuses/update', {'status': message})
    print(r.status_code+'\n'+consumer_key)
    return 'SUCCESS' if r.status_code == 200 else 'FAILURE'

def tweetImage(message,image_file):
    api = ta.TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
    file = open(image_file, 'rb')
    data = file.read()
    r = api.request('statuses/update_with_media', {'status':message}, {'media[]':data})
    return 'SUCCESS' if r.status_code == 200 else 'FAILURE'

def main():
    if len(sys.argv) == 2:
        print("Tweet Status")
        print(tweet(sys.argv[1]))
    elif len(sys.argv) == 3:
        print("Tweet Image")
        print(tweetImage(sys.argv[1], sys.argv[2]))


if __name__ == "__main__":
    main()
