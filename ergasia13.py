import re

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
for i in range(1,20):
    print("\'",i,"\'",":", end="")
    flag3=True
    k=0
    for j in listflens:
        if (j==i):
            print(listf[k], end=" ")
            flag3=False
        k+=1
    if flag3:
        print("\"\"", end="")
    print("\r")
