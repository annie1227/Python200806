file=open("jade weber.jpg","rb")
img=file.read()
file.close()

file=open("複製.jpg","wb")
file.write(img)
file.close()