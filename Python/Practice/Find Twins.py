'''
Suppose you have two pets and you love both of them very much.
You go to a pet store to buy different articles for your pets.
But you ask salesman that you will buy only those articles which are actually in pair.
In this store, articles are referred as integers. So you have to tell total no. of articles you will buy for your pets.
'''
T = int(input())

for x in range(T):

    N = int(input())

    a = list(map(int, input().split()))

    bucket = {}

    for element in a:
        if element in bucket.keys():
            bucket[element] += 1
        else:
            bucket[element] = 1
    count = 0
    for i in bucket.values():
        count += 2 * int(i / 2)

    print(count)