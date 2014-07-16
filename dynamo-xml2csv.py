#!/usr/bin/env python
import os.path
import xml.etree.ElementTree as etree
from argparse import ArgumentParser
from bz2 import BZ2File
from sys import stdout

parser = ArgumentParser(description='Extract parameters from .xml or .xml.bz2 files, output as csv.')

parser.add_argument('keys', nargs=1, help='keys to read, separated with commas')
parser.add_argument('files', metavar='file', nargs='+', help='input files')

args = parser.parse_args()

for fileName in args.files:
    tree = None
    if fileName[-4:] == ".bz2":
        tree = etree.parse(BZ2File(fileName))
    else:
        tree = etree.parse(fileName)

    for keyPath in args.keys[0].split(','):
        stdout.write(tree.find(keyPath).items()[0][1] + "\t")

    print()
