# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
import string
import networkx as nx
import numpy as np
dict_1={}
dict_2={}

# def test_bridge(matix,len_dic,a,b):
#
#     if a not in dict_1:
#         return None
#     elif b not in dict_1:
#         return None
#
#     else:
#         a_index = dict_1[a]["id"]
#         b_index = dict_1[b]["id"]
#         list_a = []
#         list_b = []
#         for i in range(len_dic):
#             if matix[a_index][i] == 1:
#                 list_a.append(i)
#             if matix[i][b_index] == 1:
#                 list_b.append(i)
#         x = [k for k in list_a if k in list_b]
#         if len(x) == 0:
#             return None
#         else:
#             list_3 = []
#             for i in x:
#                 list_3.append(dict_2[i])
#
#             return list_3


def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    list_1=[]
    with open("test.txt", "r") as f:  # 打开文件
        data = f.read()  # 读取文件
        #print(data)

        data = "".join([i for i in data if i not in string.punctuation])
        data =data.replace('\n', ' ').replace('\r', ' ')
        data=data.lower()

        #print(data)
        for i in data:
            if i.isalpha():

                list_1.append(i)
            else:
                if list_1[len(list_1)-1]!=' ':

                    list_1.append(i)
    str="".join(list_1)
    #print(str)
    list_2=str.split(' ')
    print(list_2)

    j=0
    for i in list_2:
        if i not in dict_1:
            dict_2.update({j:i})
            dict_1.update({i:{"num":1,"id":j}})
            j = j + 1
        else:
            dict_1[i]["num"]+=1
    print(dict_1)
    matix=np.zeros((j,j),dtype=int)
    t=0
    len1=len(list_2)-1
    for i in range(len1):
        first=list_2[t]
        second=list_2[t+1]
        t+=1
        x=dict_1[first]["id"]
        y=dict_1[second]["id"]
        matix[x][y]=matix[x][y]+1
    print(matix)
    len_dic=len(dict_1)
    a =input("input1:")
    b=input("input2:")
    if a not in dict_1 :
        print("No word1 or word2 in the graph!")
    elif b not in dict_1:
        print("No word1 or word2 in the graph!")

    else:
        a_index=dict_1[a]["id"]
        b_index=dict_1[b]["id"]
        list_a=[]
        list_b=[]
        for i in range(len_dic):
            if matix[a_index][i]==1:
                list_a.append(i)
            if matix[i][b_index]==1:
                list_b.append(i)
        x = [k for k in list_a if k in list_b]
        if len(x)==0:
            print("/"+"No bridge words from word1 to word2!")
        else:
            list_3=[]
            for i in x:
                list_3.append(dict_2[i])

            print("The bridge words from word1 to word2 are :{}".format(", ".join(list_3)))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
