# -*- coding:utf-8 -*-
import logging
from gensim.models.word2vec import LineSentence, Word2Vec
import sys
import importlib
import numpy as np
from numpy import array, zeros, full, argmin, inf, ndim
from scipy.spatial.distance import cdist
from math import isinf

importlib.reload(sys)
'''
对每个句子的所有词向量取均值，生成一个句子的vector
'''

def build_sentence_vector(text,size,imdb_w2v):
    vec = np.zeros(size).reshape((1,size))
    senvec=[]
    count = 0
    # print(text)
    text=text.split()
    # print (text)
    # print(imdb_w2v['568.572.1608.1613'] )
    # print(imdb_w2v['568.572.1608.1613']+imdb_w2v['568.572.1608.1613'])
    # print(text)
    for word in text:
        # print(9)
        try:
            vec += imdb_w2v[word].reshape((1,size))
            senvec.append(vec.tolist()[0])
            count += 1
        except KeyError:

            continue
    # if count != 0:
    #     vec /= count
    # print(senvec)
    return senvec
'''
构建待测句子向量
'''
def get_predict_vecs(words):
    # print(words)
    n_dim = 100
    imdb_w2v =Word2Vec.load('Trained1.mod')
    train_vecs = build_sentence_vector(words,n_dim,imdb_w2v)
    # print(train_vecs)
    return train_vecs

def trainmodel(file,outfile):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences= LineSentence(file)
    model = Word2Vec(sentences ,min_count=1, iter=1000)
    model.train(sentences, total_examples=model.corpus_count, epochs=1000)
    model.save(outfile)
#计算两个句子向量的相似性
def cos_dist(vec1,vec2):
    """
    :param vec1: 向量1
    :param vec2: 向量2
    :return: 返回两个向量的余弦相似度
    """
    # vec2 = vec2.reshape((100, 1))
    # print("输出vec1：{0}输出\nvec2:{1}".format(vec1,vec2))
    # print(type(vec1))
    # print(vec1)

    dist1=float(np.dot(vec1,vec2)/(np.linalg.norm(vec1)*np.linalg.norm(vec2)))
    return dist1
#dtw算法(可以计算两个不同长度口袋之间的相似性，也可以计算两个动态口袋之间的相似性
def dtw(x, y, warp=1, w=inf, s=1.0):
    """
    Computes Dynamic Time Warping (DTW) of two sequences.
    :param array x: N1*M array
    :param array y: N2*M array
    :param func dist: distance used as cost measure
    :param int warp: how many shifts are computed.
    :param int w: window size limiting the maximal distance between indices of matched entries |i,j|.
    :param float s: weight applied on off-diagonal moves of the path. As s gets larger, the warping path is increasingly biased towards the diagonal
    Returns the minimum distance, the cost matrix, the accumulated cost matrix, and the wrap path.
    """
    assert len(x)
    assert len(y)
    assert isinf(w) or (w >= abs(len(x) - len(y)))
    assert s > 0
    r, c = len(x), len(y)
    if not isinf(w):
        D0 = full((r + 1, c + 1), inf)
        for i in range(1, r + 1):
            D0[i, max(1, i - w):min(c + 1, i + w + 1)] = 0
        D0[0, 0] = 0
    else:
        D0 = zeros((r + 1, c + 1))
        D0[0, 1:] = inf
        D0[1:, 0] = inf
    D1 = D0[1:, 1:]  # view
    for i in range(r):
        for j in range(c):
            if (isinf(w) or (max(0, i - w) <= j <= min(c, i + w))):
                try:
                    if x[i][0][0]:
                        print("动态口袋DTW")
                except:
                    D1[i, j] = cos_dist(x[i], y[j])
                else:
                    D1[i, j] = dtw(x[i], y[j])
    C = D1.copy()
    jrange = range(c)
    for i in range(r):
        if not isinf(w):
            jrange = range(max(0, i - w), min(c, i + w + 1))
        for j in jrange:
            min_list = [D0[i, j]]
            for k in range(1, warp + 1):
                i_k = min(i + k, r)
                j_k = min(j + k, c)
                min_list += [D0[i_k, j] * s, D0[i, j_k] * s]
            D1[i, j] += min(min_list)
    if len(x) == 1:
        path = zeros(len(y)), range(len(y))
    elif len(y) == 1:
        path = range(len(x)), zeros(len(x))
    else:
        path = _traceback(D0)
    # return D1[-1, -1], C, D1, path
    return D1[-1, -1]
def _traceback(D):
    i, j = array(D.shape) - 2
    p, q = [i], [j]
    while (i > 0) or (j > 0):
        tb = argmin((D[i, j], D[i, j + 1], D[i + 1, j]))
        if tb == 0:
            i -= 1
            j -= 1
        elif tb == 1:
            i -= 1
        else:  # (tb == 2):
            j -= 1
        p.insert(0, i)
        q.insert(0, j)
    return array(p), array(q)
#model.save("test_01.model")
#model.wv.save_word2vec_format('test_01.model.txt','test_01.vocab.txt',binary=False)
#model_loaded = Word2Vec.load("netA80w2v.mod")
#model1 = word2vec.load("netA80w2v.mod")
# sim = model1.wv.most_similar(positive=[u'1130.1190.1232.1237'])
# for s in sim:
#     print( s[0])

def addtrain(filename,modelfile):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = LineSentence(filename)
    model = Word2Vec.load(modelfile)
    model.train(sentences, total_examples=model.corpus_count, epochs=1000)
    model.save(modelfile)

#model.save("test_01.model")
#model.wv.save_word2vec_format('test_01.model.txt','test_01.vocab.txt',binary=False)
#model_loaded = Word2Vec.load("netA80w2v.mod")
#model1 = word2vec.load("netA80w2v.mod")



# sim = model1.wv.most_similar(positive=[u'1130.1190.1232.1237'])
# for s in sim:
# #     print( s[0])
#
#生成向量，并DTW start
outfile="out/相似度.txt"
if __name__ == "__main__":
    #相似性计算部分，所有的口袋和1号口袋计算相似度

    #口袋目录
    pocketset=[]
    for i in range(1,20):
        pocketset.append("out/w2vTrainData"+str(i)+".txt")
    # print(pocketset)
    vect1=[]#存放连续时间的口袋
    #f1是对比的目标口袋，f2与f1对比
    # 读取多个步长的口袋数据
    with open(pocketset[0], 'r+', encoding='utf-8') as f1:
        for st1 in f1.readlines():
            # 单个时间片口袋
            vect1_ele = get_predict_vecs(st1)#list类型
            vect1.append(vect1_ele) #存入连续的口袋
    print(vect1)
            # print(vect1.shape)
    print("口袋1向量生成完毕")
    for j in range(1,19):#计算从1-19口袋的相关性
        vect2=[]#存放连续时间的口袋
        print("开始生成对比口袋向量————")
        with open(pocketset[j], 'r+', encoding='utf-8') as f2:
            for st2 in f2.readlines():
                # 单个时间片口袋
                # print(st2)
                vect2_ele = get_predict_vecs(st2)  # list类型
                # print(vect2_ele)
                vect2.append(vect2_ele)  # 存入连续的口袋
        print("对比口袋向量生成完毕，开始计算相似性————")
        print(vect2)
        correlation= dtw(vect1, vect2)#计算两个动态口袋之间的相似性
        # 输出
        file = open(outfile, 'a')
        file.write('动态口袋{0}与口袋1使用DTW对比相似得分： {1}'.format(j+1, correlation))
        file.close()

        print('动态口袋{0}与口袋1使用DTW对比相似得分： {1}'.format(j+1, correlation))
#生成向量，并DTW end


#训练模型部分
# trainmodel("out/w2vTrainData.txt","Trained1.mod")
# #训练集目录
# trainset=[]
# for i in range(2,20):
#     trainset.append("out/w2vTrainData"+str(i)+".txt")
# print(trainset)
#
#
# #根据训练集训练w2v模型
# for i in trainset:
#     print("第",i)
#     try:
#         addtrain(i, "Trained1.mod")
#     except:
#         print("跳过:",i)
#         continue
#训练模型部分结束