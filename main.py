score = 0
flag = False
highest = 0
lowest = 1000
ave = 0
str_scores = ''
for i in range(10):
    score = int(input("Enter your score: "))
    str_scores += str(score)+','
    ave += score/10
    if score >100:
        flag = True
        break
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score
print(str_scores)
if flag:
    print("ATTENTION,you entered wrong score")
print("the highest score is: ",highest)
print("the lowest score is: ",lowest)
print("the score average is: ",ave)