# score = 0
# flag = False
# highest = 0
# lowest = 1000
# ave = 0
# str_scores = ''
# for i in range(10):
#     score = int(input("Enter your score: "))
#     str_scores += str(score)+','
#     ave += score/10
#     if score >100:
#         flag = True
#         break
#     if score > highest:
#         highest = score
#     if score < lowest:
#         lowest = score
# print(str_scores)
# if flag:
#     print("ATTENTION,you entered wrong score")
# print("the highest score is: ",highest)
# print("the lowest score is: ",lowest)
# print("the score average is: ",ave)
############################################################
# lowest = 101
# second_lowest = 101
#
# for i in range(10):
#     score = int(input())
#
#     if score < lowest:
#         second_lowest = lowest
#         lowest = score
#
#     if score < second_lowest and score != lowest:
#         second_lowest = score
########################################################
# from string import ascii_lowercase          ##############example p 67
# s = input()
# word_s = input()
# new_string = ''
# s = s.lower()
# for char in s:
#     if char in ascii_lowercase or char == ' ':
#         new_string += char
# l = new_string.split()
# c = 0
# for word in l:
#     if word == word_s:
#         c += 1
# print(c)
################################################
###################################################
# s = input().split()
# artics = ['a','an','the']
# c = sum([1 for item in s if item in artics])
# print(c)
##################################################
# s = input().split()
# l = ''.join([s[i]+'+' for i in range(len(s)-1)]) + s[len(s) -1]
# print(l)
#####################################
# s = input().split()
# print(s[2])
##########################################
# s = input().split()
# l = [s[i-1] for i in range(1,len(s)) if i % 3 == 0]
# print(l)
######################################################
# from random import shuffle
# s = input().split()
# shuffle(s)
# print(' '.join(s))
##############################################################
# from random import shuffle
# from string import punctuation
# s = input().lower()
# l = s.split()
# x =''
# if l[-1][-1] in punctuation:
#     x = l[-1][-1]
#     l[-1] = l[-1][:-1]
# shuffle(l)
# l[0] = l[0].capitalize()
# print(' '.join(l),x,sep='')
########################################################
# lo0l nam2e heh8 ii1h ysh5k qqw7 6hshd qw3lk cvc4vcv pp9p
# lol iih name qwlk cvcvcv yshk hshd qqw heh ppp
# l = input().split()
# numbers = [i for i in range(10)]
# for row in l:
#     for col in row:
#         if col.isdigit():
#             row = row.replace(col,'')
#             numbers[int(col)] = row
# print(' '.join(numbers))
######################################
# a = [int(i) for i in input().split()]
# b = [int(i) for i in input().split()]
# c = [int(i) for i in input().split()]
# s = 0
# for  item in a:
#     if item in b and item in c:
#         s += item
#         b.remove(item)
#         c.remove(item)
#################################################
# from random import choice
# l = ['1', '2', '3', '4']
# print(choice(l))
######################################################
# from random import  randint
# l = []
# for i in range(6):
#     x = randint(1,48)
#     if x not in l:
#       l.append(x)
# print(l)
########################################
# from random import randint
# user = []
# for i in range(6):
#     user.append(randint(1,10))
# for i in range(1000):
#     for j in range(6):
#         simulate = []
#         simulate.append(randint(1, 10))
#         if user == simulate:
#             aver = i/10
#             print(aver)
##############################################################
# from random import choice
# names = input().split()
# entries = [int(i) for i in input().split()]
# hat = []
# for i in range(len(entries)):
#     for j in range(entries[i]):
#         hat.append(names[i])
# print(choice(hat))
############################################
# s = input()
# if s[3] == '-' and s[6] == '-' and s[:3].isdigit() and s[4:7].isdigit() and s[8:].isdigit():
#     print("Valid")
# elif s[:2] == '1-' and s[5] == '-' and s[9] == '-'and s[2:5].isdigit() and s[6:9].isdigit() and s[10:].isdigit():
#     print("Valid")
# else:
#     print("invalid")
#####################################################
# l = ['shams', 'abdo', 'ali']
# s1 = [i[1:] for i in l]
# s2 = [len(i) for i in l]
# s3 = [len(i) for i in l if len(i)>=3]
# print(s1)
# print(s2)
# print(s3)
#################################################
# n = [str(i) for i in range(100,1001)]
# l = [int(item) for item in n if item[0] == item[-1]]
# print(l)
###############################################
# l = [item for i in range(11) for item in [1,*('0'*i)]]
# print(l)
#################################
# l = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
# gaps = [l[i]-l[i-1] for i in range(1,len(l)) ]
# print(f'the maximum gap is {max(gaps)}')
# repeated = l.count(2)
# per = repeated/len(gaps)*100
# print(f'the percentage is {per}')
##############################################
# l = [[1 for i in range(4)]for j in range(4)]
# ans = 0
# for row in l:
#     for j in row:
#         ans += j
# print(f'the average is {ans/16}')
#############################################
# from random import randint
# l = [[randint(1,100) for i in range(10)] for j in range(10)]
# print_l = [print(i)for i in l]
# x = 1
# larg = max([i for i in l[2] if i > x])
# print(f"the largest value in the third row is {larg}")
#
# x = 100
# smallest = min([row[5] for row in l if row[5]<x])
# print(f"the smallest value in the sixth column is {smallest}")
######################################################################
# from random import randint
# l = [[randint(1,2) for i in range(8)] for j in range(8)] # how to solve l[0][0] = 1
# l[0][0] = 1
# print(l)
###########################################
# from random import randint
# l = [[randint(1,5) for i in range(4)] for j in range(4)]
# ans_row = [sum(i) for i in l]
# #ans_col = [l[j][i]for i in range(len(l)) for j in range(len(l))] how to append the sum of items in colum not the items
# ans_col2 = []
# ans_r = []
# for i in range(len(l)):
#     x = []
#     for j in range(len(l)):
#         x.append(l[j][i])
#     ans_col2.append(sum(x))
# flag = True
# i,j = 0,0
# while flag:
#     x = []
#     x.append(l[i][j])
#     i += 1
#     j += 1
#     if i == 3:
#         ans_r.append(sum(x))
#         flag = False
#
# print(l)
# print(ans_row)
# print(ans_col2)
####################################################
# standard = [0.0254,0.9144,1609.34, 0.001, 0.01,1,1000] #0 inch, 1 yard, 2 mile, 3 mm, 4 cm, 5 m, 6 km
# s = float(input("Enter the length: "))
# x = input("What is the current unit? ")
# y = int(input("What unit you would like to convert it to? "))
# print(s * standard[y])
#############################################
# from random import randint
# l = [[randint(0,1) for i in range(5)] for j in range(5)]
# s = [int(i) for i in input().split()]
# print(l)
# if l[s[0] -1][s[1] -1] == 1 :
#     print("Hit")
# else:
#     print("Miss")
############################################
# from string import printable
# from random import randint,shuffle
# random_chars = []
# for i in range(18):
#     x = randint(0, len(printable) - 1)
#     if printable[x] not in random_chars:
#         random_chars.append(printable[x])
# random_chars *= 2
# shuffle(random_chars)
# l = [[1 for i in range(6)] for j in range(6)]
# for i in range(6):
#     for j in range(6):
#         l[i][j] = random_chars.pop()
#
# print(l)
######################################################
# from random import randint
# l = [[randint(0,1) for j in range(5)] for i in range(5)]
# flag = True
# while flag:
#     x,y = randint(0,4),randint(0,4)
#     if l[x][y] == 0:
#         l[x][y] = 1
#         flag = False
# ones = True
# for row in l:
#     for col in row:
#         if col == 0:
#             ones = False
# if ones:
#     print("all the entries are one")
######################################################
# x = 0
# for i in range(3):
#     for j in range(3):
#         print(x,end=' ')
#         x +=1
#     print()
# ##########################################################
# for i in range(3):
#     for j in range(3):
#         print(f"({i},{j})",end=' ')
#     print()
#####################################################



# i = 1
# while i<= 50:
#     print(i)
#     i += 1
# ##########################################
# s = input()
# i = 0
# while len(s) > i:
#     print(s[i])
#     i += 1
##########################################
# s = input()
# i = 1
# while len(s) > i:
#     print(s[i])
#     i += 2
#####################################
# weight = float(input("enter the weight: "))
# while weight <= 0:
#     print("the entry is invalid!")
#     weight = float(input("enter the weight: "))
# print(f"the weight in pounds is {weight * 2.2}")

#####################################################################
# c_pass = 1234
# in_pass = 0
# i = 1
# while i <6 and c_pass != in_pass :
#     i += 1
#     in_pass = int(input(" enter the password: "))
#     if c_pass == in_pass:
#         print(" log in the system ")
#     else:
#         print(" reenter the password,please ")
# if c_pass != in_pass:
#     print(" you are blocked! ")
#############################################
# c = 0
# score = 0
# sum_score = 0
# x = 0
# while score >= 0:
#     score = float(input("enter your score: "))
#     x += 1
#     if score >= 90:
#         c += 1
#     sum_score += score
# print(f"the average is {sum_score/x}")
# if c == 1 :
#     print(f"you have 1 degree")
# elif c > 1:
#     print(f"you have {c} A degrees")
##################################################################
# s = input("enter the string ")
# x = input("enter the letter ")
# i= 0
# while i < len(s) and x in s:
#     i += 1
#     print(s.index(x))
#     break
# else:
#     print(f"{x} not in the string")
####################################################
# s = input("enter the string ")
# x = input("enter the letter ")
# for i in range(len(s)):
#     if x in s:
#         print(s.index(x))
#         break
# else:
#     print(f"{x} not in the string")
#####################################################
# number = [int(i) for i in input().split()]
# number.sort()
# com_divisor = 2
# i = 2
# while i < number[0]:
#     if number[0]%i == 0 and number[1]%i == 0:
#         com_divisor = i
#     i += 1
# print(f"the common divisor is {com_divisor}")
##########################################################################
# from random import randint
# l = ['shams', 'abdo', 'adam', 'yara']
# while True:
#     x = randint(0,len(l) -1)
#     for i in range(len(l[x])):
#         if l[x][i] in l[x][i+1 : ]:
#             break
#     else:
#         print(l[x])
#         break
#################################################
# from random import randint
# l = [[0 for i in range(5)] for j in range(5)]
# n = 0
# while n <10:
#     x = randint(0,4)
#     y = randint(0,4)
#     if l[x][y] != 1:
#         l[x][y] = 1
#         n += 1
# print(l)
##############################################
# l = [int(i) for i in input().split()]
# i = 0
# while i < len(l) -1 :
#     if l[i] == 1:
#         l[i] = 0
#         break
#     i += 1
# print(l)
#############################################################
# from random import randint
# l = [i for i in range(1,4)]
# c_x , c_y = 0 , 0
# while c_x <=3 or c_y <= 3 :
#     x = int(input("enter 1 for Rock, 2 for Paper, 3 for Scissors: "))
#     y =randint(1,3)
#     if y == 3 and x == 1 :
#         c_x += 1
#     elif y == 1 and x == 3 :
#         c_y += 1
#     elif x < y :
#             c_y += 1
#     elif x > y :
#         c_x += 1
# if c_x > c_y:
#     print("You win!!")
# else:
#     print("You lose!!")
###########################################################
# from random import randint
# money = 100
# while True:
#     guess = int(input("enter 1 head or 2 tail: "))
#     x = randint(1,2)
#     if guess == x :
#         money += 9
#     else:
#         money -= 10
#     if money <= 0 or money > 200:
#         break
# print(money)
#####################################
# from random import randint
# l= ['canada','usa','egypt','belgium']
# picked = l[randint(0,len(l) -1)]
# flag = True
# while flag:
#     x = 0
#     guess = input("enter your guessing: ")
#     if guess in picked:
#         for i in range(len(picked)):                      ?????????????????????????????
#             if picked[i] == guess:
#                 print(guess,end='')
#             else:
#                 print('-',end='')

    # else:
    #     x += 1
    # if x == 5:
    #     flag = False
####################################################
# from random import randint
# l = [[0 for i in range(6)] for j in range(6)]
# n = 0
# while n < 12 :
#     n += 1
#     x = randint(0,5)
#     y = randint(0,5)
#     l[x][y] = 1
# print(l)
##################################
# from random import randint
# l = [[0 for i in range(9)] for j in range(9)]
# n = 0
# while n < 81:
#     x = randint(0,8)
#     y = randint(0,8)
#     num = randint(1,9)
#     if num not in l[:][y] and num not in l[x][:]:               ??????????????????????????????
#         n += 1
#         l[x][y] = num
# print(l)
##############################################
# num = int(input("enter the numerator "))
# den = int(input("enter the denominator "))
# ans = '.'
# if num > den :
#     ans = str(num // den) + '.'
#     num = num % den
# i = 0
# while i < 7:
#     i += 1
#     ans += str((num * 10) // den)
#     num = (num * 10) % den
# print(ans[4])
######################################################
# from string import printable
# from random import randint
# l = [["*" for i in range(5)] for j in range(5)]
#
# indx = [randint(0,35) for i in range(12)]
# new_list = []
# for i in indx:
#     new_list.append(printable[i])
# new_list = 2 * new_list[:] + ['x']            #new_list is 1D
#
# letter_2D = [[0 for i in range(5)] for j in range(5)]                               #make letters 2D
# for i in range(5):
#     for j in range(5):
#         letter_2D[i][j] = new_list.pop()
# turns = 5
# flag = True
# while turns != 0 :
#     print(l)
#     grid = [int(i) for i in input("enter the coordinates ").split()]
#     x,y = grid[0],grid[1]
#     l[x][y] = letter_2D[x][y]
#     char_1 = letter_2D[x][y]
#     print(l)
#     grid = [int(i) for i in input("enter the coordinates ").split()]
#     i, j = grid[0], grid[1]
#     l[i][j] = letter_2D[i][j]
#     char_2 = letter_2D[i][j]
#     print(l)
#     if char_1 != char_2:
#         l[x][y] = '*'
#         l[i][j] = '*'
#         turns -= 1
#     if '*' not in l:
#         print("You win!!")
#         break
# else:
#     print("You lose!!")
###########################################################
# print(list(range(3,100,3)))
##########################################
# weight = float(input("enter your weight in kilograms: "))
# ans = weight * 2.2
# print('your weight in pounds is {:.f}'.format(ans))
########################################################
# word = input("enter he word: ")
# l = list(word)
# l.sort()
# sorted_word = ''.join(l)
# print(sorted_word)
# ################################
# items = [i for i in input("enter your items: ").split()]
# prices = [float(i) for i in input("enter the prices: ").split()]
# i = 0
# while i < len(items):
#     print('{:9s}  $  {:7.2f} '.format(items[i], prices[i]))
#     i += 1
###################################################
# l1 = [i for i in input().split()]
# l2 = [i for i in input().split()]
# flag = True
# while flag:
#     for item in l1:
#         if item in l2:
#             flag = False
#     break
# if flag:
#     print("they are different")
# else:
#     print("they have common item")
####################################################
# l = ['1'*(i+1) for i in range(100)]
# for i in range(len(l)):
#     l[i] = int(l[i])
# print(l)
##########################################
# divisor = []
# for i in range(6,1000,10):
#     if i%7 == 0:
#         divisor.append(i)
# print(divisor)
#########################################
# c = 0
# for i in range(1,1000):
#     i = str(i)
#     if '3' in i :
#         c += 1
# print(c)
#################################
# ans = []
# for i in range(10,100):
#     c = 0
#     num = str(i)
#     rev_num = str(num)[::-1]
#     while num != rev_num and c <= 20:
#         c += 1
#         num = str(int(num) + int(rev_num))
#         rev_num = str(num)[::-1]
#     if c > 20:
#         ans.append(i)
#
# for i in ans:
#     print(i)
###############################################
# plind = []
# for i in range(100000,999999 + 1):
#     rev_i = str(i)[::-1]
#     if i == int(rev_i):
#         plind.append(i)
#
# for i in range(len(plind)):
#     for j in range(i, len(plind)):
#         if plind[j] - plind[i] < 20 :
#             print(plind[i], plind[j])
#####################################################3
# # 3- if i has 6 or 9 switch them and check if rev_i = i or not (if true append i in ans list)
# # 4- if i doesn't have 6 or 9 (append i in ans list)
# nums = ['2','3', '4', '5', '7']
# for i in range(1,100000 +1):
#     # 1- check if i is a palindromic number
#     rev_i = str(i)[::-1]
#     if i == int(rev_i):
#         # 2- check that i don't have any of nums list
#         for item in nums:
#             if item not in rev_i:
#                 continue
#         else:
#             if '6' in rev_i :
###############################################################
# 1- convert int i to string
# 2- add = sum of i digits ex: i = '123', sum = int('1') + int('2') + int('3')
# 3- multi = multiple of i digits , multi = int('1') * int('2') * int('3')
# 4- if add + multi == i , then  append i in ans list
# ans = []
# for i in range(1,10000):
#     num = str(i)
#     add, multi = 0, 1
#     for item in num:
#         add += int(item)
#         multi *= int(item)
#     if add + multi == i:
#         ans.append(i)
# print(ans)
##########################################
# 1- take the number from user (name is num)
# 2- move first digit to mostright (name is re_num)
# 3- if re_num / num == 3.5 , then print valid else print not valid

# num = input("enter the number:")
# re_num = num[1:] + num[0]
# if int(re_num)*2 == int(num)*7 :
#     print("valid")
# else:
#     print("not valid")
###################################################
# 1- find the number that divided by 5
# 2- while number %5 ==0 then numer /5 , increase c by 1
# c = 0
# for i in range(1,10):
#     num = i
#     while num%5 == 0:
#         num = i/5
#         c += 1
# print(c)
#################################################
# height = input("enter the height: ")
# mod = ''
# num = ''
# for i in range(len(height)):
#     if height[i] == '.':
#         mod = float(height[i:])
#         num = height[:i]
#         break
# print(f"{num} feed and {int(mod*12)} inch")
#####################################################
# 1- take input in while loop until input "done"
# 2- for loop to input, if i == " ' ",then input[:i]
# 3- if input[:i] = 5 increase
# x = ''
# feets = [0 for i in range(8)]
# while x != 'done':
#     x = input('enter the height (feet’inches")')
#     for i in range(len(x)):
#         if x[i] == '’':
#             feet = x[:i]
#             feets[int(feet)] += 1
# for i in range(4,8):
#     print(feets[i])
####################################################
# 1- take all scores in while loop , break when input "done"
# 2- split the input by "-"
# 3- if input[i] > greatest then, greatest = input[i]
# 4- if input[i] < smallest then, smallest = input[i]
# 5- print greatest and smallest
# greatest = 0
# smallest = 100
# flag = True
# while flag:
#     x = input()
#     if x != 'done':
#         x = [int(i) for i in x.split('-')]
#         for item in x:
#             if item > greatest:
#                 greatest = item
#             if item < smallest:
#                 smallest = item
#     else:
#         flag = False
# print(greatest,smallest)
###################################################
# 1- take all scores in while loop , break when input "done"
# 2- split the input by "/"
# 3- for loop in input when i = '/' if num[:i] == 2 increase c_2 by 1
# 4- when i = '/' if num[i+1:] == 25 increase c_25 by 1
# c_2,c_25 = 0,0
# flag = True
# while flag:
#     x = input("enter the birthday(mm/dd) ")
#     if x != 'done':
#         x = [int(i) for i in x.split('/')]
#         if x[0] == '2':
#             c_2 += 1
#         elif x[1] == '25':             ???????????????????????????????
#             c_25 += 1
#     else:
#         flag = False
# print(c_2,c_25)
###############################################
# months = [0, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# flag = True
# while flag:
#     x = input("Enter the date (mm/dd/yy)")
#     if x != 'done':
#         x = [int(i) for i in x.split('/')]
#         if x[2] > 27:         #19??
#             print(f"{months[x[0]]}{x[1]}, {1900 + x[2]}")
#         else:          #20??
#             print(f"{months[x[0]]}{x[1]}, {2000 + x[2]}")
#     else:
#         flag = False
#########################################################################
# frac = [int(i) for i in input("enter the fraction ").split('/')]
# num,den = frac[0],frac[1]
# flag = True
# while flag:
#     for i in range(2,den):
#         if num%i == 0 and den%i ==0:
#             num //= i
#             den //= i
#     else:
#         flag = False
# print(f"{num}/{den}")
#########################################################




########################################################
# flag = True
# d = {}
# while flag:
#     x = input("enter the product and its price")
#     if x == 'done':
#         flag = False
#     else:
#         x = x.split()
#         d[x[0]] = int(x[1])
#
#
# fll = True
# while fll:
#     x = input("what do you search for? ")
#     if x == "done":
#         fll = False
#     else:
#          print(d[x])
# check = True
# while check:
#     x = input("enter price dollar: ")
#     if x == 'done':
#         check = False
#     else:
#         for w in d:
#             if d[w] < int(x):
#                 print(w)
###################################################
# d = { 'January' :31, 'February' :28, 'March' :31, 'April' :30,
#       'May' :31, 'June' :30, 'July' :31, 'August' :31,
#       'September' :30, 'October' :31, 'November' :30, 'December' :31}
# x = input("enter the month: ")
# print(d[x])

# months = list(d)
# months.sort()   # sort the key alpha
# # print(months)
#
# days = list(d.values())
# days.sort()
# for i in days:
#     for w in months:
#         if d[w] == i:
#             print(f"({w},{i})")
#             months.remove(w)
# x = input("enter the month: ")
# for w in d:
#     if x == w[:3]:
#         print(d[w])
#######################################################
# d = {s : len(s) for s in input().split()}
# user = input("Enter username and password: ").split()
# for w in d:
#     if user[0] not in d:
#         print("you are not a valid user!")
#     while int(user[1]) != d[user[0]]:
#         user[1] = input("enter the correct password: ")
#     print("You are now logged in  to the system")
#     break
###############################################
# flag = True
# d = {}
# wins = []
# teams = []
# while flag:
#     x = input("enter team information: ")
#     if x == 'done':
#         flag = False
#     else:
#         x = x.split()
#         d[x[0]] = [int(i) for i in x[1:]]
#         wins.append(d[x[0]][0])
# team = input("enter name of the team: ")
# ave = (d[team][0]/ sum(d[team])) * 100
# print(f"the team’s winning percentage is {ave}")
# print("the number of wins of each team ",wins)
# for w in d:
#     if d[w][0] > d[w][1]:
#         teams.append(w)
# print(teams)
###################################################
# flag = True
# d = {}
# while flag:
#     x = input("enter information: ")
#     if x == 'done':
#         flag = False
#     else:
#         x = x.split(' - ')
#         team1 = x[0].split()
#         team2 = x[1].split()
#         if team1[1] > team2[1]:
#             d[team1[0] + team2[0]] = [team1[1],team2[1]]
#         else:
#             d[team2[0] + team1[0]] = [team2[1],team1[1]]
# print(d)
#######################################################
# from random import randint
# l = [[randint(1,10) for i in range(5)] for j in range(5)]
# d = {}
# for row in l:
#     for i in row:
#         if i not in d:
#             d[str(i)] = 1
#         else:
#             d[str(i)] += 1
# print(d)
###########################################
# from random import randint
# player1= []
# player2= []
# cards = [{ 'value' :i, 'suit' :c}
# for c in [ 'spades' , 'clubs' , 'hearts' , 'diamonds' ]
# for i in range(2,15)]
#
# for i in range(3):
#     player1.append(cards[randint(0,len(cards) -1)]['value'])
# for i in range(3):
#     player2.append(cards[randint(0,len(cards) -1)]['value'])
# player1.sort()
# player2.sort()
# for i in range(2,-1,-1):
#     if player1[i] > player2[i]:
#         print(1)
#         break
#     elif player2[i] > player1[i]:
#         print(2)
#         break
# else:
#     print("draw")
####################################################
# from random import randint
# cards = [{'value':j,'suit': i} for i in ['spades', 'clubs', 'hearts', 'diamonds'] for j in range(2,15)]
# flush = []
# x = randint(0,len(cards) -1)
# flush.append(cards[x])
# while len(flush) != 3:
#     a = randint(0, len(cards) -1)
#     if cards[a]['suit'] == flush[0]['suit']:
#         flush.append(cards[a])
# print(flush)
# while len(flush) != 3:
#     a = randint(0, len(cards) -1)
#     if cards[a]['value'] == flush[0]['value']:
#         flush.append(cards[a])
# print(flush)
# while len(flush) != 3:
#     a = randint(0, len(cards) -1)
#     if cards[a]['value'] not in flush and cards[a]['suit'] != flush:
#         flush.append(cards[a])
# print(flush)
##########################################################
#   10 is probability

#
# def is_rep_char_match(s1, s2):
#     is_match = True
#     d = {}
#     for i in range(len(s2)):
#         if s1[i] not in d:
#             d[s1[i]] = s2[i]
#         else:
#             if d[s1[i]] != s2[i]:
#                 is_match = False
#                 break
#     return is_match
#
#
# s1 = input("enter the first string: ")
# s2 = input("enter the second string: ")
#
# is_no_char_match = True
#
# for i in range(len(s2)):
#     if s1[i] == s2[i]:
#         is_no_char_match = False
#         break
#
# if is_no_char_match and is_rep_char_match(s1, s2) and is_rep_char_match(s2, s1):
#     print("encoded")
# else:
#     print("not encoded")
#
#
#
#################################################
# d = {'Minor': [3,7], 'Augmented fifth': [4,8], 'Minor fifth': [4,6], 'Major sixth': [4,7,9], 'Minor sixth': [3,7,9],
#      'Dominant seventh':[4,7,10], 'Minor seventh':[3,7,10], 'Major seventh': [4,7,11], 'Diminished seventh': [3,6,10]}
# notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
# letter, name = input("enter the name of note: ").split()
# print(letter,end='')
# ind = notes.index(letter)
# for i in d[name]:
#     print(notes[i+ind],end='')
################################################
d = {'Minor': [3,7], 'Augmented fifth': [4,8], 'Minor fifth': [4,6], 'Major sixth': [4,7,9], 'Minor sixth': [3,7,9],
     'Dominant seventh':[4,7,10], 'Minor seventh':[3,7,10], 'Major seventh': [4,7,11], 'Diminished seventh': [3,6,10]}
notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
letter, name = input("enter the name of note: ").split()
print(letter,end='')
ind = notes.index(letter)
for i in d[name]:
    print(notes[i+ind],end='')
