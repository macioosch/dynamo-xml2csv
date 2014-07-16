#!/usr/bin/env python
import glob
import sys
import os.path
import xml.etree.ElementTree as etree

usageString = "\tUsage: dynamo-xml2csv KEY [KEY]... FILE\n\tAccepts .xml and .xml.bz2 files."

if len(sys.argv) < 3:
    sys.exit("ERROR: Too few arguments!\n" + usageString)

fileName = sys.argv[-1]
if not os.path.isfile(fileName):
    sys.exit("ERROR: Can't open file \"" + fileName + "\"!\n" + usageString)
tree = None
if fileName[-4:] == ".bz2":
    tree = etree.parse(bz2.BZ2File(fileName))
else:
    tree = etree.parse(fileName)

for keyPath in sys.argv[1:-1]:
    sys.stdout.write(tree.find(keyPath).items()[0][1] + "\t")

print()
