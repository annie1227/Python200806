import os.path

if os.path.isfile('favorite.txt'):
    print("file 存在")
else:
    print("file 不存在")
    
fo=open("favorite.txt","w")
fo.write("I love sunny day")
#fo=open("favorite.txt","r")
#fo.read()
fo=open("favorite.txt","a")
fo.write(" with blue sky")
fo.close()
    