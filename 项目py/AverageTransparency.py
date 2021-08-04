#import distance
#import math
from Bio.PDB.PDBParser import PDBParser
import numpy as np
from atom_radius import atomradius
from residue_hydrophobicity import residuehydrophobicity
import struct
import glob
import csv
import eulerangles
import string
import re

#输出scv文件
def shuchu2(a, num): #输出2
    s = []
    for i in range(len(a)):
        s1 = [num, i, a[i]]
        s.append(s1)
    shuchu1('test.csv', s)


def shuchu1(flie, s):#输出1
    # 输出
    # 参数file是文件名，s是数据
    file = open(flie, 'a')
    for i in range(len(s)):
        sw = str(s[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        sw = sw.replace("'", ' ')+ '\n'  # 去除单引号，逗号，每行末尾追加换行符
        file.write(sw)
    file.close()
    #print("保存文件成功")
#num 个一组求数组求均值
def Divided(vector,num): #num 个一组求数组均值
    mean = []
    for i in range(int(len(vector)/num)):
        tem=vector[i:i + num]
        #mean.append(np.mean(tem))
        n0 = 0#求分母
        for j in tem:
            if j !=0:
                n0=n0+1

        sumtemp=np.sum(tem) #分子
        if n0==0:
            mean.append(0)
        else:
            mean.append(sumtemp/n0)
    return mean
#num 个一组求数组求透明度
def diaphaneity(vector,num):
    dia=[]
    for i in range(int(len(vector)/num)):
        tem=vector[i:i + num]
        #mean.append(np.mean(tem))
        n0 = 0#求分母
        for j in tem:
            if j !=0:
                n0=n0+1
        dia.append(n0/10)
    return dia


#10个一组求时间片的数据
# amean=Divided(a,10)
# bmean=Divided(b,10)
# cmean=Divided(c,10)
# dmean=Divided(d,10)
# emean=Divided(e,10)
# #输出
# print (amean)
# print(',')
# print (bmean)
# print(',')
# print (cmean)
# print(',')
# print (dmean)
# print(',')
# print (emean)
#计算透明度
# aDia=diaphaneity(a,10)
# bDia=diaphaneity(b,10)
# cDia=diaphaneity(c,10)
# dDia=diaphaneity(d,10)
# eDia=diaphaneity(e,10)
# #输出透明度
# print(aDia)
# print(bDia)
# print(cDia)
# print(dDia)
# print(eDia)
# #输出csv文件
# shuchu2(amean, 'pocket1')
# shuchu2(bmean, 'pocket2')
# shuchu2(cmean, 'pocket3')
# shuchu2(dmean, 'pocket4')
# shuchu2(emean, 'pocket5')

# for i in range(22):
#     amean=Divided(f[i],10)
#     shuchu2(amean, 'pocket'+str(i+1))
#     Dia=diaphaneity(f[i],10)
#     print(Dia)
#     print(',')



