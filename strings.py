#Table Printer
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
	colwidths = [0] * len(tableData)


	for i in range(len(table[0])):
		for n in range(len(table)):
			colwidths[n] = len(max(table[n],key=len))
			print(table[n][i].rjust(colwidths[n]," "), end=" ")
		print()

printTable(tableData)