#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 23:46:52 2020

@author: rochor
"""

with open('input.txt') as f:
    full_text = f.read().split('\n')

i = 0
while (i < len(full_text)):
    if len(full_text[i]) > 40:
        j = 39
        while j:
            if full_text[i][j] == ' ':
                new = full_text[i][j+1:]
                full_text[i] = full_text[i][:j]
                full_text.insert(i+1, new)
                break
            j -= 1
        else:
            new = full_text[i][39:]
            full_text[i] = full_text[i][:39]+'_'
            full_text.insert(i+1, new)
    i += 1
'''
with open('res.txt', 'w') as f:
    for i in full_text:
        f.write(i + '\n')
'''

def lengthen(line):
    if len(line) <= 50:
        return line + ' ' * (50-len(line))
    else:
        raise Exception('??? Line too long ???')

def processLine(line, word):
    location = line.find(word)
    return lengthen(line[:location] + ' ' + line[location:]) + (line[:location+len(word)] + ' ' + line[location+len(word):])

highlighted = "Project Bible GUTENBERG"
l = 0
res = ''
for word in highlighted.split():
    if l < len(full_text):
        while word not in full_text[l]:
            line = lengthen(full_text[l]) + full_text[l]
            l += 1
            res += line + '\n'
        else:
            line = processLine(full_text[l], word)
            l += 1
            res += line + '\n'
    else:
        raise Exception("%s not found!" % word)

i = 10
while l < len(full_text) and i:
    i -= 1
    line = lengthen(full_text[l]) + full_text[l]
    l += 1
    res += line + '\n'

with open('res.txt', 'w') as f:
    f.write(res)
