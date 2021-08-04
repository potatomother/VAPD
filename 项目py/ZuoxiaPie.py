#计算亲疏水性，首先确定pocket，然后依次计算各个model中的残基。
#对2000遍历某pocket 中的某model的每个球。找到最接近该球的4个残基编号。
#将残基编号存入列表，去重
#创建根据编号查询残基的函数
#根据残基列表计算亲疏水性（均值）

#import distance
#import math
# from Bio.PDB.PDBParser import PDBParser
import numpy as np
from aic_sc import atomradius
# from residue_hydrophobicity import residuehydrophobicity
# import struct
# import glob
# import csv
# import eulerangles
# import string
import re
import math



fname1 = 'data/mdpout_mdpocket.pdb'  #文件夹路径
fname2 = 'data/mdpout_mdpocket_atoms.pdb'  #文件夹路径
#根据输入氨基酸序列，输出亲疏水极性统计
def mycountdemo ( mylist ):
    # 对输入的字符串进行匹配
    # 氨基酸序列


    # 氨基酸序列对应的个数
    # Asp Glu His Lys Asn Gln Arg  1-6亲水性
    # Pro Ser Thr Trp Tyr
    # Gly
    # Ala Cys Phe Met
    # Leu
    # Iie Val
    # 极性 Ala Val Leu Iie Phe Met Pro Trp
    # Thr Ser Cys Asn Gln Tyr Gly
    # Lys Arg His
    # Asp Glu


    listB = [[0, 0, 0, 0, 0, 0],[0, 0, 0, 0]]
    for i in mylist:
        if i == 'ASP' or i == 'GLU' or i == 'HID' or i == 'LYS' or i == 'ASN' or i == 'GLN' or i == 'ARG':
            listB[0][5] = listB[0][5]+1
        elif i == 'PRO' or i == 'SER' or i == 'THR' or i == 'TRP' or i == 'TYR':
            listB[0][4] = listB[0][4] + 1
        elif i == 'GLY':
            listB[0][3] = listB[0][3] + 1
        elif i == 'ALA' or i == 'CYS' or i == 'PHE' or i == 'MET':
            listB[0][2] = listB[0][2] + 1
        elif i == 'LEU':
            listB[0][1] = listB[0][1] + 1
        elif i == 'IIE' or i == 'VAL':
            listB[0][0] = listB[0][0] + 1
        # Ala Val Leu Iie Phe Met Pro Trp
        # Thr Ser Cys Asn Gln Tyr Gly
        # Lys Arg His
        # Asp Glu
    for i in mylist:
        if i == 'ALA' or i == 'VAL' or i == 'LEU' or i == 'IIE' or i == 'PHE' or i == 'MET' or i == 'PRO' or i == 'TRP':
            listB[1][0] = listB[1][0] + 1
        elif i == 'THR' or i == 'SER' or i == 'CYS' or i == 'ASN' or i == 'GLN' or i == 'TYR' or i == 'GLY':
            listB[1][1] = listB[1][1] + 1
        elif i == 'LYS' or i == 'ARG' or i == 'HID':
            listB[1][2] = listB[1][2] + 1
        elif i == 'ASP' or i == 'GLU':
            listB[1][3] = listB[1][3] + 1
    return listB
#输出函数
def shuchu1(s):
    #输出
    # 参数file是文件名，s是数据
    file = open('test3.txt','a')
    sw = str(s)
    file.write(sw)
    file.close()
#根据残基名字查询残基的亲疏水性
def hydrophobiciy(aic):
    ave=0
    scor=0
    for a in aic:
        with open(fname2, 'r+', encoding='utf-8') as f2:
            # for line in f.readlines():    #按行读取每行
            # print(line[:-1].split(' ')) #切片去掉换行符，再以‘，’分割字符串 ，得到一个列表
            atoms = []
            for j in f2.readlines():
                iafter2 = re.sub(' +', ' ', j)
                aele2 = iafter2[:-1].split(' ')
                aele2 = np.array(aele2)
                if len(aele2)>3 and a==aele2[5]:
                    scor=scor + atomradius(aele2[3])
                    break
    ave=scor/len(aic)
    return ave
#根据序号查询残基名字
def hydrophobiciy1(aic):
    residue=[]
    for a in aic:
        with open(fname2, 'r+', encoding='utf-8') as f2:
            # for line in f.readlines():    #按行读取每行
            # print(line[:-1].split(' ')) #切片去掉换行符，再以‘，’分割字符串 ，得到一个列表
            atoms = []
            for j in f2.readlines():
                iafter2 = re.sub(' +', ' ', j)
                aele2 = iafter2[:-1].split(' ')
                aele2 = np.array(aele2)
                if len(aele2)>3 and a==aele2[5]:
                    residue.append(aele2[3])
                    break
    return residue


#计算pdb文件中pocket的体积，每个时间片，每个pocket都计算
#输出格式[ , ],[ , ],[ , ]...[ , ],第一维度是时间片，第二个维度是pocket
def comhydrophobiciy(pocket):
    print("pocket",pocket)
    aicsum=[]
    aic = []#残基
    with open(fname1, 'r+', encoding='utf-8') as f1:
        #for line in f.readlines():    #按行读取每行
            #print(line[:-1].split(' ')) #切片去掉换行符，再以‘，’分割字符串 ，得到一个列表
        for i in f1.readlines():
            iafter1=re.sub(' +', ' ', i)
            aele1=iafter1[:-1].split(' ')
            aele1 = np.array(aele1)
            if len(aele1)<3:
                if aele1[0]=='MODEL':
                    model=int(aele1[1])
                    #print('model'+ aele1[1])
                    continue
            if len(aele1)>3 :
                if pocket == int(aele1[4]):   #计算每个model的第n个pocket
                    x = float(aele1[5])
                    y = float(aele1[6])
                    z = float(aele1[7])
                    #扫描第二个文件的model
                    sta = 0
                    with open(fname2, 'r+', encoding='utf-8') as f2:
                        # for line in f.readlines():    #按行读取每行
                        # print(line[:-1].split(' ')) #切片去掉换行符，再以‘，’分割字符串 ，得到一个列表
                        atoms = []
                        for j in f2.readlines():
                            iafter2 = re.sub(' +', ' ', j)
                            aele2 = iafter2[:-1].split(' ')
                            aele2 = np.array(aele2)
                            if len(aele2) < 3:
                                if aele2[0] == 'MODEL' and model == int(aele2[1]):
                                    sta = 1
                                    continue
                                if aele2[0] == 'ENDMDL' and sta == 1:
                                    # aic中加入四个最近的残基
                                    atoms.sort(key=lambda x: x[1])
                                    aic.append(atoms[0][0])
                                    aic.append(atoms[1][0])
                                    aic.append(atoms[2][0])
                                    aic.append(atoms[3][0])
                                    break
                            if sta==1 :
                                distace = math.sqrt((x - float(aele2[6])) ** 2 + (y - float(aele2[7])) ** 2 + ((z - float(aele2[8]))) ** 2)
                                atom=[aele2[5], distace]
                                atoms.append(atom)
            if len(aele1)<3 and aele1[0]=='ENDMDL': #结束一个model，去重，查询残基的亲疏水性
                print(model)
                if len(aic)==0:
                    continue
                else:
                    aic = list(set(aic))
                    aicsum.append(aic)
                    aic=[]
        res=[]
        for i in range(len(aicsum)):
            res=res+aicsum[i]
        # 残基
        residue = hydrophobiciy1(res)#根据残基序号查残基名字
        a=mycountdemo(residue)#根据残残基名字，输出亲疏水极性统计
        return a














