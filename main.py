"""
p27
Write a program that simulates all possible rolls of four dice and for each simulated roll, finds
the sums of pairs of dice. For instance, if the roll is 5 1 2 4, the sums are 6, 8, 9, 3 ,5, and 6.
For each of the possible sums from 2 to 12, find the total number of simulated rolls in which
the sum appears and what percentage of the simulated rolls had those sums appear. Output
the totals and percentages, nicely formatted, with the percentages formatted to one decimal
place. To check your work, you should find that the sum 2 comes up in 171 rolls, which is
13.2% of the rolls.
"""
d = {}
for i in range(1, 6 +1):
    for j in range(1, 6 +1):
        for x in range(1, 6 +1):
            for y in range(1, 6 +1):
                roll = str(i) + str(j) + str(x) + str(y)
                # print(roll)
                for a in range(4):
                    for b in range(a+1,4):
                        sum_pair = int(roll[a]) + int(roll[b])
                        if sum_pair not in d:
                            d[sum_pair] = 1
                        else:
                            d[sum_pair] += 1

base = sum(list(d.values()))
percentage = []
for key in d:
    perc = (d[key] / base) * 100
    percentage.append(perc)
print(sum(percentage))
for i in percentage:
    print('{:.1f}'.format(i),end=' ')