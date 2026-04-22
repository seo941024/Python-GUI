with open("test.txt", 'w', encoding = 'utf-8') as f:
    f.write("I'm fine thank you\n")
    f.write("And you?\n\n")
    f.write("Have a nice day\n")

f = open ("test.txt",'r',encoding = 'utf-8')
print(f.read(4))
print(f.read(4))
s1 = f.read()
print(s1)
f.read()

print(f.tell())
f.seek(0)
f.read()