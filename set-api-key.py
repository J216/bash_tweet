import os
import webbrowser

BLANK_KEY="""
access_token_key = 'ATK'
access_token_secret = 'ATS'
consumer_key = 'CK'
consumer_secret = 'CS'
default_tweet = 'DT'
hashtags = 'HT'
"""

def set_keys():
    atk_in = input('Enter your Access Token Key:')
    ats_in = input('Enter your Access Token Secret:')
    ck_in = input('Enter your Consumer Key:')
    cs_in = input('Enter your Consumer Secret:')
    SET_KEY = BLANK_KEY.replace('ATK',atk_in).replace('ATS',ats_in).replace('CK',ck_in).replace('CS',cs_in)
    try:
        if not os.path.exists(os.path.expanduser('~/.tweet/')):
            os.mkdir(os.path.expanduser('~/.tweet/'))
        f = open(os.path.expanduser('~/.tweet/tweetkey.py), "w")
        f.write(SET_KEY)
        f.close()
        print('API key written successfully')
    except:
        print('Failed to write file')

print('Twitter API Key Setup')
existing_key = input('Do you currently have a Twitter API key? (Yes/No)')
if 'Y' in existing_key or 'y' in existing_key:
    set_keys()
else:
    existing_key = input('Would you like to open the Twitter page to obtain an API key in your browser? (Yes/No)')
    if 'Y' in existing_key or 'y' in existing_key:
        webbrowser.open("https://xkcd.com/353/")

