def isIsogram(s):
    my_dict = {}
    for i in range(len(s)):
        if s[i] in my_dict.keys():
            return 0
        else:
            my_dict[s[i]] = 1
    return 1

word = input('Enter String : ')
print(isIsogram(word))