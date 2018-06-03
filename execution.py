
# coding: utf-8

# In[9]:


from tweets import Tweets
from morphological_analysis_and_modeling import MorphologicalAnalysisAndModeling


def posting_most_similar_words_on_Twitter():
    
    # インスタンスの生成
    tw = Tweets()
    maam = MorphologicalAnalysisAndModeling()

    # 検索ワードかつ類似度判定の基準となる単語を入力する
    search_word = input("検索ワードを入力してください >>> ")
    
    # search　wordでTwitterを検索する。２００ツイートを取得しリストtweet listにまとめる。
    tweet_list = tw.get_tweet_by_search(search_word = search_word, count = 200)
    
    # MeCabで上記の２００ツイートtweet listの形態素解析を行い、結果をリストresultsに出力する。
    results = maam.mecab(tweet_list)
    
    # Word2vecで形態素解析の結果をモデル化
    model = maam.word2vec(results)
    
    # モデルの中でsearch wordと類似した言葉を出力し、体裁を整えて文字列にする。
    words = ''
    for i in model.wv.most_similar(positive=[search_word]):
        words += str(i)[1:-20]
    words = words.replace("'", "")
    
    text = '{}と近い言葉は、{}'.format(search_word, words)
    
    # 上記の文字列をTwitterに投稿する。
    tw.posting_on_twitter(text=text)


if __name__ == "__main__":
    posting_most_similar_words_on_Twitter()

