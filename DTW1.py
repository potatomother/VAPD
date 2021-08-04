# 计算序列组成单元之间的距离，可以是欧氏距离，也可以是任何其他定义的距离,这里使用绝对值
#这个计算dtw是从知乎上找的，效果没有用原本的dtw库方法好，暂时不用
def distance(w1, w2):
    d = abs(w2 - w1)
    return d


# DTW计算序列s1,s2的最小距离
def DTW(s1, s2):
    m = len(s1)
    n = len(s2)

    # 构建二位dp矩阵,存储对应每个子问题的最小距离
    dp = [[0] * n for _ in range(m)]

    # 起始条件,计算单个字符与一个序列的距离
    for i in range(m):
        dp[i][0] = distance(s1[i], s2[0])
    for j in range(n):
        dp[0][j] = distance(s1[0], s2[j])

    # 利用递推公式,计算每个子问题的最小距离,矩阵最右下角的元素即位最终两个序列的最小值
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + distance(s1[i], s2[j])

    return dp[-1][-1]


# s1 = [1, 3, 2, 4, 2]
# s2 = [0, 3, 4, 2, 2]
#
# print('DTW distance: ', DTW(s1, s2))