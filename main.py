lowest = 101
second_lowest = 101

for i in range(10):
    score = int(input())

    if score < lowest:
        second_lowest = lowest
        lowest = score

    if score < second_lowest and score != lowest:
        second_lowest = score
