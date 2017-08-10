import sys
# Author Niklas le Comte
#
# This program copies and adds the id number of each simulation to
# the values for that simulation for each simulated state.
# Add more .csv args (one for each state) to split the data into more chunks.
#
def appenedTop():
	return "ID TIME DONE" + '\n'

args = sys.argv;
newFile = open(args[2], 'w')

if(len(args) >= 3):
	with open(args[1]) as f:
		id = ''
		index = -1
		argNum = 2
		for line in f:
			if ' #' in line:
				index = line.find(' #') + 2
				id = line[index:]
				#checks if it is at the first simulation of a state
				if id.rstrip('\n') == '1' and argNum < len(args):
					newFile.close()
					newFile = open(args[argNum], 'w')
					newFile.write(appenedTop())
					argNum += 1
				newFile.write(line)
			else:
				newFile.write('%s%s%s' % (id.rstrip('\n'), " ", line))
else:
	print("you need at least two argsuments")
	
	
	
	
	
	
	
	
	
	
	
