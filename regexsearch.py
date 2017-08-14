import os,re

filelist = os.listdir(os.getcwd())
txtfiles = []

for file in filelist:
    if file.endswith('.txt'):
        txtfiles.append(file)
        
lines = ""

for file in txtfiles:
    name = open(file,"r")
    lines += name.read() + "\n"   

rein = input("Please insert a Regular Expression:")

searchregex = re.compile(rein)

activesearch = searchregex.match(lines)
print(activesearch)
