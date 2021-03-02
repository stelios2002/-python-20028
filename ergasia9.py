file = input("Enter the file location of your text:")
f = open(file,'r')
f = f.read()
listf=[]
for element in range(0, len(f)):
    listf.append(f[element])
dict={"a":0}
for i in range(len(listf)-1):
    flag = False
    for k in dict:
        if listf[i]==k:
            flag = True
            break
    if not(flag):
        dict[listf[i]]=0
for i in listf:
    dict[i]=dict.get(i)+1
for i in dict:
    dict[i]=(dict.get(i)*100/len(listf))
for i in dict:
    dict[i]=int(dict.get(i)//1)+1
    dict[i]=dict.get(i)*"*"
for i in sorted(dict.items()):
    print(i[0],":",i[1])
