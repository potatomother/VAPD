#ps：输入序列是哪个py的结果？

# 对输入的字符串进行匹配
# 氨基酸序列

listc=['DEHKNQR/PSTWY/G/ACFM/L/IV']
# 氨基酸序列对应的个数
#Asp Glu His Lys Asn Gln Arg  1-6亲水性
#Pro Ser Thr Trp Tyr
#Gly
#Ala Cys Phe Met
#Leu
#Iie Val
#极性 Ala Val Leu Iie Phe Met Pro Trp
#Thr Ser Cys Asn Gln Tyr Gly
#Lys Arg His
#Asp Glu


def mycountdemo ( mylist ):
    listB = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #list 0-5 亲水性6-9极性
    for i in mylist:
        if i == 'ASP' or i == 'GLU' or i == 'HID' or i == 'LYS' or i == 'ASN' or i == 'GLN' or i == 'ARG':
            listB[0] = listB[0]+1
        elif i == 'PRO' or i == 'SER' or i == 'THR' or i == 'TRP' or i == 'TYR':
            listB[1] = listB[1] + 1
        elif i == 'GLY':
            listB[2] = listB[2] + 1
        elif i == 'ALA' or i == 'CYS' or i == 'PHE' or i == 'MET':
            listB[3] = listB[3] + 1
        elif i == 'LEU':
            listB[4] = listB[4] + 1
        elif i == 'IIE' or i == 'VAL':
            listB[5] = listB[5] + 1
        # Ala Val Leu Iie Phe Met Pro Trp
        # Thr Ser Cys Asn Gln Tyr Gly
        # Lys Arg His
        # Asp Glu
    for i in mylist:
        if i == 'ALA' or i == 'VAL' or i == 'LEU' or i == 'IIE' or i == 'PHE' or i == 'MET' or i == 'PRO' or i == 'TRP':
            listB[6] = listB[6] + 1
        elif i == 'THR' or i == 'SER' or i == 'CYS' or i == 'ASN' or i == 'GLN' or i == 'TYR' or i == 'GLY':
            listB[7] = listB[7] + 1
        elif i == 'LYS' or i == 'ARG' or i == 'HID':
            listB[8] = listB[8] + 1
        elif i == 'ASP' or i == 'GLU':
            listB[9] = listB[9] + 1
    return  listB+mylist
def ListtoEchartInput(mylist):

    a=\
    "{value:"+str(mylist[0]) +", name: '非常亲水'},{value:"+str(mylist[1])+", name: '亲水的'},{value:"\
    +str(mylist[2])+", name: ''疏水性小'},{value:"+str(mylist[3])+", name: '疏水性好'},{value:"+str(mylist[4])+", name: '疏水的'},{value:"\
    +str(mylist[5])+", name: '疏水性强'}   "
    b="{value:"+str(mylist[6]) + ", name: '非极性'},{value:"+str(mylist[7]) + ", name: '极性中性'},{value:"\
    +str(mylist[8]) + ", name: '正电'},{value:"+str(mylist[9]) + ", name: '负电'}"
    print(a)
    print(b)


list=[['MET', 'ARG', 'GLU', 'HID', 'LEU', 'SER', 'PRO'],
      ['GLY', 'ALA', 'ALA', 'CYS', 'ALA', 'PHE', 'LEU', 'THR', 'LYS', 'PHE'],
      ['GLY', 'ASP', 'GLU', 'THR', 'PRO'],
      ['PHE', 'GLY', 'ALA', 'PHE', 'TYR', 'HID', 'ALA', 'VAL', 'CYS', 'PHE', 'LEU', 'THR', 'LYS', 'ALA'],
      ['PHE', 'ALA', 'CYS', 'THR', 'LYS', 'ALA'],
      ['GLY', 'ALA', 'ALA', 'ALA', 'PHE', 'LEU', 'THR', 'LYS', 'PHE']
      ]
for i in list :
    temp=mycountdemo(i)
    ListtoEchartInput(temp)


