'''Sherlock is a famous detective. This time he's working to catch a team of gangsters.
 Sherlock knows that the head of gangsters will be caught if he catches his underlings.
 The gangsters work under a hierarchical system. Each member reports exactly to one other member of the town. It's clear that there are no cycles in their reporting system.There are N people in the town, for simplicity indexed from 1 to N, and Sherlock knows who each of them report to. Member i reports to member Ai, and head of Gangsters does not report to anybody.
 Sherlock wants to find the members to whom nobody reports as these members could help him bring down the organization.'''


def sherlock(arr, n):
    reported = {}
    for i in range(n):
        reported[i] = arr[i]
    i = 1
    not_reported = []
    while i <= n:
        if i not in reported.values():
            not_reported.append(i)
        i += 1
    return not_reported


t = int(input())
for _ in range(t):
    n = int(input())
    gangsters = list(map(int, input().split()))

    not_reported = sherlock(gangsters, n)

    for element in not_reported:
        print(element, end=' ')
    print()