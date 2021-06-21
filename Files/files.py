FILENAME = "data.txt"
BINFILE = "data2.dat"
"""
Modes:
"r" +
"w" +
"rb"
"wb"
"a"



"""
#TEXT
def readfile(filename):
	with open(filename, "r") as fp:
		return fp.read()

def writefile(filename, data):
	with open(filename, "w") as fp:
		fp.write(data)

def appendfile(filename, data):
	with open(filename, "a") as fp:
		fp.write(data)

#BINARY
def readbinfile(filename):
	with open(filename, "rb") as fp:
		return fp.read()

def writebinfile(filename, data):
	with open(filename, "wb") as fp:
		fp.write(data)



if __name__ == "__main__":
	appendfile(FILENAME, "Hello Nick")
