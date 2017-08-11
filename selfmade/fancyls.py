import os
import sys

#If commandline argument is empty then use current working directory
if(len(sys.argv) < 2):
	target = os.getcwd()
#Else use the argument 
else:
	target = sys.argv[1]

#Iterate over the directory
for afolder in os.listdir(target):
	print(folder)





