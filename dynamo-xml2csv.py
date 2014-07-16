#!/usr/bin/env python
import argparse
import glob
import sys
import os.path
import xml.etree.ElementTree as etree

parser = argparse.ArgumentParser(description='Extract parameters from .xml or .xml.bz2 files, output as csv.')

parser.add_argument('keys', nargs=1, help='keys to read, separated with commas')
parser.add_argument('files', metavar='file', nargs='+', help='input files')

args = parser.parse_args()

for fileName in args.files:
    tree = None
    if fileName[-4:] == ".bz2":
        tree = etree.parse(bz2.BZ2File(fileName))
    else:
        tree = etree.parse(fileName)

    for keyPath in args.keys[0].split(','):
        sys.stdout.write(tree.find(keyPath).items()[0][1] + "\t")

    print()
