str1="vignan=23,cse=12,iit=19,nikhil=78"
lst=[]
for x in str1.split(','):
    y=x.split('=')
    lst.append(y)
d=dict(lst)


d1={}
for k,v in d.items():
    d1[k]=int(v)
print(d1)
type(d)
