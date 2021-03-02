import re
import random

def sorting_of_element(list1,list2):

    # initializing blank dictionary
    f_1 = {}

    # initializing blank list
    final_list = []

    # Addition of two list in one dictionary
    f_1 = {list1[i]: list2[i] for i in range(len(list2))}

    # sorting of dictionary based on value
    f_lst = {k: v for k, v in sorted(f_1.items(), key=lambda item: item[1])}

    # Element addition in the list
    for i in f_lst.keys():
        final_list.append(i)
    return final_list

file = input("Enter the file location of your text:")
f = open(file,'r')
f = f.read()
listf=re.split(r'\;|\,| |\.|\n|\r|\:|\(|\)|\[|\]|\#|\$|\*|\&|\^|\@|\!|\-|\"|\'|\?|\_|\\', f)
i=len(listf)-1
while (i>=0):
    if (len(listf[i]) == 0):
        listf.pop(i)
    i = i - 1
listflens=[]
i=0
while (i<=len(listf)-1):
    listflens.append(len(listf[i]))
    i=i+1
flag=True
if(sum(listflens)<20):
    flag=False
listf, listflens = (list(t) for t in zip(*sorted(zip(listf, listflens))))
while (flag):
    i=0
    j=len(listf)-1
    sum=0
    sumnums=[]
    flag=False
    flag2=True
    while (i<=j and flag2):
        if (listflens[j]+sum<=20):
            sumnums.append(j)
            sum+=listflens[j]
        j-=1
        if (sum==20):
            flag2=False
    if (sum==20):
        for j in range(len(sumnums)-1):
            listflens.pop(sumnums[j])
            listf.pop(sumnums[j])
        flag=True
    else:
        j=len(listf)-1
        flag2=True
        sum=0
        sumnums=[]
        while (i<=j and flag2):
            if (listflens[i]+sum<=20):
                sumnums.append(i)
                sum+=listflens[i]
            i+=1
            if (sum==20):
                flag2=False
        if (sum==20):
            k=0
            for i in range(len(sumnums)-1):
                listflens.pop(sumnums[i-k])
                listf.pop(sumnums[i-k])
                k+=1
            flag=True
print(listf)
