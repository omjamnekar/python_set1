


f1 = open("file1.txt","r")
f2 = open("file2.txt","r")

temp= open("temp.txt","w+")

temp.write(f1.read())

temp.write(f2.read())
temp.seek(0,0)
print(temp.read())

f1.close()

f2.close()
temp.close()
