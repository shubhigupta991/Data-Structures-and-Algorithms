strings = ['a','b','c','d']
# for 64-bit, 8*4 = 32 bytes

print(strings[2])

#push
strings.append('e')                 # O(1)

#pop
strings.pop()
strings.pop()                       # O(1)

#addelementatfirst
strings.insert(0,'A')               # O(n)

#addinmiddle
strings.insert(2,'alien')           # O(n)

#addatlast
strings.insert(len(strings),'d')    # O(n)

#remove
strings.remove('alien')
strings.remove('A')                 # O(n)

print(strings)