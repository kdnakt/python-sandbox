# coding=utf8
from __future__ import print_function
path = 'memo.txt'

with open(path) as f:
    for line in f:
        if line.startswith('■'):
            print(line, end='')