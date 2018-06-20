"""Test.py"""
import os

myLines = []
with open("problems.txt", 'r', errors='ignore') as problemFile:
    myLines = problemFile.readlines()

begLineList = []
for idx, lines in enumerate(myLines):
    if lines.startswith("Problem"):
        begLineList.append(idx)
begLineList.append(len(myLines))

Alpha = ""
numBottom = ""
numTop = ""
dirName = ""
ii = 0

for idx, line in enumerate(begLineList):
    if (idx == len(begLineList) - 1):
        break
    if (idx % 20 == 0):
        Alpha = chr(ord('A') + ii)
        numBottom = str(ii * 20 + 1)
        numTop = str(((ii + 1) * 20))
        topDirName = str(Alpha) + ". Projects " + numBottom + " - " + numTop
        if not os.path.exists(topDirName):
            os.makedirs(topDirName)
        ii = ii + 1
    fulldirName = topDirName + '/' + 'P' + str(idx + 1) + '_'
    if not os.path.exists(fulldirName):
        os.makedirs(fulldirName)
    fullPath = fulldirName + '/' + 'P' + str(idx + 1) + '.py'
    if not os.path.exists(fullPath):
        writeFile = open(fullPath, 'w')
        writeFile.write('"""\n')
        for writeLines in myLines[begLineList[idx]:begLineList[idx+1]]:
            writeFile.write(writeLines)
        writeFile.write('"""\n')
        writeFile.close()
