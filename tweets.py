
# coding: utf-8

# In[27]:


from requests_oauthlib import OAuth1Session
import json
import sys
from application_settings import Application_Settings # API key と Access Token


# In[28]:


class Tweets():
    
    def __init__(self):
        api = Application_Settings
        self.session = OAuth1Session(api["Consumer Key (API Key)"], api["Consumer Secret (API Secret)"], api["Access Token"], api["Access Token Secret"])  # 認証処理
    
    # textをtwitterに投稿する関数を定義する。
    def posting_on_twitter(self,text):
        url = "https://api.twitter.com/1.1/statuses/update.json"
        
        if len(text) > 140:
            text = text[0:140]
        
        params = {"status": text}
        req = self.session.post(url, params = params)
        
    # search wordでtwitterを検索し、countの数だけツイートを取得する。
    def get_tweet_by_search(self, search_word, count):
        url = 'https://api.twitter.com/1.1/search/tweets.json'
        res = self.session.get(url, params = {'q':search_word, 'count':count})
        
        # 正常通信出来なかった場合にはエラーを吐き終了する。
        if res.status_code != 200:
            print("Twitter API Error: %d" % res.status_code)
            sys.exit(1)

        res_text = json.loads(res.text)
        tweet_list = []
        for tweet in res_text['statuses']:
            tweet_list.append(tweet['text'])
        
        # ツイートは文面のみをリストに格納する。    
        return tweet_list

