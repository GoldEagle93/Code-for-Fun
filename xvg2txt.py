#!/usr/bin/env python

"""
I wanted to be able to use Gromacs xvg files in Apple's Numbers app for plotting.
The app didn't support defining delimination parameters (comma, space, tab, etc.)
then, So I made this to do the job.
"""

import fileinput
import sys

newfile = open('%s.txt' % (sys.argv [1:]), 'a')
keyword1 = '     '
keyword2 = '    '
keyword3 = '   '
keyword4 = '  '
keyword5 = ' '
replacement = '	'
for line in fileinput.input(sys.argv[1:]):
    stripped = line.lstrip()
    if stripped.startswith('@') or stripped.startswith('#'):
        continue
    elif keyword1 in stripped:
        stripped = stripped.replace(keyword1, replacement)
        newfile.write(stripped)
    elif keyword2 in stripped:
        stripped = stripped.replace(keyword2, replacement)
        newfile.write(stripped)
    elif keyword3 in stripped:
        stripped = stripped.replace(keyword3, replacement)
        newfile.write(stripped)
    elif keyword4 in stripped:
        stripped = stripped.replace(keyword4, replacement)
        newfile.write(stripped)
    elif keyword5 in stripped:
        stripped = stripped.replace(keyword5, replacement)
        newfile.write(stripped)
newfile.close()
