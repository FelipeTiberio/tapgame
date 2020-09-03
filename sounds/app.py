from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(".") if isfile(join(".", f))]

aut = []

for file in onlyfiles:
	aut.append('sounds/' + file); 

print(aut)
