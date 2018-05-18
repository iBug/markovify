#!/usr/bin/env python3

from collections import defaultdict
import random

def markov(text, clen, cnum, charmode=False):
    s = text.split()
    if charmode:
        s = list(''.join(s))
    chain = defaultdict(list)
    for i in range(len(s)):
        for l in range(clen):
            try:
                chain[tuple(s[i:i+l])].append(s[i+l])
            except IndexError:
                pass
    out = [random.choice(s)]
    for i in range(cnum):
        for l in range(clen, 0, -1):
            try:
                out.append(random.choice(chain[tuple(out[-l:])]))
            except (IndexError, KeyError):
                continue
            except TypeError:
                print(l, len(out))
            else:
                break
    return ('' if charmode else ' ').join(out)

if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'r') as f:
        s = f.read()

    try:
        clen = int(sys.argv[2])
    except:
        clen = 2
    try:
        cnum = int(sys.argv[3])
    except:
        cnum = 50

    charmode = False
    if clen < 0:
        clen = -clen
        charmode = True
    print(markov(s, clen, cnum, charmode))
