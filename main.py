def merge(l1, l2):
    l = []
    while len(l1) != 0 and len(l2) != 0:
        l.append(l1.pop() if l1[-1] > l2[-1] else l2.pop())

    l.extend(list(reversed(l1)))
    l.extend(list(reversed(l2)))
    return list(reversed(l))


print(merge([1, 2, 4, 9], [4, 5, 5, 6]))
