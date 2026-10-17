from string import ascii_lowercase          ##############example p 67
s = input()
word_s = input()
new_string = ''
s = s.lower()

# need you op
for char in s:
    if char in ascii_lowercase or char == ' ':
        new_string += char
l = new_string.split()
#####################

c = 0
for word in l:
    if word == word_s:
        c += 1
print(c)
