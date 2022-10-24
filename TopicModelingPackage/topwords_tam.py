#!/usr/bin/python

import sys
from operator import itemgetter


def main():
	filename = sys.argv[1]
	infile = open(filename, "r")

	Y = 0
	Z = 0
	count = {}
	countY = {}

	for line in infile:
		tokens = line.split()
		# we don't use this but we need to remove it from the token list
		collection = int(tokens.pop(0))

		for token in tokens:
			parts = token.split(":")
			x = int(parts.pop())
			l = int(parts.pop())
			y = int(parts.pop())
			z = int(parts.pop())
			word = ":".join(parts)

			if y > Y:
				Y = y
			if z > Z:
				Z = z

			if l == 0:
				z = -1  # this will represent the "background"

			if x == 0:
				if z not in count:
					count[z] = {}
				if word not in count[z]:
					count[z][word] = 0
				count[z][word] += 1
			else:
				if y not in countY:
					countY[y] = {}
				if z not in countY[y]:
					countY[y][z] = {}
				if word not in countY[y][z]:
					countY[y][z][word] = 0
				countY[y][z][word] += 1

	infile.close()

	Y += 1
	Z += 1

	for z in range(-1, Z):
		if z == -1:
			print("Background")
		else:
			print("Topic %d" % (z+1))

		w = 0
		if (z not in count):
			words = {}
		else:
			words = sorted(count[z].items(), key=itemgetter(1), reverse=True)

		for word, v in words:
			print(word)
			w += 1
			if w >= 20:
				break

		for y in range(Y):
			print(" Aspect %d" % (y+1))

			w = 0

			if (y not in countY or z not in countY[y]):
				words = {}
			else:
				words = sorted(countY[y][z].items(), key=itemgetter(1), reverse=True)
			for word, v in words:
				print(" ", word)
				w += 1
				if w >= 20:
					break

		print("\n")


if __name__ == "__main__":
  main()
