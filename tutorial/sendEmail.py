import os,sys
print(os.getcwd(),sys.argv[0])
f = open(os.getcwd()+r"\spiders\List.json")
line = f.readline().decode('unicode_escape')
textr = []
while line:
    textr.append(line)
    line = f.readline().decode('unicode_escape')
body = ' '.join(textr)
print(body)