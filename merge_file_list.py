f1 =open("file1.txt","r")
f2 =open("file2.txt","r")
content1 =f1.readlines()
content2 =f2.readlines()

new_content = content1+content2
print(new_content)

f1.close()
f2.close()
