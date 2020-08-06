import os.path

if os.path.isfile('scores.txt'):
    fo=open('scores.txt','r')
    print("old file")
else:
    fo= open('scores.txt','w')
    print("new file")
    
d={}

print("歡迎進入系統")
print("#######################################")
while True:
    print("1.建立成績")
    print("2.列出所有成績")
    print("3.成績查詢系統")
    print("4.離開系統")
    x=int(input("請輸入數字: "))

    if x==4:
        break

    elif x==1:
         while True:
            name=str(input("請輸入姓名(按0跳出): "))
            if name=='0':
                break
            score=str(input("請輸入成績: "))
            d[name]=score
            
    elif x==2:
        print(d)
        
    elif x==3:
        while True:
            name=str(input("請輸入查詢姓名(按0跳出): "))
            if name=='0':
                break
            print(name,'的分數是',d[name])
            
fo=open("scores.txt",'w')
for k,v in d.items():
   fo.write(k)
   fo.write(':')
   fo.write(v)
   fo.write('\n')
fo.close


'''
for row in fo.readlines():
    data=row.split(':')
    
    key=data[0]
    value[1]
    value=value.strip()
    
    d[key]=value
'''
#print(d)
fo.close()






        