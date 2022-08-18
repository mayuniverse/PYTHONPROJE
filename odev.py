list1= [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
n_list=[]
def m(a):

    for k in a:
        if isinstance(k,list):
            m(k)
        else:
            n_list.append(k)

m(list1)
print(n_list)


l=[[1, 2], [3, 4], [5, 6, 7]]
n_l=[]
def rvrs(a):
    a=a[::-1]
    for i in a:
        if isinstance(i,list):
            b=i[::-1]
            n_l.append(b)
        else:
            n_l.append(i)
    return n_l
print(rvrs(l))