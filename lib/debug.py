#!/usr/bin/env python3

from anagram import Anagram

if __name__ == '__main__':
    a = Anagram("listen")
    results = a.match(["enlist", "silent", "hello", "world"])
    print("Anagrams of 'listen':", results)
    import ipdb
    ipdb.set_trace()
