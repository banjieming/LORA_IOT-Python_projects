# name = input("What's your name? ")
# print("Hello, " + name + "! Nice to meet you.")


# Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
# xx = tuple(x)
# Traceback (most recent call last):
#   File "<pyshell#0>", line 1, in <module>
#     xx = tuple(x)
# NameError: name 'x' is not defined
# x != y
# Traceback (most recent call last):
#   File "<pyshell#1>", line 1, in <module>
#     x != y
# NameError: name 'x' is not defined
# x = ["apple", "cherry", "banana"]
# y = ["apple", "banana", "cherry"]
# x == y
# False
# x != y
# True
# print(list(xx))
# Traceback (most recent call last):
#   File "<pyshell#6>", line 1, in <module>
#     print(list(xx))
# NameError: name 'xx' is not defined. Did you mean: 'x'?
# print(list())
# []
# x = str(b "hello world")
# SyntaxError: invalid syntax
# print(x)
# ['apple', 'cherry', 'banana']
# x = str(b"Hello World")
# print (x)
# b'Hello World'
# b "Hello World".decode
# SyntaxError: invalid syntax
# b"Hello World".decode()
# 'Hello World'
# "Hello"==[0:5]
# SyntaxError: invalid syntax
# "Hello"== b"Hello World".decode()[0:5]
# True
# "Hello"==stringx[0:5]
# Traceback (most recent call last):
#   File "<pyshell#16>", line 1, in <module>
#     "Hello"==stringx[0:5]
# NameError: name 'stringx' is not defined
# stringx=b"Hello World".decode()[0:5]
# "Hello"==stringx[0:5]
# True
# stringx
# 'Hello'
# stringx[1]
# 'e'
# string[4]
# Traceback (most recent call last):
#   File "<pyshell#21>", line 1, in <module>
#     string[4]
# NameError: name 'string' is not defined. Did you mean: 'stringx'?
# stringx[4]
# 'o'
# stringx[]

# stringx=b"Hello World".decode()[0:5]
# "Hello"==stringx[0:5]
# stringx[1]

# string = " Hello World "
# string.rstrip()

# args = '0x0a 0x0b 0x0c'
# argslist = args.split()
# length = len(argslist)
# for argslist in argslist:
#     if argslist.startswith('0x'):
#         length.append(int(argslist, 16))
#     else:
#         length.append(int(argslist))
# print(length)

args = '0x0a 0x0b 0x0c'
argslist = args.split()
integers = []
for number in argslist:
    if number.startswith('0x'):
        integers.append(int(number, 16))
    else:
        integers.append(int(number))
print(integers)