"""
p14
Dictionaries provide a convenient way to store structured data. Here is an example dictionary:
d=[{ ' name ' : ' Todd ' , ' phone ' : ' 555-1414 ' , ' email ' : ' todd@mail.net ' },
{ ' name ' : ' Helga ' , ' phone ' : ' 555-1618 ' , ' email ' : ' helga@mail.net ' },
{ ' name ' : ' Princess ' , ' phone ' : ' 555-3141 ' , ' email ' : ' ' },
{ ' name ' : ' LJ ' , ' phone ' : ' 555-2718 ' , ' email ' : ' lj@mail.net ' }]
Write a program that reads through any dictionary like this and prints the following:
(a) All the users whose phone number ends in an 8
(b) All the users that don’t have an email address listed
"""
l = []
flag = True
while flag:
    d = {}
    d['name'] = input("enter your name: ")
    d['phone'] = input("enter your phone: ")
    d['email'] = input("enter your email: ")
    l.append(d)
    flag = bool(input("Are you finished? ").capitalize())

list_phone = []
list_email = []
for row in l:
    item = list(row.values())
    if item[1][-1] == '8':
        list_phone.append(item[0])
    if item[2] == ' ':
        list_email.append(item[0])

print("users whose phone number ends in an 8 ",list_phone)
print("users that don’t have an email address listed ",list_email)