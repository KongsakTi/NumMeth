import os

maxSoFar = 0

direct = "."
for filename in os.listdir(direct):
	name = filename.split('.')[0]
	if name != ".DS_Store" and filename != "util.py":
		if name[:4] == "Full":
			val = int(name[4:])
			if maxSoFar < val:
				maxSoFar = val

for filename in os.listdir(direct):
	name = filename.split('.')[0]
	if name != ".DS_Store" and filename != "util.py":
		if name[:4] != "Full" and filename[-3:] == "png":
			maxSoFar += 1
			# print(filename)
			os.rename(filename, "Full" + str(maxSoFar) + ".png")
print maxSoFar
