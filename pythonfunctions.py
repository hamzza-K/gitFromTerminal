import sys
import time

name = sys.argv[1]

def taking_names():
	return "Hello " + name

if __name__ == '__main__':
	print(taking_names())
