# -*- coding:utf-8 -*-
import logging
from gensim.models.word2vec import LineSentence, Word2Vec
import sys
import importlib
import numpy as np
importlib.reload(sys)
'''
对每个句子的所有词向量取均值，生成一个句子的vector
'''
def build_sentence_vector(text,size,imdb_w2v):
    vec = np.zeros(size).reshape((1,size))
    count = 0
    # print(text)
    text=text.split()
    # print (text)
    # print(imdb_w2v['568.572.1608.1613'] )
    # print(imdb_w2v['568.572.1608.1613']+imdb_w2v['568.572.1608.1613'])
    for word in text:
        # print(9)
        try:
            vec += imdb_w2v[word].reshape((1,size))
            # print(10)
            count += 1
            # print(3)
        except KeyError:
            # print(11)
            continue
    if count != 0:
        vec /= count
    return vec
'''
构建待测句子向量
'''
def get_predict_vecs(words):
    n_dim = 100
    imdb_w2v =Word2Vec.load('netA80w2v.mod')
    train_vecs = build_sentence_vector(words,n_dim,imdb_w2v)
    return train_vecs

def trainmodel(filename,modelfile):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences= LineSentence(filename)
    model = Word2Vec(sentences ,min_count=1, iter=1000)
    model.train(sentences, total_examples=model.corpus_count, epochs=1000)
    model.save(modelfile)

def addtrain(filename,modelfile):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = LineSentence(filename)
    model = Word2Vec.load(modelfile)
    model.train(sentences, total_examples=model.corpus_count, epochs=1000)
    model.save(modelfile)
def cos_dist(vec1,vec2):
    """
    :param vec1: 向量1
    :param vec2: 向量2
    :return: 返回两个向量的余弦相似度
    """
    # vec2 = vec2.reshape((100, 1))
    dist1=float(np.dot(vec1,vec2)/(np.linalg.norm(vec1)*np.linalg.norm(vec2)))
    return dist1


#model.save("test_01.model")
#model.wv.save_word2vec_format('test_01.model.txt','test_01.vocab.txt',binary=False)
#model_loaded = Word2Vec.load("netA80w2v.mod")
#model1 = word2vec.load("netA80w2v.mod")



# sim = model1.wv.most_similar(positive=[u'1130.1190.1232.1237'])
# for s in sim:
# #     print( s[0])

if __name__ == "__main__":
    #trainmodel()
    st1 = open('t1.txt', 'r', encoding='UTF-8').read()
    st2 = open('t2.txt', 'r', encoding='UTF-8').read()
    vect1 = get_predict_vecs(st1 )

    # print(vect1)
    # print(vect1.shape)
    vect2 = get_predict_vecs(st2 )

    # print(vect2)
    # print(vect1.shape)
    vect2=vect2.reshape((100, 1))
    # print(np.dot(vect1, vect2))
    # print(np.linalg.norm(vect1))
    print(vect1)
    dis= cos_dist(vect1 ,vect2)
    print(dis)

# trainmodel("out/w2vTrainData1.txt","Trained.mod")
# #训练集目录
# trainset=[]
# for i in range(2,20):
#     trainset.append("out/w2vTrainData"+str(i)+".txt")
# print(trainset)
#
#
# #根据训练集训练w2v模型
# for i in trainset:
#     try:
#         addtrain(i, "Trained.mod")
#     except:
#         print("跳过:",i)
#         continue