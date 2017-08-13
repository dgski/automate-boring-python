import os
import sys

#If commandline argument is empty then use current working directory
if(len(sys.argv) < 2):
	target = os.getcwd()
#Else use the argument 
else:
	target = sys.argv[1]


#Item Dicitonary
items = {}

#Iterate over the directory
for item in os.listdir(target):
	items[item] = (os.stat(target + "/" + item).st_size) #/1000


#Function to print fancy table
def FancyLs(items, leftWidth, rightWidth):
	path,folder_name = os.path.split(target)
	print(folder_name.center(leftWidth + rightWidth, '-'))
	print('Name'.ljust(leftWidth) + 'Size'.rjust(numberwidth))
	print("-" * (leftWidth + rightWidth))

	for item, size in items.items():
		print(item.ljust(leftWidth, '.') + str(size).rjust(rightWidth,'.'))

#Calculate width of table
namewidth = len(max(items, key=len)) + 3
numberwidth = len(max(items.keys(), key=(lambda k: items[k])))

print(namewidth, numberwidth)

FancyLs(items, namewidth, numberwidth)
