#Comma code: returns string with last item concatenated with 'and'
spam = ['apples','bananas','tofu','cats'];

def stringer(listofthings):

	string = ""

	for i,x in enumerate(listofthings):
		if i == len(listofthings) - 1:
			string += "and " + x + "."
		elif i == 0:
			string += x[0].upper() + x[1:] + " "
		else:
			string += x + ", "

	return string

print(stringer(spam))

