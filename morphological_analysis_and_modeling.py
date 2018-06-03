
# coding: utf-8

# In[32]:


import MeCab
import sys
from gensim.models import word2vec


# In[120]:


class MorphologicalAnalysisAndModeling:
    
    # MeCabによって与えられたリストを形態素解析する。
    def mecab(self, tweet_list):
        global results
        
        # 新しい辞書を利用するため、引数にパスを指定する。
        m = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd') 
        
        results = []
        words = []
        
        # リスト内の各要素(各ツイート)に形態素解析を実行する。
        # 品詞が名詞、動詞、形容詞であるもののみを抽出し、リストに入れる。
        for sentence in tweet_list:
            sentence = sentence.strip()
            for token in m.parse(sentence).splitlines()[:-1]:
                (surface, feature) = token.split('\t')[0], token.split('\t')[1]
                if feature.startswith('名詞') or feature.startswith('動詞') or feature.startswith('形容詞'):
                    words.append(surface)
        rl = (" ".join(words)).strip()
        results.append(rl)
        return results
        
    # word2vecで形態素解析の結果をモデル化する。
    def word2vec(self, results):
        wakachigaki_file = "Twitter_search_result.wakachi"
        with open(wakachigaki_file, 'w',encoding='utf-8') as fp:
            fp.write("\n".join(results))
                
        data = word2vec.LineSentence(wakachigaki_file)
        model = word2vec.Word2Vec(data,size=200, window=10, hs = 1, min_count =2, sg = 1)
        model.save('Twitter_search_result.model')
            
        return model
            

