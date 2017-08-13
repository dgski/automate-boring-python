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
	print('Name'.ljust(leftWidth) + 'Size (bytes)'.rjust(rightWidth))
	print("-" * (leftWidth + rightWidth))

	for item, size in items.items():
		print(item.ljust(leftWidth, '.') + str(size).rjust(rightWidth,'.'))
		
#Calculate width of table
fullwidth = len(max(items, key=len)) +len('...')

print(fullwidth)
FancyLs(items, 25, 13)
