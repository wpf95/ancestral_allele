import sys
fo=open(sys.argv[1],"r")
fo2=open(sys.argv[2],"w")

m = 0
l1=[]
n = 0
l2=[]

for line in fo:
    line1 = line.strip().split()
    for i in line1[9:]:
        num=len([x.strip() for x in line1[9:]])
###找纯合基因型
        if i[0:3:1] ==  '1/1' :
            m = m+1
        elif i[0:3:1] == "0/0":
            n = n+1
    l1.append(m)
    l2.append(n)
    try:
        s = l1[-1] - l1[-2]
        freq1 =float (s / num)
        z = l2[-1] - l2[-2]
        freq2 = float(z / num)
###寻找纯合等位基因型几率大于50%的点
        if freq1 > 0.5:
            fo2.write(line1[0]+"\t"+line1[1]+"\t"+'1/1'+"\n")
        elif freq2 > 0.5:
            fo2.write(line1[0]+"\t"+line1[1]+"\t"+'0/0'+"\n")
    except:
        pass
fo.close()
fo2.close()







