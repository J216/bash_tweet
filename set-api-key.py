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
    atk_in = raw_input('Enter your Access Token Key:')
    ats_in = raw_input('Enter your Access Token Secret:')
    ck_in = raw_input('Enter your Consumer Key:')
    cs_in = raw_input('Enter your Consumer Secret:')
    if len(atk_in) < 6 or len(ats_in) < 6 or len(ck_in) < 6 or len(cs_in) < 6 :
        print("Setting TwitterAPI key failed. \nVerify your key is correct and run `python set-api-key.py` try again.")
        SET_KEY = 'print("Setting TwitterAPI key failed. \nVerify your key is correct and run `python set-api-key.py` try again.")'
        if not os.path.exists(os.path.expanduser('~/.tweet/tweetkey.py')):
            try:
                os.mkdir(os.path.expanduser('~/.tweet/'))
                f = open(os.path.expanduser('~/.tweet/tweetkey.py'), "w")
                f.write(SET_KEY)
                f.close()
            except:
                print('Failed to write error file.')
    else:
        SET_KEY = BLANK_KEY.replace('ATK',atk_in).replace('ATS',ats_in).replace('CK',ck_in).replace('CS',cs_in)
        try:
            if not os.path.exists(os.path.expanduser('~/.tweet/')):
                os.mkdir(os.path.expanduser('~/.tweet/'))
            f = open(os.path.expanduser('~/.tweet/tweetkey.py'), "w")
            f.write(SET_KEY)
            f.close()
            print('API key written successfully')
        except:
            print('Failed to write file')

print('Twitter API Key Setup')
existing_key = raw_input('Do you currently have a Twitter API key? (Yes/No)')
if 'Y' in existing_key or 'y' in existing_key:
    set_keys()
else:
    existing_key = raw_input('Would you like to open the Twitter page to obtain an API key in your browser? (Yes/No)')
    if 'Y' in existing_key or 'y' in existing_key:
        webbrowser.open("https://stackoverflow.com/questions/1808855/getting-new-twitter-api-consumer-and-secret-keys")

